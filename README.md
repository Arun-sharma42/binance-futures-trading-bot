# Binance Futures Testnet Trading Bot

A simplified Python application to place orders on the Binance Futures Testnet (USDT-M) with robust logging and input validation.

## Features
- **Order Types**: MARKET, LIMIT, and STOP_LIMIT (Bonus).
- **Sides**: BUY and SELL.
- **Validation**: Strict input validation for symbols, quantity, and price.
- **Logging**: Comprehensive logging of API requests, responses, and errors to `trading_bot.log`.
- **UI**: Enhanced CLI output using the `rich` library.

## Setup Instructions

### 1. Prerequisites
- Python 3.8+
- Binance Futures Testnet account and API credentials.

### 2. Installation
Clone this repository or extract the zip folder, then navigate to the project root:

```bash
pip install -r requirements.txt
```

### 3. Configuration
Create a `.env` file in the root directory (you can use `.env.template` as a guide):

```text
BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_api_secret
```

## Usage Examples

### Place a Market Order
```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Place a Limit Order
```bash
python cli.py --symbol ETHUSDT --side SELL --type LIMIT --quantity 0.1 --price 2500
```

### Place a Stop-Limit Order (Bonus)
```bash
python cli.py --symbol BTCUSDT --side BUY --type STOP_LIMIT --quantity 0.001 --price 65000 --stop_price 64500
```

## Project Structure
- `bot/`: Core logic package.
  - `client.py`: Binance API client wrapper.
  - `orders.py`: Order placement methods.
  - `validators.py`: Input validation logic.
  - `logging_config.py`: Centralized logging setup.
- `cli.py`: Command-line interface entry point.
- `trading_bot.log`: Log file generated during runtime.

## Assumptions
- The bot is designed specifically for the **Binance Futures Testnet (USDT-M)**.
- User has sufficient margin/balance in their testnet account.
- The `timeInForce` for Limit and Stop-Limit orders is set to `GTC` (Good Till Cancelled).

## Error Handling
The application handles:
- **API Errors**: Logs and displays specific error messages from Binance (e.g., "Account has insufficient balance").
- **Validation Errors**: Catches invalid symbols, negative quantities, or missing prices before calling the API.
- **Network Failures**: Logs connection issues and exits gracefully.
