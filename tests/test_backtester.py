from validation_service import Backtester, MetricCalculator, load_data, GraphDisplayer

class TrendStrategy:
    def should_enter(self, signal, current_position):
        if signal == 0:
            return False
        return signal != current_position

if __name__ == "__main__":
    data = load_data("btc_signal_data.csv")
    strategy = TrendStrategy()
    bt = Backtester(strategy=strategy, data=data)
    bt.run()

    print("=== Backtest Trades ===")
    # for trade in bt.trades:
    #     print(trade)

    mc = MetricCalculator(trades=bt.trades, equity_curve=bt.equity)
    metrics = mc.calculate()

    print("\n=== Backtest Metrics ===")
    for k, v in metrics.items():
        print(f"{k}: {v}")

    print(f"\nFinal Equity: {bt.results['final_equity']}")

    GraphDisplayer(bt.results).show_equity_curve()