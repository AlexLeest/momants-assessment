import abc
from abc import ABC


class AbstractLlmProvider(ABC):
    api_key: str

    @abc.abstractmethod
    def __init__(self, api_key: str):
        self.api_key = api_key

    @abc.abstractmethod
    def query(self, input: str):
        raise NotImplemented()