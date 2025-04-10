import matplotlib.pyplot as plt

class GraphDisplayer:
    def __init__(self, results):
        self.results = results

    def show_equity_curve(self):
        equity = self.results.get("equity", [100, 105, 102, 110])
        plt.plot(equity)
        plt.title("Equity Curve")
        plt.xlabel("Time")
        plt.ylabel("Equity")
        plt.grid(True)
        plt.show()