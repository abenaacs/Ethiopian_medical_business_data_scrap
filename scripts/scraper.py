from data_collection.scraper import TelegramScraper

if __name__ == "__main__":
    scraper = TelegramScraper()
    asyncio.run(scraper.scrape_channels(CHANNELS_TO_SCRAPE, RAW_DATA_FILE))
