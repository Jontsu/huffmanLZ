import unittest

from src.lzw import get_next_code, initialise_dictionary, add_to_size_limited_dictionary


class TestLZWAlgorithm(unittest.TestCase):
    """Unit tests for LZW compresion algorithm functions."""

    def test_get_next_code(self):
        compressed_bits = "01010101010101010101"
        code, bit_index = get_next_code(compressed_bits, 0)
        self.assertEqual(code, 1365)
        self.assertEqual(bit_index, 12)

    def test_initialise_dictionary_compress(self):
        dictionary = initialise_dictionary('compress')
        self.assertEqual(dictionary['A'], 65)

    def test_initialise_dictionary_decompress(self):
        dictionary = initialise_dictionary('decompress')
        self.assertEqual(dictionary[65], bytes([65]))

    def test_add_to_size_limited_dictionary_within_limit(self):
        dictionary = {1: 'A', 2: 'B'}
        add_to_size_limited_dictionary(dictionary, 3, 'C', 3)
        self.assertTrue(3 in dictionary)

    def test_add_to_size_limited_dictionary_beyond_limit(self):
        dictionary = {1: 'A', 2: 'B', 3: 'C'}
        add_to_size_limited_dictionary(dictionary, 4, 'D', 3)
        self.assertFalse(4 in dictionary)

if __name__ == '__main__':
    unittest.main()
