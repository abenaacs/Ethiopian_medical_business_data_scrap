import logging
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(message)s")

# Define project structure
PROJECT_STRUCTURE = [
    ".vscode/settings.json",
    ".github/workflows/ci-cd.yml",
    ".gitignore",
    "requirements.txt",
    "README.md",
    "Makefile",
    "data/raw_data.json",
    "data/images/",
    "notebooks/data_scraping.ipynb",
    "notebooks/data_cleaning.ipynb",
    "data_collection/__init__.py",
    "data_collection/logger.py",
    "data_collection/config.py",
    "data_cleaning/__init__.py",
    "data_cleaning/cleaner.py",
    "data_cleaning/dbt_project/models/cleaned_data.sql",
    "data_cleaning/dbt_project/dbt_project.yml",
    "data_cleaning/config.py",
    "object_detection/__init__.py",
    "object_detection/yolov5/requirements.txt",
    "api/__init__.py",
    "api/database.py",
    "api/models.py",
    "api/schemas.py",
    "api/crud.py",
    "scripts/scraper.py",
    "scripts/cleaner.py",
    "scripts/detector.py",
    "scripts/run_api.py",
    "tests/__init__.py",
    "tests/test_scraper.py",
    "tests/test_cleaner.py",
    "tests/test_api.py",
]


def create_project_structure(projects):
    for entry in projects:
        path = Path(entry)

        if entry.endswith("/"):
            # Create directory structure
            directory = path.parent / path.name
            directory.mkdir(parents=True, exist_ok=True)
            logging.info(f"Created directory: {directory}")
        else:
            # Create parent directories if needed
            path.parent.mkdir(parents=True, exist_ok=True)

            # Create file if it doesn't exist or is empty
            if not path.exists() or path.stat().st_size == 0:
                path.touch()
                logging.info(f"Created file: {path}")
            else:
                logging.info(f"Skipped existing file: {path}")


if __name__ == "__main__":
    create_project_structure(PROJECT_STRUCTURE)
    logging.info("Project structure initialization complete!")
