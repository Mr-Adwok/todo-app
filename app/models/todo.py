import uuid
from sqlmodel import Field, SQLModel
import sqlalchemy.dialects.postgresql as pg

# an example mapping using the base
class Todo(SQLModel,table = True):

    uid:uuid.UUID = Field(
        sa_column=Column(pg.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    )
    title:str
    completed:bool
    created_at:datetime = Field(default_factory = datetime.utcnow)

