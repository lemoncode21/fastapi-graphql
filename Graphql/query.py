from typing import List

import strawberry

from Service.note import NoteService
from schema import NoteType


@strawberry.type
class Query:

    @strawberry.field
    def hello(self) -> str:
        return "Hello World!"

    @strawberry.field
    async def get_all(self) -> List[NoteType]:
        return await NoteService.get_all_note()

    @strawberry.field
    async def get_by_id(self, id: int) -> NoteType:
        return await NoteService.get_by_id(id)
