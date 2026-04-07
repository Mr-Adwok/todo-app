from app.models.todo import Todo
from uuid import UUID


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
    for todo in results
]


    # get one todo

    async def get_todo_by_uuid(self,uuid:UUID,session:AsyncSession):
        # query
        # statement = select(Todo).where(uuid == Todo.uuid)
        statement = select(Todo).where(Todo.uid == uuid)
        get_todo = await session.exec(statement)
        result = get_todo.first()
        # title = result.title
        # print(title,"Hellllllllllllllooooooo am title yesssssssss my brother")
        # print(result,"______--------------------------------------------------------------")
        return result


    async def delete_todo_service(self,uuid:UUID,session:AsyncSession):
        # getting a todo
        statement = await self.get_todo_by_uuid(uuid,session)

        print(statement,"hellloo _______________ yep")
        # delete a statement
        # result = await session.delete(statement)
        if statement:
            await session.delete(statement)
            await session.commit()

        # return a result
        # print(result,"hellllo ------------------------------------------------")
        # return result

        # statement = select(Todo).where(Todo.uid == uuid)
        # get_todo = await session.exec(statement)
        # result = get_todo.first()
        # if result:
        #     await session.delete(result)


    async def update_todo_service(self,uuid:UUID,new_title_param,session:AsyncSession):
        statement = await self.get_todo_by_uuid(uuid,session)
        # title = statement.title
        # new_title_param = title
        statement.title = new_title_param["title"]
        new_ = statement.title

        print("new_title_param: ", "God is Love ____________________________",new_)
        # await session.add(statement)
        await session.commit()

        return statement









