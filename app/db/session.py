from sqlmodel import SQLModel
from settings import config
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncEngine,create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession





async_engine = create_async_engine(url = config.DATABASE_URL, echo=True)

async def init_db():
    async with async_engine.connect() as conn:
        from models.todo import Todo
        print("Database connected")
        await conn.run_sync(SQLModel.metadata.create_all)
        print(SQLModel.metadata.tables)




SessionLocal = sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_session() -> AsyncSession:
    async with SessionLocal() as session:
        yield session