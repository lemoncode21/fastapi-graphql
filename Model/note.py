from sqlmodel import SQLModel, Field
from typing import Optional


class Note(SQLModel, table=True):
    __tablename__ = "note"

    id: Optional[int] = Field(None, primary_key=True, nullable=False)
    name: str
    description: str
