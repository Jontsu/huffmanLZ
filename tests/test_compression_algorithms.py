import unittest

from src.huffman import huffman_compress, huffman_decompress
from src.lzw import lzw_compress, lzw_decompress


class TestCompressionAlgorithms(unittest.TestCase):
    """Unit tests for the compression algorithms: Huffman and LZW."""

    def test_repetitive_string_compression(self):
        repetitive_data = "A" * 1000
        compressed_data_huffman, _ = huffman_compress(repetitive_data)
        compressed_data_lzw = lzw_compress(repetitive_data)

        self.assertNotEqual(compressed_data_huffman, "",
                            "Huffman repetitive string compression failed")
        self.assertNotEqual(compressed_data_lzw, [],
                            "LZW repetitive string compression failed")

    def test_repetitive_string_decompression(self):
        repetitive_data = "A" * 1000
        compressed_data_huffman, codes = huffman_compress(repetitive_data)
        compressed_data_lzw = lzw_compress(repetitive_data)

        decompressed_data_huffman = huffman_decompress(
            compressed_data_huffman, codes)
        decompressed_data_lzw = lzw_decompress(compressed_data_lzw)

        self.assertEqual(decompressed_data_huffman, repetitive_data,
                         "Huffman repetitive string decompression failed")
        self.assertEqual(decompressed_data_lzw, repetitive_data,
                         "LZW repetitive string decompression failed")

    def test_short_string_compression(self):
        short_data = "AB"
        compressed_data_huffman, _ = huffman_compress(short_data)
        compressed_data_lzw = lzw_compress(short_data)

        self.assertNotEqual(compressed_data_huffman, "",
                            "Huffman short string compression failed")
        self.assertNotEqual(compressed_data_lzw, [],
                            "LZW short string compression failed")

    def test_short_string_decompression(self):
        short_data = "AB"
        compressed_data_huffman, codes = huffman_compress(short_data)
        compressed_data_lzw = lzw_compress(short_data)

        decompressed_data_huffman = huffman_decompress(
            compressed_data_huffman, codes)
        decompressed_data_lzw = lzw_decompress(compressed_data_lzw)

        self.assertEqual(decompressed_data_huffman, short_data,
                         "Huffman short string decompression failed")
        self.assertEqual(decompressed_data_lzw, short_data,
                         "LZW short string decompression failed")

    def test_long_string_compression(self):
        long_data = (
            "ABCDEFGHIJKLMNOPQRSTUVWXYZabcefghijklmnopqrstuvwxyz1234567890"
            * 50
        )

        compressed_data_huffman, _ = huffman_compress(long_data)
        compressed_data_lzw = lzw_compress(long_data)

        self.assertNotEqual(compressed_data_huffman, "",
                            "Huffman long string compression failed")
        self.assertNotEqual(compressed_data_lzw, [],
                            "LZW long string compression failed")

    def test_long_string_decompression(self):
        long_data = (
            "ABCDEFGHIJKLMNOPQRSTUVWXYZabcefghijklmnopqrstuvwxyz1234567890"
            * 50
        )

        compressed_data_huffman, codes = huffman_compress(long_data)
        compressed_data_lzw = lzw_compress(long_data)

        decompressed_data_huffman = huffman_decompress(
            compressed_data_huffman, codes)
        decompressed_data_lzw = lzw_decompress(compressed_data_lzw)

        self.assertEqual(decompressed_data_huffman, long_data,
                         "Huffman long string decompression failed")
        self.assertEqual(decompressed_data_lzw, long_data,
                         "LZW long string decompression failed")


if __name__ == '__main__':
    unittest.main()
