class Backtester:

    def run(
        self,
        prices,
        strategy,
        initial_capital=100000,
        commission=0.001,
    ):
        """
        Simulate trades and return results.
        """