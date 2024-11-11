from dataclasses import dataclass
from server.orchestrator.business_process.steps import STEPS
from server.models.pipeline import Pipeline, StepEnum


@dataclass(kw_only=True)
class BusinessProcess:
    pipeline: Pipeline

    def execute(self) -> Pipeline:
        while self.pipeline.step != StepEnum.DONE:
            step_class = STEPS[self.pipeline.step]
            step_class(pipeline=self.pipeline).execute()
            self.__forward()
        return self.pipeline

    def __forward(self):
        steps = tuple(StepEnum)
        index = steps.index(self.pipeline.step)
        self.pipeline.step = steps[min(index + 1, len(steps) - 1)]
