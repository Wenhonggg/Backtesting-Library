class MetricCalculator:
    def __init__(self, trades):
        self.trades = trades

    def calculate(self):
        return {
            "total_trades": len(self.trades),
            "win_rate": 0.5,
            "sharpe_ratio": 1.2
        }