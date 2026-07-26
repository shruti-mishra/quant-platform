"""
Risk Calculator

Provides utility functions for:
- Portfolio value calculation
- Risk amount calculation
- Maximum permissible loss per trade
- Position sizing
"""


def calculate_portfolio_value(cash: float, holdings_value: float) -> float:
    """
    Calculate total portfolio value.

    Args:
        cash: Available cash balance
        holdings_value: Current market value of all holdings

    Returns:
        Total portfolio value
    """
    return cash + holdings_value


def calculate_risk_amount(
    portfolio_value: float,
    risk_percentage: float
) -> float:
    """
    Calculate maximum permissible loss per trade.

    Example:
        Portfolio = 10,00,000
        Risk % = 1

        Returns = 10,000
    """

    if risk_percentage <= 0:
        raise ValueError("Risk percentage must be greater than 0.")

    return portfolio_value * (risk_percentage / 100)


def calculate_position_size(
    entry_price: float,
    stop_loss_price: float,
    risk_amount: float
) -> int:
    """
    Calculate position size based on risk.

    Formula:
        Position Size = Risk Amount / |Entry - Stop Loss|

    Returns:
        Number of shares/units to buy.
    """

    if entry_price <= 0:
        raise ValueError("Entry price must be positive.")

    if stop_loss_price <= 0:
        raise ValueError("Stop-loss price must be positive.")

    if risk_amount <= 0:
        raise ValueError("Risk amount must be positive.")

    risk_per_share = abs(entry_price - stop_loss_price)

    if risk_per_share == 0:
        raise ValueError("Entry price and stop-loss price cannot be equal.")

    position_size = risk_amount / risk_per_share

    return int(position_size)


def calculate_trade_risk(
    cash: float,
    holdings_value: float,
    risk_percentage: float,
    entry_price: float,
    stop_loss_price: float,
) -> dict:
    """
    Complete risk calculation.

    Returns:
        {
            portfolio_value,
            risk_percentage,
            risk_amount,
            position_size
        }
    """

    portfolio_value = calculate_portfolio_value(
        cash,
        holdings_value,
    )

    risk_amount = calculate_risk_amount(
        portfolio_value,
        risk_percentage,
    )

    position_size = calculate_position_size(
        entry_price,
        stop_loss_price,
        risk_amount,
    )

    return {
        "portfolio_value": round(portfolio_value, 2),
        "risk_percentage": risk_percentage,
        "risk_amount": round(risk_amount, 2),
        "position_size": position_size,
    }



def portfolio_risk(account_balance, open_positions):
    """
    account_balance: float
    open_positions: list of risk amounts

    Returns:
        total_open_risk
        risk_percentage
    """

def reward_risk_ratio(entry_price, stop_loss, target_price):

if __name__ == "__main__":
    result = calculate_trade_risk(
        cash=10000,
        holdings_value=202107,
        risk_percentage=1,
        entry_price=906,
        stop_loss_price=806,
    )

    print(result)