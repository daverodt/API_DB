from pydantic import BaseModel, Schema
from fastapi import Query
from models.author import Author
from utils.const import ISBN_DESCRIPTION

class Book(BaseModel):
	isbn: str = Schema(None, description=ISBN_DESCRIPTION)
	name: str
	author: Author
	year: int = Schema(None, lt=1900, gt=2100)

