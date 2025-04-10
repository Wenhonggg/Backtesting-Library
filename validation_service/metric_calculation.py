import numpy as np

class MetricCalculator:
    def __init__(self, trades, equity_curve):
        self.trades = trades
        self.equity_curve = equity_curve

    def calculate(self):
        profits = [t['profit'] for t in self.trades]
        returns = np.diff(self.equity_curve)
        equity_array = np.array(self.equity_curve)

        win_rate = sum(1 for p in profits if p > 0) / len(profits) if profits else 0
        avg_return = np.mean(returns) if len(returns) > 1 else 0
        std_return = np.std(returns) if len(returns) > 1 else 1
        sharpe_ratio = avg_return / std_return * np.sqrt(252) if std_return != 0 else 0

        running_max = np.maximum.accumulate(equity_array)
        drawdowns = (running_max - equity_array) / running_max
        max_drawdown = np.max(drawdowns)

        trade_freq = len(self.trades) / len(self.equity_curve) if self.equity_curve else 0

        return {
            "total_trades": len(self.trades),
            "win_rate": round(win_rate, 2),
            "sharpe_ratio": round(sharpe_ratio, 2),
            "max_drawdown": round(max_drawdown, 4),
            "trade_frequency": round(trade_freq, 4),
            "final_equity": round(self.equity_curve[-1], 2) if self.equity_curve else None
        }