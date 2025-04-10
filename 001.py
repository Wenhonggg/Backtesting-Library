def generate_trade_signals(prices, short_window=5, long_window=20):
    """
    Generates buy/sell signals based on moving average crossover strategy.

    Parameters:
    - prices: List of float, historical price data (latest last)
    - short_window: int, short-term moving average window
    - long_window: int, long-term moving average window

    Returns:
    - signals: List of str, 'BUY', 'SELL', or 'HOLD' for each price point
    """
    signals = ['HOLD'] * len(prices)
    if len(prices) < long_window:
        return signals  # Not enough data

    for i in range(long_window, len(prices)):
        short_avg = sum(prices[i - short_window:i]) / short_window
        long_avg = sum(prices[i - long_window:i]) / long_window

        if short_avg > long_avg:
            signals[i] = 'BUY'
        elif short_avg < long_avg:
            signals[i] = 'SELL'
        else:
            signals[i] = 'HOLD'
    return signals
