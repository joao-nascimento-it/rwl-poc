from dataclasses import dataclass
from enum import StrEnum


class StepEnum(StrEnum):
    "The step ordering is IMPORTANT!"
    STARTING = "Starting"
    ADDING = "Adding"
    SUBTRACTING = "Subtracting"
    MULTIPLING = "Multipling"
    VALIDATING = "Validating"
    DONE = "Done"


@dataclass(kw_only=True)
class Pipeline:
    lhs: int
    rhs: int
    result: int | None = None
    step: StepEnum = StepEnum.STARTING
