from sqlmodel import SQLModel
from app.settings import config
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncEngine,create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession





async_engine = create_async_engine(url = config.DATABASE_URL, echo=True)

async def init_db():
    async with async_engine.begin() as conn:


        print("Database connected")
        from app.models.todo import Todo
        await conn.run_sync(SQLModel.metadata.create_all)
        print(config.DATABASE_URL)
        # print(SQLModel.metadata.tables)

# async def init_db():
#     async with async_engine.begin() as conn:  # 🔥 use begin()
#         print("Database connected")
#         await conn.run_sync(SQLModel.metadata.create_all)

SessionLocal = sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_session() -> AsyncSession:
    async with SessionLocal() as session:
        yield session

print(config.DATABASE_URL)