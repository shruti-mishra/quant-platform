from abc import ABC, abstractmethod

class MarketDataProvider(ABC):

    @abstractmethod
    def get_history(
        self,
        symbol: str,
        start_date: str,
        end_date: str,
    ):
        """
        Return historical OHLCV data
        as a pandas DataFrame.
        """
        pass