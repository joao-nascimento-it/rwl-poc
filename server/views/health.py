from rwl_core import RWLResponse, Router

router = Router.create("/health")


@router.get("/")
def health():
    return RWLResponse(data="Hello World!")
