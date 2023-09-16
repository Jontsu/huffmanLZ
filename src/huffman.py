from collections import Counter
import heapq


class Node:
    def __init__(self, char, freq):
        """Initialise a node with character and its frequency.
        
        Parameters:
        - char (str): The character the node represents.
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
    """Build and return the Huffman Tree based on data frequencies.
    
    Parameter:
    - data (str): The data to build the tree from.
    
    Returns:
    - Node: The root of the Huffman Tree.
    """
    freq = Counter(data)
    heap = [Node(char, freq) for char, freq in freq.items()]
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
    """Recursively generate Huffman codes for characters.
    
    Parameters:
    - node (Node): The current node.
    - code (str): The current Huffman code being generated.
    - codes (dict): The dictionary to store the generated codes.
    """

    # Check for non-existent branch
    if node is None:
        return
    # Handle special case where the Huffman tree has only one node (data has only one unique character)
    if node.char is not None and not code:
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
    - data (str): The data to compress.
    
    Returns:
    - tuple (str, dict): The compressed data and the Huffman codes.
    """
    root = build_huffman_tree(data)
    codes = {}
    generate_huffman_codes(root, "", codes)
    return ''.join([codes[char] for char in data]), codes


def huffman_decompress(compressed_data, codes):
    """Decompress the data using the provided Huffman codes.
    
    Parameters:
    - compressed_data (str): The compressed data.
    - codes (dict): The Huffman codes to use for decompression.
    
    Returns:
    - str: The decompressed data.
    """
    reversed_codes = {value: key for key, value in codes.items()}
    decompressed_data = ''
    temp = ''

    for bit in compressed_data:
        temp += bit

        if temp in reversed_codes:
            decompressed_data += reversed_codes[temp]
            temp = ''
    return decompressed_data
