from src.utils import bits_to_bytes, bytes_to_bits


def get_next_code(compressed_bits, bit_index):
    """Retrieve the next code from the compressed bit string."""
    bit_length = 12
    code = int(compressed_bits[bit_index:bit_index+bit_length], 2)
    bit_index += bit_length
    return code, bit_index

def initialise_dictionary(algorithm_mode):
    """Initialise the dictionary f....
    
    Parameters:
    - ...: Either 'compress' or 'decompress'.
    
    Returns:
    dict: The initialised dictionary.
    """
    if algorithm_mode == 'compress':
        return {chr(i): i for i in range(256)}
    if algorithm_mode == 'decompress':
        return {i: bytes([i]) for i in range(256)}
    return

def add_to_size_limited_dictionary(dictionary, key, value, limit=2**12 - 1):
    """Add key-value pair to dictionary if its size is less than the given limit.
    
    Parameters:
    - dictionary (dict): The dictionary to which the key-value pair will be added.
    - key (int): The key to be added.
    - value (bytes or str): The value to be associated with the key.
    - limit (int, optional): The maximum size of the dictionary. Defaults to 2**12 - 1.
    
    Returns:
    None.
    """
    if len(dictionary) < limit:
        dictionary[key] = value

def lzw_compress(data):
    """Compress data using the LZW algorithm.

    Parameter:
    - data (bytes): The data to be compressed.

    Returns:
    - bytes: Compressed data as bytes.
    """
    # Initialise dictionary and map single characters to their ASCII values
    dictionary = initialise_dictionary('compress')
    current_string = ''
    compressed_data = []

    for byte in data:
        byte_char = chr(byte)
        combined_string = current_string + byte_char

        if combined_string in dictionary:
            current_string = combined_string
        else:
            compressed_data.append(dictionary[current_string])
            add_to_size_limited_dictionary(dictionary, combined_string, len(dictionary))
            current_string = byte_char

    if current_string:
        compressed_data.append(dictionary[current_string])

    # Convert each LZW code into a fixed width 12 bit binary representation
    compressed_bits = ''.join(f'{code:012b}' for code in compressed_data)
    no_of_padding_bits, compressed_bytes = bits_to_bytes(compressed_bits)
    return bytes([no_of_padding_bits]) + compressed_bytes

def lzw_decompress(compressed_data):
    """Decompress LZW encoded data back to its original form.

    Parameter:
    - compressed_data (bytes): Compressed data as bytes.

    Returns:
    - bytes: The decompressed data.
    """
    no_of_padding_bits = compressed_data[0]
    compressed_bits = bytes_to_bits(no_of_padding_bits, compressed_data[1:])
    # Initialise dictionary and map codes to single-byte sequences
    dictionary = initialise_dictionary('decompress')
    decompressed_data = bytearray()
    bit_index = 0

    previous_code, bit_index = get_next_code(compressed_bits, bit_index)
    decompressed_data.extend(dictionary[previous_code])
    previous_string = dictionary[previous_code]

    while bit_index < len(compressed_bits):
        code, bit_index = get_next_code(compressed_bits, bit_index)

        if code in dictionary:
            current_string = dictionary[code]

        if code == len(dictionary):
            current_string = previous_string + previous_string[:1]

        decompressed_data.extend(current_string)
        add_to_size_limited_dictionary(dictionary, len(dictionary), previous_string + current_string[:1])
        previous_string = current_string

    return bytes(decompressed_data)
