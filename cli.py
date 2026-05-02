import argparse
import sys
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

from bot.client import BinanceClient
from bot.orders import OrderManager
from bot.validators import validate_symbol, validate_side, validate_quantity, validate_price
from bot.logging_config import logger

console = Console()

def print_response(response):
    """Prints a formatted table with order response details."""
    table = Table(title="Order Execution Details", title_style="bold magenta")
    
    table.add_column("Field", style="cyan")
    table.add_column("Value", style="green")
    
    fields = ['symbol', 'orderId', 'clientOrderId', 'status', 'type', 'side', 'origQty', 'avgPrice', 'executedQty']
    
    for field in fields:
        val = response.get(field, "N/A")
        table.add_row(field, str(val))
    
    console.print(table)

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot CLI")
    
    parser.add_argument("--symbol", required=True, help="Trading symbol (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"], help="Order side")
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT", "STOP_LIMIT"], help="Order type")
    parser.add_argument("--quantity", type=float, required=True, help="Order quantity")
    parser.add_argument("--price", type=float, help="Order price (required for LIMIT and STOP_LIMIT)")
    parser.add_argument("--stop_price", type=float, help="Stop price (required for STOP_LIMIT)")

    args = parser.parse_args()

    try:
        # Validate Inputs
        symbol = validate_symbol(args.symbol)
        side = validate_side(args.side)
        quantity = validate_quantity(args.quantity)
        
        if args.type in ["LIMIT", "STOP_LIMIT"]:
            if not args.price:
                console.print("[bold red]Error:[/bold red] Price is required for LIMIT and STOP_LIMIT orders.")
                sys.exit(1)
            price = validate_price(args.price)
        
        if args.type == "STOP_LIMIT":
            if not args.stop_price:
                console.print("[bold red]Error:[/bold red] Stop price is required for STOP_LIMIT orders.")
                sys.exit(1)
            stop_price = validate_price(args.stop_price)

        # Initialize Client and Manager
        console.print(Panel(f"🚀 Initializing Order: [bold]{args.type} {side} {quantity} {symbol}[/bold]", border_style="blue"))
        
        binance_client = BinanceClient()
        client = binance_client.get_client()
        order_manager = OrderManager(client)

        # Place Order
        if args.type == "MARKET":
            response = order_manager.place_market_order(symbol, side, quantity)
        elif args.type == "LIMIT":
            response = order_manager.place_limit_order(symbol, side, quantity, price)
        elif args.type == "STOP_LIMIT":
            response = order_manager.place_stop_limit_order(symbol, side, quantity, price, stop_price)

        # Success Output
        console.print("[bold green]Success![/bold green] Order placed successfully.")
        print_response(response)

    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {str(e)}")
        logger.error(f"CLI Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
