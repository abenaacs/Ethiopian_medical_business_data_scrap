from telethon import TelegramClient, events
import asyncio
import json
from logger import setup_logger
from config import TELEGRAM_API_ID, TELEGRAM_API_HASH, CHANNELS_TO_SCRAPE, RAW_DATA_FILE

setup_logger()


class TelegramScraper:
    def __init__(self, api_id, api_hash):
        self.api_id = api_id
        self.api_hash = api_hash
        self.client = TelegramClient("session_name", self.api_id, self.api_hash)

    async def ensure_authorization(self):
        """Ensure the user is authorized."""
        if not await self.client.is_user_authorized():
            print("User is not authorized. Please provide your phone number.")
            phone_number = input("Enter your phone number (with country code): ")
            await self.client.send_code_request(phone_number)
            try:
                await self.client.sign_in(
                    phone_number, input("Enter the code you received: ")
                )
            except Exception as e:
                await self.client.sign_in(password=input("Enter your 2FA password: "))
        logging.info("Logged in successfully.")

    async def scrape_channels(self, channels, output_file):
        try:
            all_messages = []
            async with self.client:
                # Ensure the user is logged in
                await self.ensure_authorization()

                for channel in channels:
                    try:
                        # Check if the channel exists
                        entity = await self.client.get_entity(channel)
                        logging.info(f"Found channel: {entity.title} (ID: {entity.id})")

                        # Fetch messages
                        messages = []
                        logging.info(f"Scraping messages from channel: {channel}")
                        async for message in self.client.iter_messages(
                            entity, limit=100
                        ):  # Limit to 100 messages for testing
                            if message.text:
                                messages.append(
                                    {"id": message.id, "text": message.text}
                                )
                                logging.debug(
                                    f"Message ID: {message.id}, Text: {message.text[:50]}..."
                                )
                            else:
                                logging.debug(
                                    f"Skipped message ID {message.id} (no text)"
                                )
                        all_messages.extend(messages)
                        logging.info(f"Scraped {len(messages)} messages from {channel}")
                    except Exception as e:
                        logging.error(f"Failed to scrape channel {channel}: {e}")

            # Save scraped data to file
            output_dir = os.path.dirname(output_file)
            os.makedirs(
                output_dir, exist_ok=True
            )  # Create the directory if it doesn't exist
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(all_messages, f, ensure_ascii=False, indent=4)
            logging.info(f"All data saved to {output_file}")
        except Exception as e:
            logging.error(f"Error scraping channels: {e}")


if __name__ == "__main__":
    scraper = TelegramScraper(TELEGRAM_API_ID, TELEGRAM_API_HASH)
    asyncio.run(scraper.scrape_channels(CHANNELS_TO_SCRAPE, RAW_DATA_FILE))
