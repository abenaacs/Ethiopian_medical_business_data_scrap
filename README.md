# Ethiopian Medical Business Data Pipeline

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [Directory Structure](#directory-structure)
5. [Setup Instructions](#setup-instructions)
6. [Using the Makefile](#using-the-makefile)
7. [Project Workflow](#project-workflow)
8. [Contributing](#contributing)
9. [License](#license)

---

## Overview

This project aims to build a robust data pipeline for Ethiopian medical businesses by scraping relevant data from Telegram channels, cleaning it, transforming it into a structured format, and preparing it for further analysis in a data warehouse.

The pipeline includes:

- **Data Scraping**: Extracting text-based data and images from public Telegram channels.
- **Data Cleaning**: Ensuring high-quality data by removing duplicates and inconsistencies.
- **DBT Transformations**: Using DBT (Data Build Tool) to transform cleaned data into a structured format suitable for a data warehouse.

---

## Features

- **Telegram Scraper**: Collects text-based data and images from public Telegram channels.
- **Data Cleaner**: Ensures high-quality data by removing duplicates and inconsistencies.
- **DBT Integration**: Automates SQL-based transformations for scalable data processing.
- **Makefile Automation**: Simplifies execution of the entire pipeline with predefined targets.

---

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.9+
- `pip` (Python package manager)
- `make` (for executing the Makefile)
- `dbt` (Data Build Tool)
- `telethon` (for interacting with the Telegram API)
- `pandas` (for data manipulation)
- `SQLAlchemy` (for database interactions)

You can install the required Python dependencies using:

```bash
pip install -r requirements.txt
```

Additionally, you will need:

- A Telegram API key (`API_ID` and `API_HASH`) to access the Telegram API.
- A configured DBT project for data transformations.

---

## Directory Structure

```
project/
├── .vscode/
│   └── settings.json
├── .github/
│   └── workflows/
│       └── unittests.yml
├── .gitignore
├── requirements.txt
├── README.md
├── Makefile
├── data/
│   ├── raw_data.json
│   └── images/
├── notebooks/
│   ├── data_scraping.ipynb
│   └── data_cleaning.ipynb
├── data_collection/
│   ├── __init__.py
│   ├── telegram_scraper.py
│   ├── image_scraper.py
│   ├── logger.py
│   └── config.py
├── data_cleaning/
│   ├── __init__.py
│   ├── cleaner.py
│   ├── dbt_project/
│   │   ├── models/
│   │   │   └── cleaned_data.sql
│   │   └── dbt_project.yml
│   └── config.py
```

---

## Setup Instructions

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/abenaacs/Ethiopian_medical_business_data_scrap.git
   cd Ethiopian_medical_business_data_scrap
   ```

2. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Telegram API**:

   - Obtain your `API_ID` and `API_HASH` from [Telegram's App Configuration](https://my.telegram.org/auth).
   - Update the `data_collection/config.py` file with your credentials:
     ```python
     TELEGRAM_API_ID = 'your_api_id'
     TELEGRAM_API_HASH = 'your_api_hash'
     ```

4. **Set Up DBT**:
   - Install DBT if not already installed:
     ```bash
     pip install dbt-core dbt-snowflake  # Replace `snowflake` with your target adapter
     ```
   - Configure your DBT project in `data_cleaning/dbt_project/`.

---

## Using the Makefile

The project includes a `Makefile` to automate the execution of various tasks. Below are the available commands:

- **Scrape Data**:

  ```bash
  make scrape
  ```

  This will run the Telegram scraper and save the raw data to `data/raw_data.json`.

- **Clean Data**:

  ```bash
  make clean
  ```

  This will clean the raw data and save the cleaned data to `data/cleaned_data.json`.

- **Run DBT Transformations**:

  ```bash
  make dbt
  ```

  This will execute the DBT transformations defined in `data_cleaning/dbt_project/`.

- **Run All Steps**:

  ```bash
  make run
  ```

  This will execute the entire pipeline (`scrape`, `clean`, `dbt`) in one command.

- **Clean Up Generated Files**:

  ```bash
  make clean-all
  ```

  This will delete all generated files and reset the project.

- **View Available Commands**:
  ```bash
  make help
  ```

---

## Project Workflow

1. **Scrape Data**:

   - Use the `telegram_scraper.py` script to extract messages and images from Telegram channels.
   - Store the raw data in `data/raw_data.json`.

2. **Clean Data**:

   - Use the `cleaner.py` script to remove duplicates, handle missing values, and standardize formats.
   - Save the cleaned data in `data/cleaned_data.json`.

3. **Transform Data**:

   - Use DBT to apply SQL-based transformations to the cleaned data.
   - Define transformation logic in `data_cleaning/dbt_project/models/`.

4. **Load Data**:
   - Load the transformed data into a data warehouse for further analysis.

---

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. To get started:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/new-feature`.
3. Make your changes and commit them: `git commit -m "Add new feature"`.
4. Push to the branch: `git push origin feature/new-feature`.
5. Submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

For questions or feedback, please contact me at [abenezernigussiecs@gmail.com](mailto:abenezernigussiecs@gmail.com).

---

Thank you for using this project! I hope it helps you gain valuable insights into Ethiopian medical businesses.

```

```
