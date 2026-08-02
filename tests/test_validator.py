import pandas as pd
import pytest

from src.data.validator import check_missing_values


def test_check_missing_values_pass():
    df = pd.DataFrame({
        "Open": [100, 101],
        "Close": [102, 103],
    })

    check_missing_values(df)


def test_check_missing_values_fail():
    df = pd.DataFrame({
        "Open": [100, None],
        "Close": [102, 103],
    })

    with pytest.raises(ValueError):
        check_missing_values(df)