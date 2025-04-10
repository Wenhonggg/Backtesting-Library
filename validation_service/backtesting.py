class Backtester:
    def __init__(self, strategy, data):
        self.strategy = strategy
        self.data = data
        self.trades = []
        self.results = {}

    def run(self):
        for index, row in self.data.iterrows():
            if self.strategy.should_enter(row):
                self.trades.append({"entry": row['price'], "time": row['timestamp']})
        self.results = {"total_trades": len(self.trades)}