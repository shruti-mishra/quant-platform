from dataclasses import dataclass

@dataclass
class PerformanceMetrics:
    total_return: float
    win_rate: float
    expectancy: float
    profit_factor: float
    max_drawdown: float


def total_return(initial_value: float, final_value: float) -> float:
    """
    Returns the percentage total return.
    """

    def profit_factor(
    gross_profit: float,
    gross_loss: float
) -> float: