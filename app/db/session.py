from sqlmodel import SQLModel   # import sqlModel for metadata purpose
from app.settings import config  # loading the class that is handling .env
from sqlalchemy.orm import sessionmaker # session-maker for making a session
from sqlalchemy.ext.asyncio import AsyncEngine,create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession #
from contextlib import asynccontextmanager




#  an engine is crucial to connect to a database so you need it that's the first thing to consider
async_engine = create_async_engine(url = config.DATABASE_URL, echo=True)

async def init_db():
    async with async_engine.begin() as conn:


        print("Database connected")
        from app.models.todo import Todo
        await conn.run_sync(SQLModel.metadata.create_all)
        print(config.DATABASE_URL)
        # print(SQLModel.metadata.tables)


SessionLocal = sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)




@asynccontextmanager
async def get_session():
    async with SessionLocal() as session:
        yield session



# async def get_session() -> AsyncSession:
#     async with SessionLocal() as session:
#         yield session

print(config.DATABASE_URL)