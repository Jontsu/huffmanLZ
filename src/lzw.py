from src.utils import bits_to_bytes, bytes_to_bits  # pragma: no cover


def initialise_dictionary(algorithm_mode, size):
    """Initialise the dictionary for compression or decompression. 
    In 'compress' mode, maps byte characters to their ASCII values.
    In 'decompress' mode, maps codes to byte sequences.
    
    Parameters:
    - algorithm_mode (str): Either 'compress' or 'decompress'.
    - size (int): The desired dictionary size.
    
    Returns:
    - dict: The initialised dictionary.
    - int: The bit length for each code
    """
    bit_length = size.bit_length() - 1

    if algorithm_mode == 'compress':
        return {chr(i): i for i in range(256)}, bit_length
    
    if algorithm_mode == 'decompress':
        return {i: bytes([i]) for i in range(256)}, bit_length
    
    return None, 0
 

def add_to_dictionary(dictionary, key, value, limit):
    """Add key-value pair to dictionary if its size is less than the given limit.
    
    Parameters:
    - dictionary (dict): The dictionary to which the key-value pair will be added.
    - key (int): The key to be added.
    - value (bytes or str): The value to be associated with the key.
    - limit (int): The maximum size of the dictionary.
    
    Returns:
    None.
    """
    if len(dictionary) < limit:
        dictionary[key] = value


def lzw_compress(data, dictionary_size=65536):
    """Compress data using the LZW algorithm.

    Parameter:
    - data (bytes): The data to be compressed.
    - dictionary_size (int): The desired dictionary size.

    Returns:
    - bytes: Compressed data as bytes.
    """
    dictionary, bit_length = initialise_dictionary('compress', dictionary_size)
    current_string = ''
    compressed_data = []

    for byte in data:
        byte_char = chr(byte)
        combined_string = current_string + byte_char

        if combined_string in dictionary:
            current_string = combined_string
        else:
            compressed_data.append(dictionary[current_string])
            add_to_dictionary(dictionary, combined_string, len(dictionary), dictionary_size)
            current_string = byte_char

    if current_string:
        compressed_data.append(dictionary[current_string])

    compressed_bits = ''.join(f'{code:0{bit_length}b}' for code in compressed_data)
    no_of_padding_bits, compressed_bytes = bits_to_bytes(compressed_bits)
    return bytes([no_of_padding_bits]) + compressed_bytes


def lzw_decompress(compressed_data, dictionary_size=65536):
    """Decompress LZW encoded data back to its uncompressed form.

    Parameter:
    - compressed_data (bytes): Compressed data as bytes.
    - dictionary_size (int): The desired dictionary size.    

    Returns:
    - bytes: The decompressed data.
    """
    no_of_padding_bits = compressed_data[0]
    compressed_bits = bytes_to_bits(no_of_padding_bits, compressed_data[1:])
    dictionary, bit_length = initialise_dictionary('decompress', dictionary_size)
    decompressed_data = bytearray()
    bit_index = 0

    previous_code, bit_index = get_next_code(compressed_bits, bit_index, bit_length)
    decompressed_data.extend(dictionary[previous_code])
    previous_string = dictionary[previous_code]

    while bit_index < len(compressed_bits):
        code, bit_index = get_next_code(compressed_bits, bit_index, bit_length)

        if code in dictionary:
            current_string = dictionary[code]

        if code == len(dictionary):
            current_string = previous_string + previous_string[:1]

        decompressed_data.extend(current_string)
        add_to_dictionary(dictionary, len(dictionary), previous_string + current_string[:1], dictionary_size)
        previous_string = current_string

    return bytes(decompressed_data)


def get_next_code(compressed_bits, bit_index, bit_length):
    """Retrieve the next code from the compressed bit string.

    Parameters:
    - compressed_bits (str): Compressed data as a string of bits.
    - bit_index (int): The index to start extracting the code from.
    - bit_length (int): The length of each code in bits.

    Returns:
    - tuple: The next code and the new bit index.
    """
    code = int(compressed_bits[bit_index:bit_index+bit_length], 2)
    bit_index += bit_length
    return code, bit_index
