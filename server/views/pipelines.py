from rwl_core import Router, RWLResponse, Injector
from server.models.pipeline import Pipeline
from server.orchestrator import Orchestrator
from server.orchestrator.dtos import StartPipelineDTO

router = Router.create("/pipelines")


@router.post("/", response_model=RWLResponse[Pipeline])
def start_pipeline(dto: StartPipelineDTO):
    orchestrator = Injector.inject(Orchestrator)
    pipeline = orchestrator.start(dto)
    return RWLResponse(data=pipeline)
