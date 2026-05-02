from binance.exceptions import BinanceAPIException
from bot.logging_config import logger

class OrderManager:
    def __init__(self, client):
        self.client = client

    def place_market_order(self, symbol, side, quantity):
        """Places a Market Order on Binance Futures."""
        try:
            logger.info(f"Attempting MARKET {side} order: {quantity} {symbol}")
            response = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type='MARKET',
                quantity=quantity
            )
            logger.info(f"MARKET order successful: {response.get('orderId')}")
            return response
        except BinanceAPIException as e:
            logger.error(f"Binance API Error (Market Order): {e.message}")
            raise
        except Exception as e:
            logger.error(f"Unexpected Error (Market Order): {str(e)}")
            raise

    def place_limit_order(self, symbol, side, quantity, price):
        """Places a Limit Order on Binance Futures."""
        try:
            logger.info(f"Attempting LIMIT {side} order: {quantity} {symbol} at {price}")
            response = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type='LIMIT',
                timeInForce='GTC',  # Good Till Cancelled
                quantity=quantity,
                price=price
            )
            logger.info(f"LIMIT order successful: {response.get('orderId')}")
            return response
        except BinanceAPIException as e:
            logger.error(f"Binance API Error (Limit Order): {e.message}")
            raise
        except Exception as e:
            logger.error(f"Unexpected Error (Limit Order): {str(e)}")
            raise

    def place_stop_limit_order(self, symbol, side, quantity, price, stop_price):
        """Places a Stop-Limit Order on Binance Futures (Bonus)."""
        try:
            logger.info(f"Attempting STOP_LIMIT {side} order: {quantity} {symbol} at {price}, stop at {stop_price}")
            response = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type='STOP',
                timeInForce='GTC',
                quantity=quantity,
                price=price,
                stopPrice=stop_price
            )
            logger.info(f"STOP_LIMIT order successful: {response.get('orderId')}")
            return response
        except BinanceAPIException as e:
            logger.error(f"Binance API Error (Stop-Limit Order): {e.message}")
            raise
        except Exception as e:
            logger.error(f"Unexpected Error (Stop-Limit Order): {str(e)}")
            raise
