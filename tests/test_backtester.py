import unittest
import pandas as pd
from validation_service import Backtester

class DummyStrategy:
    def should_enter(self, row):
        return row['signal'] == 1

class TestBacktester(unittest.TestCase):

    def setUp(self):
        self.data = pd.DataFrame({
            'timestamp': [1, 2, 3, 4, 5],
            'price': [100, 101, 102, 103, 104],
            'signal': [0, 1, 0, 1, 0]
        })
        self.strategy = DummyStrategy()
        self.backtester = Backtester(strategy=self.strategy, data=self.data)

    def test_run_backtest(self):
        self.backtester.run()
        self.assertEqual(len(self.backtester.trades), 2)
        self.assertIn('total_trades', self.backtester.results)
        self.assertEqual(self.backtester.results['total_trades'], 2)

    def test_trade_structure(self):
        self.backtester.run()
        for trade in self.backtester.trades:
            self.assertIn('entry', trade)
            self.assertIn('time', trade)

if __name__ == '__main__':
    unittest.main()