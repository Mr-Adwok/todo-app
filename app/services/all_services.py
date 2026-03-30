from app.models.todo import Todo

from sqlmodel import select,desc
from app.schemas.schema import CreateTodo
from sqlmodel.ext.asyncio.session import AsyncSession


# from db.session import get_session




class TodoService():

    # create todo
    async def create_todo(self,todo:CreateTodo,session:AsyncSession):

        todo_dict = todo.model_dump()
        new_todo = Todo(**todo_dict)

        session.add(new_todo)
        await session.commit()
        await session.refresh(new_todo)
        return new_todo


    # get all todo

    async def get_todos(self,session:AsyncSession):
        statement = select(Todo)
        get_all_todo = await session.exec(statement)
        results =  get_all_todo.all()
        print("Length:", len(results))
        print(results[0])
        return [
    {
        "uid": str(todo.uid),
        "title": todo.title,
        "description": todo.description,
        "completed": todo.completed,
        "created_at": todo.created_at.isoformat()
    }
    for todo in results  # ✅ use 'results', not 'todos'
]


