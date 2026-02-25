from .models.todo import Todo
from datetime import datetime
from db.session import session
from sqlmodel import select,desc
from schemas.schema import CreateTodo
# from db.session import get_session




class Service_Act():

    async def create_todo(self,session:AsyncSession):

        todo = CreateTodo().model_dump()
        new_todo = Todo(**todo)

        session.add(new_todo)
        await session.commit()

        return new_todo




