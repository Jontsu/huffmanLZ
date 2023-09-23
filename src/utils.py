def calculate_efficiency(original_data, compressed_data):
    """Calculate the compression efficiency.

    Parameters:
    original_data (str): The data to be compressed.
    compressed_data (str): The data after compression.

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
