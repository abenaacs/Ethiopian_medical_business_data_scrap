from data_cleaning.cleaner import DataCleaner
from data_cleaning.config import RAW_DATA_FILE, CLEANED_DATA_FILE

if __name__ == "__main__":
    cleaner = DataCleaner(RAW_DATA_FILE, CLEANED_DATA_FILE)
    cleaner.run()
