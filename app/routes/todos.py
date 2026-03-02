from app.db.session import get_session
from starlette.requests import Request
from app.services.all_services import TodoService
from starlette.responses import JSONResponse
from app.schemas.schema import  CreateTodo

# service class
todo_service = TodoService()



async def create_task(request:Request):
    try:
        content = await request.json()
        todo = CreateTodo(**content)
        async for session in get_session():
            new_todo = await todo_service.create_todo(todo, session)


        return JSONResponse(new_todo,status_code = 201)


    except Exception as e:
        return JSONResponse({"detail": str(e)}, status_code=400)
    # except Exception as e:
    #     print(e)










# Here are your 6-line hints:

# ✅ Parse and validate content using CreateTodo(**content) before calling the service.

# ⚠️ Wrap validation in try/except to return 400 if data is invalid.

# 🔄Get session using async with get_session() as session: (if it’s an async generator).

# 🚀 Call await todo_service.create_todo(validated_data, session).

# 🧼 Convert returned ORM object into dict (or response schema) before returning JSON.

# 🎯 Return JSONResponse(data, status_code=201) for proper REST behavior.





