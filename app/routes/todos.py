from app.db.session import get_session
from starlette.requests import Request
from app.services.all_services import TodoService
from starlette.responses import JSONResponse
from app.schemas.schema import  CreateTodo
import traceback

# service class
todo_service = TodoService()



# from starlette.requests import Request
# from starlette.responses import JSONResponse

async def create_task(request: Request):
    try:
        content = await request.json()
        todo = CreateTodo(**content)

        # async for session in get_session():
        async with get_session() as session:
            # Create the Todo in DB
            new_todo = await todo_service.create_todo(todo, session)

        # Convert to JSON-serializable dict
        todo_dict = new_todo.model_dump()
        todo_dict["created_at"] = new_todo.created_at.isoformat()
        todo_dict["uid"] = str(new_todo.uid)

        return JSONResponse(todo_dict, status_code=201)

    except Exception as e:
        return JSONResponse({"detail": str(e)}, status_code=400)


    # except Exception as e:
    #     return JSONResponse({"detail": str(e)}, status_code=400)
    # # except Exception as e:
    #     print(e)



async def all_todo(request:Request):

    try:
        async with get_session() as session:
            content = await todo_service.get_todos(session)
            # console.log(content)
            print(str(content),"Hello am content")

            return JSONResponse(content)

    except Exception as e:
        print(e)
        # return e
        print(traceback.format_exc())
        return JSONResponse({"detail": str(e)}, status_code=400)




async def get_one_todo(request:Request):
    try:
        async with get_session() as session:
            uuid = request.path_params['uuid']
            content = await todo_service.get_todo_by_uuid(uuid,session)
            content_dict = content.dict()
            content_dict["created_at"] = content.created_at.isoformat()
            content_dict["uid"] = str(content.uid)
            print("UUID RAW:", request.path_params['uuid'])
            print(type(content))
            return JSONResponse(content_dict)

    except Exception as e:
            return JSONResponse({"detail": str(e)}, status_code=404)
            # print(e)
            # return e

async def delete_todo(request:Request):
    try:
        async with get_session() as session:
            uuid = request.path_params['uuid']
            content = await todo_service.delete_todo_service(uuid,session)
            # content_dict = content.dict()

            return JSONResponse({"message":"Deleted"},status_code = 200)

    except Exception as e:
        return JSONResponse({"detail": str(e)}, status_code=404)


async def update_todo(request:Request):

    async with get_session() as session :
        uuid = request.path_params['uuid']
        title = await request.json()
        content = await todo_service.update_todo_service(uuid,title,session)
        print(content)
        content_dict = content.dict()
        content_dict["created_at"] = content.created_at.isoformat()
        content_dict["uid"] = str(content.uid)

        return JSONResponse({"successful update: ":content_dict})
















# Here are your 6-line hints:

# ✅ Parse and validate content using CreateTodo(**content) before calling the service.

# ⚠️ Wrap validation in try/except to return 400 if data is invalid.

# 🔄Get session using async with get_session() as session: (if it’s an async generator).

# 🚀 Call await todo_service.create_todo(validated_data, session).

# 🧼 Convert returned ORM object into dict (or response schema) before returning JSON.

# 🎯 Return JSONResponse(data, status_code=201) for proper REST behavior.





