from abc import ABC, abstractmethod
from dataclasses import dataclass
from server.models.pipeline import Pipeline


@dataclass(kw_only=True, frozen=True)
class AbstractStep(ABC):
    pipeline: Pipeline

    @abstractmethod
    def execute(self): ...

    @property
    def result(self):
        assert isinstance(self.pipeline.result, int)
        return self.pipeline.result
