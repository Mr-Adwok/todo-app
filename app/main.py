from app.db.session import init_db
from starlette.routing import Route
from app.routes.todos import create_task
from contextlib import asynccontextmanager
from starlette.applications import Starlette
from starlette.responses import PlainTextResponse




@asynccontextmanager
async def lifespan(app):
    print("Sever starting")
    await init_db()
    print("INIT_DB CALLED")
    yield
    print("Sever shutdown");






async def homepage(request):
    return PlainTextResponse("Hello world!")



route = [
    Route('/',homepage),
    Route('/Todo',create_task, methods=["POST"])
]

app = Starlette(
    debug = True,
    routes = route,
    lifespan = lifespan
)

