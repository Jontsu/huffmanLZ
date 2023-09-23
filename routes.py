from flask import render_template, request, session, redirect, url_for, send_from_directory

import unittest

from src.huffman import huffman_compress, huffman_decompress
from src.lzw import lzw_compress, lzw_decompress
from src.utils import calculate_efficiency


def register_routes(app, cov):

    @app.route('/')
    def index_route():
        upload_status = session.get('upload_status')
        uploaded_file = session.get('uploaded_file')
        return render_template('index.html', upload_status=upload_status, uploaded_file=uploaded_file)

    @app.route('/upload', methods=['POST'])
    def upload_file_route():
        file = request.files['file']
        if file:
            # temporary solution for UI testing until binary solution is implemented
            file_data = file.read().decode('utf-8', errors='replace') # temporary
            session['file_data'] = file_data # temporary
            session['upload_status'] = 'Upload complete'
            session['uploaded_file'] = file.filename
        else:
            session['upload_status'] = 'No file uploaded'
        return redirect(url_for('index_route'))
                             
    @app.route('/compress', methods=['POST'])
    def compress_file():
        file_data = session.get('file_data')
        error = None
        results = None

        if not file_data:
            error = "File upload failed or no file has been uploaded"
        else:
            try:
                huffman_compressed, huffman_codes = huffman_compress(file_data)
                lzw_compressed = lzw_compress(file_data)

                huffman_decompressed = huffman_decompress(huffman_compressed, huffman_codes)
                lzw_decompressed = lzw_decompress(lzw_compressed)

                huffman_integrity = huffman_decompressed == file_data
                lzw_integrity = lzw_decompressed == file_data

                huffman_efficiency = calculate_efficiency(file_data, huffman_compressed)
                lzw_efficiency = calculate_efficiency(file_data, lzw_compressed)

                results = {
                    'huffman_integrity': huffman_integrity,
                    'lzw_integrity': lzw_integrity,
                    'huffman_efficiency': huffman_efficiency,
                    'lzw_efficiency': lzw_efficiency
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
        