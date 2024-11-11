from dataclasses import dataclass


@dataclass(kw_only=True, frozen=True)
class StartPipelineDTO:
    lhs: int
    rhs: int
