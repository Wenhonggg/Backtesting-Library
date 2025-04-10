class Backtester:
    def __init__(self, strategy, data):
        self.strategy = strategy
        self.data = data
        self.trades = []
        self.results = {}
        self.equity = []

    def run(self):
        position = None
        entry_price = None
        equity = 10000  # starting equity
        self.equity.append(equity)

        for index, row in self.data.iterrows():
            signal = row['signal']
            price = row['price']

            if self.strategy.should_enter(signal, position):
                if position is not None:
                    # exit previous trade
                    profit = (price - entry_price) if position == 1 else (entry_price - price)
                    equity += profit
                    self.trades.append({
                        "entry": entry_price,
                        "exit": price,
                        "side": "BUY" if position == 1 else "SELL",
                        "profit": profit,
                        "entry_time": row['timestamp']
                    })
                entry_price = price
                position = signal

            self.equity.append(equity)

        self.results = {
            "total_trades": len(self.trades),
            "equity_curve": self.equity,
            "final_equity": equity
        }