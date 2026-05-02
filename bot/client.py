import os
from binance.client import Client
from dotenv import load_dotenv
from bot.logging_config import logger

class BinanceClient:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("BINANCE_API_KEY")
        self.api_secret = os.getenv("BINANCE_API_SECRET")
        
        if not self.api_key or not self.api_secret:
            logger.error("API Key or Secret missing in .env file.")
            raise ValueError("API Key and Secret must be provided in the .env file.")
        
        try:
            # Initialize with testnet=True for Binance Futures Testnet
            self.client = Client(self.api_key, self.api_secret, testnet=True)
            logger.info("Binance Client initialized on Testnet.")
        except Exception as e:
            logger.error(f"Failed to initialize Binance Client: {str(e)}")
            raise

    def get_client(self):
        return self.client
