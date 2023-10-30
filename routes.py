import os
import unittest
from os.path import getsize

from flask import (
    render_template, request, session, redirect,
    url_for, send_from_directory
)

from src.huffman import huffman_compress, huffman_decompress
from src.lzw import lzw_compress, lzw_decompress
from src.utils import calculate_efficiency

ASSETS_FOLDER = 'assets'


def register_routes(app, cov):
    app.config['ASSETS_FOLDER'] = ASSETS_FOLDER

    @app.route('/')
    def index_route():
        upload_status = session.get('upload_status')
        uploaded_file = session.get('uploaded_file')
        return render_template('index.html',
                               upload_status=upload_status,
                               uploaded_file=uploaded_file)

    @app.route('/upload', methods=['POST'])
    def upload_file_route():
        file = request.files['file']
        if file:
            filepath = os.path.join(app.config['ASSETS_FOLDER'], file.filename)
            file.save(filepath)
            session['file_path'] = filepath
            session['upload_status'] = 'Upload complete'
            session['uploaded_file'] = file.filename
        else:
            session['upload_status'] = 'No file uploaded'
        return redirect(url_for('index_route'))

    @app.route('/compress', methods=['POST'])
    def compress_file():
        filepath = session.get('file_path')
        error = None
        results = None

        if not filepath:
            error = "File upload failed or no file has been uploaded"
        else:
            try:
                # Load the file to be compressed from disk
                with open(filepath, 'rb') as f:
                    file_data = f.read()

                # Compress the file with both algorithms
                huffman_compressed, huffman_codes = huffman_compress(file_data)
                # lzw allows defining dictionary size, defaults to 65536
                lzw_compressed = lzw_compress(file_data, 65536)

                # Create filepath names for compressed files
                huffman_filepath = filepath + '_huffman_compressed'
                lzw_filepath = filepath + '_lzw_compressed'

                # Save compressed files to disk
                with open(huffman_filepath, 'wb') as f:
                    f.write(huffman_compressed)
                with open(lzw_filepath, 'wb') as f:
                    f.write(lzw_compressed)

                # Decompress the compressed files for integrity check
                huffman_decompressed = huffman_decompress(huffman_compressed,
                                                          huffman_codes)
                # lzw allows defining dictionary size, defaults to 65536
                lzw_decompressed = lzw_decompress(lzw_compressed, 65536)

                # Check that  original file data matches decompressed file data
                huffman_integrity = huffman_decompressed == file_data
                lzw_integrity = lzw_decompressed == file_data

                # Use os getsize method to get file sizes
                original_size = getsize(filepath)
                huffman_compressed_size = getsize(huffman_filepath)
                lzw_compressed_size = getsize(lzw_filepath)

                # Calculate how efficiently the algorimths compressed the files
                huffman_efficiency = calculate_efficiency(
                    original_size, huffman_compressed_size)
                lzw_efficiency = calculate_efficiency(
                    original_size, lzw_compressed_size)

                results = {
                    'huffman_integrity': huffman_integrity,
                    'lzw_integrity': lzw_integrity,
                    'huffman_efficiency': huffman_efficiency,
                    'lzw_efficiency': lzw_efficiency,
                    'original_size': original_size,
                    'huffman_compressed_size': huffman_compressed_size,
                    'lzw_compressed_size': lzw_compressed_size,
                }
            except Exception as e:
                error = f"Error occurred: {str(e)}"

        return render_template('index.html', error=error, results=results)

    @app.route('/coverage')
    def test_coverage_route():
        # Run unit tests
        test_loader = unittest.TestLoader()
        test_suite = test_loader.discover('tests')
        test_runner = unittest.TextTestRunner()
        test_runner.run(test_suite)

        # Generate test coverage report
        cov.stop()
        cov.save()
        cov.html_report()
        return send_from_directory('htmlcov', 'index.html')
