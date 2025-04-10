class RiskManager:
    def __init__(self, max_drawdown=0.2):
        self.max_drawdown = max_drawdown

    def evaluate(self, portfolio):
        current_drawdown = portfolio.get("drawdown", 0.1)
        return current_drawdown <= self.max_drawdown
