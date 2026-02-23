from starlette.routing import Route
from contextlib import asynccontextmanager
from starlette.applications import Starlette
from .db.session import init_db
from starlette.responses import PlainTextResponse




@asynccontextmanager
async def lifespan(app):
    print("Sever starting")
    await init_db()
    yield
    print("Sever shutdown");






async def homepage(request):
    return PlainTextResponse("Hello world!")



route = [
    Route('/',homepage)
]

app = Starlette(
    debug = True,
    routes = route,
    lifespan = lifespan
)

