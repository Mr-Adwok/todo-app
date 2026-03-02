from pydantic import BaseModel
import uuid
# from datetime import datetime,date





class CreateTodo(BaseModel):
    title:str
    description:str



