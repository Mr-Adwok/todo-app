from app.db.session import init_db
from starlette.routing import Route
from app.routes.todos import create_task,all_todo,get_one_todo,delete_todo,update_todo
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
    Route('/Todo',create_task, methods=["POST"]),
    Route('/all',all_todo,methods = ["GET"] ),
    Route('/get_one_todo1/{uuid:uuid}',get_one_todo,methods = ["GET"]),
    Route('/delete-todo/{uuid:uuid}',delete_todo,methods = ["DELETE"]),
    Route('/update-your-title/{uuid:uuid}',update_todo, methods = ["PUT"])
]

app = Starlette(
    debug = True,
    routes = route,
    lifespan = lifespan
)

