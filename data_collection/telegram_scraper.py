"""
Telegram scraper module to extract data from Telegram channels.
"""

from telethon import TelegramClient
import asyncio
import json
import os
from .logger import setup_logger
from .config import (
    TELEGRAM_API_ID,
    TELEGRAM_API_HASH,
    CHANNELS_TO_SCRAPE,
    RAW_DATA_FILE,
)

setup_logger()


class TelegramScraper:
    """
    A class to scrape data from Telegram channels using the Telethon library.
    """

    def __init__(self, api_id, api_hash):
        """
        Initialize the TelegramScraper with API credentials.
        """
        self.api_id = api_id
        self.api_hash = api_hash
        self.client = TelegramClient("session_name", self.api_id, self.api_hash)

    async def scrape_channel(self, channel_url):
        """
        Scrape messages from a single Telegram channel.
        :param channel_url: URL of the Telegram channel to scrape.
        :return: List of scraped messages.
        """
        messages = []
        try:
            async with self.client:
                async for message in self.client.iter_messages(channel_url):
                    if message.text:
                        messages.append({"id": message.id, "text": message.text})
            logging.info(f"Scraped {len(messages)} messages from {channel_url}")
        except Exception as e:
            logging.error(f"Error scraping channel {channel_url}: {e}")
        return messages

    async def scrape_channels(self, channels, output_file):
        """
        Scrape messages from multiple Telegram channels and save them to a file.
        :param channels: List of Telegram channel URLs to scrape.
        :param output_file: Path to save the scraped data.
        """
        all_messages = []
        for channel in channels:
            messages = await self.scrape_channel(channel)
            all_messages.extend(messages)

        # Ensure the directory exists before saving the file
        os.makedirs(os.path.dirname(output_file), exist_ok=True)

        # Save scraped data to a JSON file
        with open(output_file, "w") as f:
            json.dump(all_messages, f, indent=4)
        logging.info(f"All data saved to {output_file}")


if __name__ == "__main__":
    scraper = TelegramScraper(TELEGRAM_API_ID, TELEGRAM_API_HASH)
    asyncio.run(scraper.scrape_channels(CHANNELS_TO_SCRAPE, RAW_DATA_FILE))
