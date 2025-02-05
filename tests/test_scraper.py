import unittest
from unittest.mock import patch, AsyncMock
from data_collection.scraper import TelegramScraper


class TestTelegramScraper(unittest.TestCase):
    @patch("telethon.TelegramClient")
    def test_scrape_channel(self, mock_client):
        mock_client.return_value.__aenter__.return_value.iter_messages = AsyncMock(
            return_value=[{"id": 1, "text": "Test message"}]
        )
        scraper = TelegramScraper(api_id="12345", api_hash="abcdef")
        result = scraper.scrape_channel("https://t.me/test_channel")
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["text"], "Test message")


if __name__ == "__main__":
    unittest.main()
