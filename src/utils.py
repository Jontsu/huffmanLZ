def calculate_efficiency(original_data, compressed_data):
    """Calculate the compression efficiency.

    Parameters:
    original_data: The data to be compressed.
    compressed_data: The data after compression.

    Returns:
    float: The compression efficiency as a percentage.
    """
    original_size = len(original_data)
    compressed_size = len(compressed_data)

    # Handle case where original data is empty
    if original_size == 0:
        return 0.0

    efficiency = ((1 - compressed_size / original_size) * 100)
    return efficiency


def bits_to_bytes(bit_string):
    """Convert string of bits to bytearray."""
    # Ensure bit string length as multiple of 8 by padding with zeros
    # for byte conversion
    padded_bit_string = (
        bit_string.ljust(len(bit_string) + (8 - len(bit_string) % 8) % 8, '0')
    )
    # Convert 8 bit segments to bytes and collect them into bytearray
    byte_array = (
        bytearray(
            int(padded_bit_string[i:i + 8], 2)
            for i in range(0, len(padded_bit_string), 8)
        )
    )
    return byte_array


def bytes_to_bits(byte_array):
    """Convert bytearray to string of bits and concatenate them."""
    bit_string = ''.join(f'{byte:08b}' for byte in byte_array)
    return bit_string
