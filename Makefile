# Define variables
RAW_DATA_FILE = data/raw_data.json
CLEANED_DATA_FILE = data/cleaned_data.json
DBT_PROJECT_PATH = data_cleaning/dbt_project/

# Default target
all: scrape clean dbt

#install dependecies
install:
	pip install -r requirements.txt
# Target to scrape data from Telegram
scrape:
	@echo "Scraping data from Telegram..."
	python data_collection/telegram_scraper.py
	@echo "Scraping completed. Data saved to $(RAW_DATA_FILE)"

# Target to clean the scraped data
clean:
	@echo "Cleaning the scraped data..."
	python data_cleaning/cleaner.py
	@echo "Data cleaning completed. Cleaned data saved to $(CLEANED_DATA_FILE)"

# Target to run DBT transformations
dbt:
	@echo "Running DBT transformations..."
	cd $(DBT_PROJECT_PATH) && dbt run
	@echo "DBT transformations completed."

# Target to run all steps in sequence
run: scrape clean dbt
	@echo "All steps completed successfully."

# Target to clean up generated files
clean-all:
	@echo "Cleaning up generated files..."
	rm -f $(RAW_DATA_FILE)
	rm -f $(CLEANED_DATA_FILE)
	rm -rf data/images/
	@echo "Cleanup completed."

# Help target to display available commands
help:
	@echo "Available Makefile targets:"
	@echo "  make scrape       - Scrape data from Telegram"
	@echo "  make clean        - Clean the scraped data"
	@echo "  make dbt          - Run DBT transformations"
	@echo "  make run          - Run all steps (scrape, clean, dbt)"
	@echo "  make clean-all    - Clean up generated files"
	@echo "  make help         - Display this help message"

.PHONY: all scrape clean dbt run clean-all help