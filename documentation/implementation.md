# Implementation

## UI
- The application features a basic user interface using Python Flask.
- Users can upload files by clicking the Choose file button and then pressing the Upload button.
- Performance tests are ran alongside the compression process by clicking the Compress File button.
- Test coverage statistics are displayed on the front page.

To run the application, please refer to the instructions in the README front page.

## File Handling
- Uploaded files are stored in session.
- Uploaded files are processed and read as bytes for compression.

## Compression Algorithms

### Huffman Compression

- A Huffman tree is constructed based on character frequencies.
- Huffman codes are generated for compression and decompression.
- Data is compressed using Huffman codes and can be decompressed.

### LZW Compression

- A dictionary is used to track data patterns.
- Data is compressed using LZW encoding and can be decompressed.

## Performance Metrics

- The application calculates and displays performance metrics for both compression algorithms:
  - Integrity checks verify if decompressed data matches the original data.
  - Compression efficiency is calculated as a percentage.

## LLM Usage

- The LLM on chat.openai.com has been used to assist in debugging complicated issues and obtaining information on Python-specific matters. Weekly reports provide more detailed insight into its usage.

