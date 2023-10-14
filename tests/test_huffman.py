import unittest

from src.huffman import huffman_compress, huffman_decompress, build_huffman_tree, generate_huffman_codes


class TestHuffmanAlgorithm(unittest.TestCase):
    """Unit tests for Huffman compresion algorithm functions."""

    def test_build_huffman_tree(self):
        data = b"ABBCCC"
        root = build_huffman_tree(data)
        self.assertIsNotNone(root)

    def test_generate_huffman_codes(self):
        data = b"ABBCCC"
        root = build_huffman_tree(data)
        codes = {}
        generate_huffman_codes(root, "", codes)
        self.assertTrue(b"A" in codes)
        self.assertTrue(b"B" in codes)
        self.assertTrue(b"C" in codes)


if __name__ == '__main__':
    unittest.main()
