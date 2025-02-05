import unittest
import pandas as pd
from data_cleaning.cleaner import DataCleaner


class TestDataCleaner(unittest.TestCase):
    def setUp(self):
        # Create a sample raw data file
        self.raw_data_file = "tests/raw_data_test.json"
        self.cleaned_data_file = "tests/cleaned_data_test.json"
        sample_data = [
            {"id": 1, "text": "Sample text"},
            {"id": 2, "text": None},
            {"id": 3, "text": "   Extra spaces   "},
        ]
        with open(self.raw_data_file, "w") as f:
            json.dump(sample_data, f, indent=4)

    def test_clean_data(self):
        cleaner = DataCleaner(self.raw_data_file, self.cleaned_data_file)
        cleaner.run()

        # Load cleaned data
        with open(self.cleaned_data_file, "r") as f:
            cleaned_data = json.load(f)

        # Assertions
        self.assertEqual(len(cleaned_data), 2)  # One record removed due to missing text
        self.assertEqual(cleaned_data[0]["text"], "Sample text")
        self.assertEqual(cleaned_data[1]["text"], "Extra spaces")

    def tearDown(self):
        # Clean up test files
        import os

        if os.path.exists(self.raw_data_file):
            os.remove(self.raw_data_file)
        if os.path.exists(self.cleaned_data_file):
            os.remove(self.cleaned_data_file)


if __name__ == "__main__":
    unittest.main()
