from rwl_core import Server
from server.injector import INJECTOR
from server.views.health import router as health_router
from server.views.pipelines import router as todo_router

app = Server.create(routers=[health_router, todo_router], injector=INJECTOR)
