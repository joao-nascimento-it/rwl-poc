from server.models.pipeline import Pipeline
from server.orchestrator.business_process import BusinessProcess
from server.orchestrator.dtos import StartPipelineDTO


class Orchestrator:
    def start(self, dto: StartPipelineDTO) -> Pipeline:
        pipeline = Pipeline(lhs=dto.lhs, rhs=dto.rhs)
        pipeline = BusinessProcess(pipeline=pipeline).execute()
        return pipeline
