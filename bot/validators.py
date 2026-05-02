import re

def validate_symbol(symbol: str) -> str:
    """Validates the trading symbol (e.g., BTCUSDT)."""
    if not symbol or not isinstance(symbol, str):
        raise ValueError("Symbol must be a non-empty string.")
    
    symbol = symbol.upper().strip()
    if not re.match(r'^[A-Z0-9]+USDT$', symbol):
        raise ValueError(f"Invalid symbol format: {symbol}. Must be a USDT-M pair (e.g., BTCUSDT).")
    
    return symbol

def validate_side(side: str) -> str:
    """Validates the order side (BUY or SELL)."""
    side = side.upper().strip()
    if side not in ['BUY', 'SELL']:
        raise ValueError(f"Invalid side: {side}. Must be BUY or SELL.")
    return side

def validate_quantity(quantity: float) -> float:
    """Validates the order quantity."""
    try:
        qty = float(quantity)
        if qty <= 0:
            raise ValueError("Quantity must be greater than 0.")
        return qty
    except (ValueError, TypeError):
        raise ValueError(f"Invalid quantity: {quantity}. Must be a positive number.")

def validate_price(price: float) -> float:
    """Validates the order price for LIMIT orders."""
    try:
        p = float(price)
        if p <= 0:
            raise ValueError("Price must be greater than 0.")
        return p
    except (ValueError, TypeError):
        raise ValueError(f"Invalid price: {price}. Must be a positive number.")
