import unittest

from src.huffman import Node, build_huffman_tree, generate_huffman_codes, huffman_compress, huffman_decompress


class TestHuffmanAlgorithm(unittest.TestCase):
    """Unit tests for Huffman compresion algorithm functions."""

    def test_create_node(self):
        node = Node(b"A", 1)
        self.assertEqual(node.char, b"A")
        self.assertEqual(node.freq, 1)
        self.assertIsNone(node.left)
        self.assertIsNone(node.right)

    def test_build_huffman_tree(self):
        data = b"AAABBB"
        root = build_huffman_tree(data)
        self.assertIsNotNone(root)
        self.assertEqual(root.freq, 6)
        self.assertIsNotNone(root.left)
        self.assertIsNotNone(root.right)

    def test_generate_huffman_codes(self):
        data = b"AAABBB"
        root = build_huffman_tree(data)
        codes = {}
        generate_huffman_codes(root, "", codes)
        self.assertTrue(b"A" in codes)
        self.assertTrue(b"B" in codes)

    def test_generate_huffman_codes_single_char(self):
        data = b"AA"
        root = build_huffman_tree(data)
        codes = {}
        generate_huffman_codes(root, "", codes)
        self.assertEqual(codes, {b'A': '0'})

    def test_huffman_compress_decompress(self):
        data = b"ABABABABA"
        compressed_data, codes = huffman_compress(data)
        decompressed_data = huffman_decompress(compressed_data, codes)
        self.assertEqual(data, decompressed_data)

    def test_huffman_compress_decompress_single_char(self):
        data = b"A"
        compressed_data, codes = huffman_compress(data)
        decompressed_data = huffman_decompress(compressed_data, codes)
        self.assertEqual(data, decompressed_data)

    def test_huffman_compress_decompress_single_node(self):
        data = b"AAA"
        compressed_data, codes = huffman_compress(data)
        decompressed_data = huffman_decompress(compressed_data, codes)
        self.assertEqual(data, decompressed_data)

    def test_huffman_compress_decompress_complex_characters(self):
        data = b"Testing algos! 1234567890 @#$%^&*()_+[]{}|;:',.<>/?`~"
        compressed_data, codes = huffman_compress(data)
        decompressed_data = huffman_decompress(compressed_data, codes)
        self.assertEqual(data, decompressed_data)        

if __name__ == '__main__':
    unittest.main()
