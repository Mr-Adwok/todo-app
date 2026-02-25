import uuid
from datetime import datetime
from sqlmodel import Field, SQLModel,Column
import sqlalchemy.dialects.postgresql as pg

# an example mapping using the base
class Todo(SQLModel,table = True):
    __tablename__ = "todo1"

    uid:uuid.UUID = Field(
        sa_column=Column(pg.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    )
    title:str
    description:str
    completed:bool
    created_at:datetime = Field(default_factory=datetime.now)

    def __repr__(self):
        return f"<Book {self.title}>"

    class Config:
        orm_mode = True

