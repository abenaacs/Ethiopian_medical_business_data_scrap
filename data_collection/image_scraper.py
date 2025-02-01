import requests
import os
from .logger import setup_logger
from .config import IMAGE_DIR

setup_logger()


class ImageScraper:
    def __init__(self, base_url, output_dir):
        self.base_url = base_url
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def download_images(self, urls):
        try:
            for i, url in enumerate(urls):
                response = requests.get(url)
                if response.status_code == 200:
                    file_path = os.path.join(self.output_dir, f"image_{i}.jpg")
                    with open(file_path, "wb") as f:
                        f.write(response.content)
                    logging.info(f"Downloaded image {i} from {url}")
        except Exception as e:
            logging.error(f"Error downloading images: {e}")


if __name__ == "__main__":
    scraper = ImageScraper("https://t.me/lobelia4cosmetics", IMAGE_DIR)
    image_urls = ["https://abena.com/image1.jpg", "https://example.com/image2.jpg"]
    scraper.download_images(image_urls)
