from server.models.pipeline import StepEnum
from server.orchestrator.business_process.steps.abstract import AbstractStep
from server.orchestrator.business_process.steps.starting import StartingStep
from server.orchestrator.business_process.steps.adding import AddingStep
from server.orchestrator.business_process.steps.subtracting import SubtractingStep
from server.orchestrator.business_process.steps.multiplying import MultiplingStep
from server.orchestrator.business_process.steps.validating import ValidatingStep


STEPS: dict[StepEnum, type[AbstractStep]] = {
    StepEnum.STARTING: StartingStep,
    StepEnum.ADDING: AddingStep,
    StepEnum.SUBTRACTING: SubtractingStep,
    StepEnum.MULTIPLING: MultiplingStep,
    StepEnum.VALIDATING: ValidatingStep,
}
