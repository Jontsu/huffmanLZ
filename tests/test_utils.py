import unittest

from src.utils import calculate_efficiency, bits_to_bytes, bytes_to_bits


class TestUtilityFunctions(unittest.TestCase):
    """Unit tests for utility functions."""

    def test_efficiency_calculation_with_empty_data(self):
        original_size = 0
        compressed_size = 0

        expected_efficiency = 0.0
        calculated_efficiency = calculate_efficiency(original_size, compressed_size)
        self.assertEqual(calculated_efficiency, expected_efficiency, 
                         "Efficiency calculation with empty strings failed")

    def test_efficiency_calculation_with_same_size_data(self):
        original_size = 5
        compressed_size = 5

        expected_efficiency = 0.0
        calculated_efficiency = calculate_efficiency(original_size, compressed_size)
        self.assertEqual(calculated_efficiency, expected_efficiency, 
                         "Efficiency calculation with same size data failed")

    def test_bits_to_bytes_without_padding(self):
        bit_string = "0101010101010101"
        no_of_padding_bits, byte_array = bits_to_bytes(bit_string)
        self.assertEqual(no_of_padding_bits, 0)
        self.assertEqual(byte_array, bytearray([85, 85]))

    def test_bits_to_bytes_with_padding(self):
        bit_string = "01010101"
        no_of_padding_bits, byte_array = bits_to_bytes(bit_string)
        self.assertEqual(no_of_padding_bits, 0)
        self.assertEqual(byte_array, bytearray([85]))

    def test_bytes_to_bits_without_padding(self):
        no_of_padding_bits = 0
        byte_array = bytearray([85, 85])
        bit_string = bytes_to_bits(no_of_padding_bits, byte_array)
        self.assertEqual(bit_string, "0101010101010101")

    def test_bytes_to_bits_with_padding(self):
        no_of_padding_bits = 0
        byte_array = bytearray([85])
        bit_string = bytes_to_bits(no_of_padding_bits, byte_array)
        self.assertEqual(bit_string, "01010101")

if __name__ == "__main__":
    unittest.main()
