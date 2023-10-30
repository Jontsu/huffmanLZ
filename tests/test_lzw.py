import unittest

from src.lzw import (
    initialise_dictionary, add_to_dictionary, lzw_compress,
    lzw_decompress, get_next_code)


class TestLZWAlgorithm(unittest.TestCase):
    """Unit tests for LZW compresion algorithm functions."""

    def test_initialise_dictionary_compress(self):
        dictionary, bit_length = initialise_dictionary('compress', 512)
        self.assertEqual(dictionary['A'], 65)
        self.assertEqual(bit_length, 9)

    def test_initialise_dictionary_decompress(self):
        dictionary, bit_length = initialise_dictionary('decompress', 512)
        self.assertEqual(dictionary[65], bytes([65]))
        self.assertEqual(bit_length, 9)

    def test_initialise_dictionary_invalid_mode(self):
        dictionary, bit_length = initialise_dictionary('invalid_mode', 512)
        self.assertEqual(dictionary, None)
        self.assertEqual(bit_length, 0)

    def test_add_to_dictionary_within_limit(self):
        dictionary = {1: 'A', 2: 'B'}
        add_to_dictionary(dictionary, 3, 'C', 3)
        self.assertTrue(3 in dictionary)

    def test_add_to_dictionary_beyond_limit(self):
        dictionary = {1: 'A', 2: 'B', 3: 'C'}
        add_to_dictionary(dictionary, 4, 'D', 3)
        self.assertFalse(4 in dictionary)

    def test_lzw_append_last_remaining_string(self):
        data = b""
        dictionary_size = 512
        compressed_data = lzw_compress(data, dictionary_size)
        self.assertEqual(compressed_data, b"\x00")

    def test_lzw_compress_decompress_small_dictionary_size(self):
        data = b"ABABABABA"
        dictionary_size = 512
        compressed_data = lzw_compress(data, dictionary_size)
        decompressed_data = lzw_decompress(compressed_data, dictionary_size)
        self.assertEqual(data, decompressed_data)

    def test_lzw_compress_decompress_default_dictionary_size(self):
        data = b"ABABABABA"
        compressed_data = lzw_compress(data)
        decompressed_data = lzw_decompress(compressed_data)
        self.assertEqual(data, decompressed_data)

    def test_lzw_compress_decompress_large_dictionary_size(self):
        data = b"ABABABABA"
        dictionary_size = 131072
        compressed_data = lzw_compress(data, dictionary_size)
        decompressed_data = lzw_decompress(compressed_data, dictionary_size)
        self.assertEqual(data, decompressed_data)

    def test_lzw_compress_decompress_complex_characters(self):
        data = b"Testing algos! 1234567890 @#$%^&*()_+[]{}|;:',.<>/?`~"
        compressed_data = lzw_compress(data)
        decompressed_data = lzw_decompress(compressed_data)
        self.assertEqual(data, decompressed_data)

    def test_get_next_code(self):
        compressed_bits = "010101"
        bit_length = 3
        code, bit_index = get_next_code(compressed_bits, 0, bit_length)
        self.assertEqual(code, 2)
        self.assertEqual(bit_index, bit_length)


if __name__ == '__main__':
    unittest.main()
