"""
Data cleaning module to process raw data into a structured format.
"""

import pandas as pd
import json
import os
import logging
from .config import RAW_DATA_FILE, CLEANED_DATA_FILE

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class DataCleaner:
    """
    A class to clean and transform raw data into a structured format.
    """

    def __init__(self, input_file, output_file):
        """
        Initialize the DataCleaner with input and output file paths.
        """
        self.input_file = input_file
        self.output_file = output_file

    def load_data(self):
        """
        Load raw data from the input file.
        :return: Pandas DataFrame containing the raw data.
        """
        try:
            with open(self.input_file, "r") as f:
                data = json.load(f)
            logging.info(f"Loaded {len(data)} records from {self.input_file}")
            return pd.DataFrame(data)
        except Exception as e:
            logging.error(f"Error loading data: {e}")
            return pd.DataFrame()

    def clean_data(self, df):
        """
        Clean the raw data by removing duplicates, handling missing values, and standardizing formats.
        :param df: Pandas DataFrame containing raw data.
        :return: Cleaned Pandas DataFrame.
        """
        try:
            df.drop_duplicates(inplace=True)
            df.fillna(value={"text": ""}, inplace=True)
            df["text"] = df["text"].str.strip()
            logging.info("Data cleaning completed.")
            return df
        except Exception as e:
            logging.error(f"Error cleaning data: {e}")
            return pd.DataFrame()

    def save_data(self, df):
        """
        Save cleaned data to the output file.
        :param df: Pandas DataFrame containing cleaned data.
        """
        try:
            os.makedirs(os.path.dirname(self.output_file), exist_ok=True)
            cleaned_data = df.to_dict(orient="records")
            with open(self.output_file, "w") as f:
                json.dump(cleaned_data, f, indent=4)
            logging.info(f"Cleaned data saved to {self.output_file}")
        except Exception as e:
            logging.error(f"Error saving cleaned data: {e}")

    def run(self):
        """
        Run the data cleaning pipeline.
        """
        df = self.load_data()
        if not df.empty:
            cleaned_df = self.clean_data(df)
            self.save_data(cleaned_df)


if __name__ == "__main__":
    cleaner = DataCleaner(RAW_DATA_FILE, CLEANED_DATA_FILE)
    cleaner.run()
