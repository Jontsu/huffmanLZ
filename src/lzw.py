from src.utils import bits_to_bytes, bytes_to_bits


def lzw_compress(data):
    """Compress data using the LZW algorithm.

    Parameter:
    - data (bytes): The data to be compressed.

    Returns:
    - list[int]: List of integer codes representing the compressed data.
    """
    # Initialise dictionary and map single characters to their ASCII values
    dictionary = {chr(i): i for i in range(256)}
    current_string = ''
    compressed_data = []

    for byte in data:
        byte_char = chr(byte)
        combined_string = current_string + byte_char

        if combined_string in dictionary:
            current_string = combined_string
        else:
            compressed_data.append(dictionary[current_string])

            # Limit dictionary size to ensure dictionary does not grow
            # indefinitely causing performance and integrity issues
            if len(dictionary) < 2**12 - 1:
                dictionary[combined_string] = len(dictionary)

            current_string = byte_char

    if current_string:
        compressed_data.append(dictionary[current_string])

    # Use 12 bits for each code
    compressed_bits = (
        ''.join([format(code, '012b') for code in compressed_data])
    )
    compressed_bytes = bits_to_bytes(compressed_bits)
    return compressed_bytes


def lzw_decompress(compressed_data):
    """Decompress LZW encoded data back to its original form.

    Parameter:
    - compressed_data list[int]: List of integer codes representing the
      compressed data.

    Returns:
    - str: The decompressed data.
    """
    compressed_bits = bytes_to_bits(compressed_data)
    # Initialise dictionary and map codes to single-byte sequences
    dictionary = {i: bytes([i]) for i in range(256)}
    decompressed_data = bytearray()
    bit_length = 12
    bit_index = 0

    # Get the first code to initialise the algorithm for next iteration
    previous_code = int(compressed_bits[bit_index:bit_index+bit_length], 2)
    decompressed_data.extend(dictionary[previous_code])
    previous_string = dictionary[previous_code]
    bit_index += bit_length

    # Continue iteration while there are additional bits to read
    while bit_index < len(compressed_bits):
        code = int(compressed_bits[bit_index:bit_index+bit_length], 2)
        bit_index += bit_length

        if code in dictionary:
            current_string = dictionary[code]
        elif code == len(dictionary):
            current_string = previous_string + previous_string[:1]
        else:
            raise ValueError(f'Corrupted compressed code: {code}')

        # Extend decompressed data with the obtained string
        decompressed_data.extend(current_string)

        # Limit dictionary size to ensure dictionary does not grow
        # indefinitely causing performance and integrity issues
        if len(dictionary) < 2**12 - 1:
            dictionary[len(dictionary)] = previous_string + current_string[:1]

        previous_string = current_string

    return bytes(decompressed_data)
