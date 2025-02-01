import pandas as pd
import json
import logging
from .config import RAW_DATA_FILE, CLEANED_DATA_FILE

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DataCleaner:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
    
    def clean_data(self):
        try:
            with open(self.input_file, 'r') as f:
                data = json.load(f)
            
            df = pd.DataFrame(data)
            df.drop_duplicates(inplace=True)
            df.fillna(value={'text': ''}, inplace=True)
            df['text'] = df['text'].str.strip()
            
            cleaned_data = df.to_dict(orient='records')
            with open(self.output_file, 'w') as f:
                json.dump(cleaned_data, f, indent=4)
            
            logging.info(f"Data cleaned and saved to {self.output_file}")
        except Exception as e:
            logging.error(f"Error cleaning data: {e}")

if __name__ == "__main__":
    cleaner = DataCleaner(RAW_DATA_FILE, CLEANED_DATA_FILE)
    cleaner.clean_data()