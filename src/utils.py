def calculate_efficiency(original_size, compressed_size):
    """Calculate the compression efficiency based on the original and
    compressed data sizes.

    Parameters:
    - original_data (int): The size of the data before compression.
    - compressed_data (int): The size of the data after compression.

    Returns:
    float: The compression efficiency as a percentage.
    """
    # Handle case where original data is empty
    if original_size == 0:
        return 0.0

    # Calculate the compression efficiency based on file size
    efficiency = ((1 - compressed_size / original_size) * 100)
    return efficiency


def bits_to_bytes(bit_string):
    """Convert string of bits to bytearray. If the bit string length is not
    a multiple of 8, pad with zeros at the beginning of the bit string
    prior to byte conversion.

    Parameters:
    - bit_string (str): String of bits to be converted.

    Returns:
    - no_of_padding_bits (int): Number padding bits added (for reversal).
    - byte_array (bytearray): Padded (if necessary) bit string as bytes.
    """
    # Calculate number of padding bits needed to make the length multiple of 8
    no_of_padding_bits = (8 - len(bit_string) % 8) % 8
    # Add required number of padding bits to the left of the bit string
    padded_bit_string = (
        bit_string.rjust(len(bit_string) + no_of_padding_bits, '0')
    )
    # Convert 8 char binary substrings to integer values and form bytearray
    byte_array = (
        bytearray(
            # Slice substrings and convert integer values with for loop
            int(padded_bit_string[i:i + 8], 2)
            for i in range(0, len(padded_bit_string), 8)
        )
    )
    return no_of_padding_bits, byte_array


def bytes_to_bits(no_of_padding_bits, byte_array):
    """Convert bytearray back to the original bit string, reversing the
    byte conversion process in bits_to_bytes.

    Parameters:
    - no_of_padding_bits (int): Number of padding bits added during conversion.
    - byte_array (bytearray): Bit string as bytes.

    Returns:
    - bit_string (str): Original bit string.
    """
    # Concatenate each converted byte to its 8 bit string binary representation
    bit_string = ''.join(f'{byte:08b}' for byte in byte_array)
    # Remove padding bits from the beginning of the concatenated bit string
    bit_string = bit_string[no_of_padding_bits:]
    return bit_string
