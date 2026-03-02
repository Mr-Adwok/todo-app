from app.models.todo import Todo

from sqlmodel import select,desc
from app.schemas.schema import CreateTodo
from sqlmodel.ext.asyncio.session import AsyncSession


# from db.session import get_session




class TodoService():

    async def create_todo(self,todo:CreateTodo,session:AsyncSession):

        todo_dict = todo.model_dump()
        new_todo = Todo(**todo_dict)

        session.add(new_todo)
        await session.commit()
        await session.refresh(new_todo)
        return new_todo




