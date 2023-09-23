import unittest

from src.utils import calculate_efficiency


class TestUtilityFunctions(unittest.TestCase):
    """Unit tests for utility functions."""

    def test_efficiency_calculation_with_half_size_data(self):
        original_data = "AAAAAA"
        compressed_data = "AAA"

        expected_efficiency = 50.0
        calculated_efficiency = (
            calculate_efficiency(original_data, compressed_data)
        )
        self.assertEqual(calculated_efficiency, expected_efficiency,
                         "Efficiency calculation with half size data failed")

    def test_efficiency_calculation_with_empty_string(self):
        original_data = ""
        compressed_data = ""

        expected_efficiency = 0.0
        calculated_efficiency = (
            calculate_efficiency(original_data, compressed_data)
        )
        self.assertEqual(calculated_efficiency, expected_efficiency,
                         "Efficiency calculation with empty strings failed")

    def test_efficiency_calculation_with_same_size_data(self):
        original_data = "ABCDE"
        compressed_data = "ABCDE"

        expected_efficiency = 0.0
        calculated_efficiency = (
            calculate_efficiency(original_data, compressed_data)
        )
        self.assertEqual(calculated_efficiency, expected_efficiency,
                         "Efficiency calculation with same size data failed")


if __name__ == "__main__":
    unittest.main()
