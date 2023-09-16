import random
import string

from src.huffman import huffman_compress
from src.lzw import lzw_compress


def generate_random_text(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))


def generate_structured_text(length):
    return 'ABCD' * (length // 4)


def calculate_efficiency_as_percentage(original_size, compressed_size):
    return (1 - compressed_size / original_size) * 100


def compute_compressed_data_and_size(data, algorithm):
    if algorithm == 'huffman':
        compressed_data, codes = huffman_compress(data)
        # Calculate the total bits by summing up the bit-lengths of Huffman codes for each character in data
        size_in_bits = sum(len(codes[char]) for char in data)

    elif algorithm == 'lzw':
        compressed_data = lzw_compress(data)
        # Find the largest integer code in the compressed data
        max_code = max(compressed_data)
        # Calculate the total bits by multiplying the number of codes by the bit-length of the largest code
        size_in_bits = len(compressed_data) * max_code.bit_length()

    else:
        raise ValueError("Unknown compression algorithm")
    
    return compressed_data, size_in_bits


def main():
    lengths = [10000, 50000, 100000]
    for data_type, generator in [('Random', generate_random_text), ('Structured', generate_structured_text)]:
        
        for length in lengths:
            data = generator(length)
            original_size = len(data.encode('utf-8')) * 8
            
            for algorithm in ['huffman', 'lzw']:
                _, compressed_size = compute_compressed_data_and_size(data, algorithm)
                efficiency = calculate_efficiency_as_percentage(original_size, compressed_size)
                # Display the compression efficiency for the given data type and algorithm
                print(f"{data_type} Data (Length: {length}) | {algorithm.capitalize()} Compression Efficiency: {efficiency:.2f}%")


if __name__ == "__main__":
    main()
