from abc import ABC, abstractmethod

class Transformer(ABC):
    @abstractmethod
    def transform(self, dataframe: pd.DataFrame, transformations: list) -> pd.DataFrame:
        """Transform dataframe following `transformations` indications."""
        pass