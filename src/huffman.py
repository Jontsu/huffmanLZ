from collections import Counter  # pragma: no cover
import heapq  # pragma: no cover

from src.utils import bits_to_bytes, bytes_to_bits  # pragma: no cover


class Node:
    def __init__(self, char, freq):
        """Initialise a node with character and its frequency.

        Parameters:
        - char (char or None): The character the node represents,
          as a single byte sequence, or 'None' for merged nodes.
        - freq (int): The frequency of the character in the data.
        """
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        """Override the default behavior for the less than (<)
        operator to compare nodes based on frequency. Python doesn't know
        how to order custom objects, so this helps to order the nodes."""
        return self.freq < other.freq


def build_huffman_tree(data):
    """Build and return the Huffman Tree based on data frequencies,
    using min-heap to merge nodes with the lowest frequencies first.

    Parameter:
    - data (bytes): The data to build the tree from.

    Returns:
    - Node: The root of the Huffman Tree.
    """
    freq = Counter(data)
    heap = [Node(bytes([char]), freq[char]) for char in freq]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]


def generate_huffman_codes(node, code, codes):
    """Recursively generate codes for characters by traversing the
    Huffman tree. These are variable length codes assigned to input
    characters, with shorter codes assigned to more frequent characters.

    Parameters:
    - node (Node): The current node.
    - code (str): The current Huffman code being generated.
    - codes (dict): The dictionary to store the generated codes.
    """

    # Handle special case where the Huffman tree has only one node
    # (data has only one unique character)
    if node.char and len(node.char) == 1 and not code:
        codes[node.char] = '0'
        return
    # Store the Huffman code for the given character in the dictionary
    if node.char is not None:
        codes[node.char] = code
        return

    generate_huffman_codes(node.left, code + '0', codes)
    generate_huffman_codes(node.right, code + '1', codes)


def huffman_compress(data):
    """Return the compressed data and the Huffman codes used.

    Parameter:
    - data (bytes): The data to compress.

    Returns:
    - tuple (bytes, dict): The compressed data and the Huffman codes.
    """
    root = build_huffman_tree(data)
    codes = {}
    generate_huffman_codes(root, "", codes)
    compressed_bits = ''.join(codes[bytes([byte])] for byte in data)
    no_of_padding_bits, compressed_data = bits_to_bytes(compressed_bits)
    return bytes([no_of_padding_bits]) + compressed_data, codes


def huffman_decompress(compressed_data, codes):
    """Decompress the data using the provided Huffman codes.

    Parameters:
    - compressed_data (bytes): The compressed data.
    - codes (dict): The Huffman codes to use for decompression.

    Returns:
    - bytes: The decompressed data.
    """
    no_of_padding_bits = compressed_data[0]
    compressed_bits = bytes_to_bits(no_of_padding_bits, compressed_data[1:])
    reversed_codes = {value: key for key, value in codes.items()}
    decompressed_data = bytearray()
    temp = ''

    for bit in compressed_bits:
        temp += bit

        if temp in reversed_codes:
            decompressed_data.extend(reversed_codes[temp])
            temp = ''

    return bytes(decompressed_data)
