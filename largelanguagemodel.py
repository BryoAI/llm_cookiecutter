import abc


class LargeLanguageModel(abc.ABC):
    @abc.abstractmethod
    def query(query: str) -> str:
        pass
