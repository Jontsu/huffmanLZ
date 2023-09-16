from io import StringIO


def lzw_compress(data):
    """Compress data using the LZW algorithm.
    
    Parameter:
    - data (str): The data to be compressed.
    
    Returns:
    - list[int]: List of integer codes representing the compressed data.
    """
    dictionary = {chr(i): i for i in range(256)}
    current_string = ""
    compressed_data = []

    for char in data:
        combined_string = current_string + char

        if combined_string in dictionary:
            current_string = combined_string
        else:
            compressed_data.append(dictionary[current_string])
            dictionary[combined_string] = len(dictionary)
            current_string = char

    if current_string:
        compressed_data.append(dictionary[current_string])

    return compressed_data


def lzw_decompress(compressed_data):
    """Decompress LZW encoded data back to its original form.
    
    Parameter:
    - compressed_data list[int]: List of integer codes representing the compressed data.
    
    Returns:
    - str: The decompressed data.
    """
    dictionary = {i: chr(i) for i in range(256)}
    current_string = chr(compressed_data[0])
    decompressed_data = StringIO()
    decompressed_data.write(current_string)

    for code in compressed_data[1:]:

        if code in dictionary:
            entry = dictionary[code]
        elif code == len(dictionary):
            entry = current_string + current_string[0]
        else:
            raise ValueError(f'Corrupted compressed code: {code}')

        decompressed_data.write(entry)
        dictionary[len(dictionary)] = current_string + entry[0]
        current_string = entry

    return decompressed_data.getvalue()
