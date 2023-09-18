import strawberry
from Service.note import NoteService
from schema import NoteType, NoteInput


@strawberry.type
class Mutation:

    @strawberry.mutation
    async def create_note(self, note_data: NoteInput) -> NoteType:
        return await NoteService.add_note(note_data)

    @strawberry.mutation
    async def delete_note(self, note_id: int) -> str:
        return await NoteService.delete(note_id)

    @strawberry.mutation
    async def update_note(self, note_id: int, note_data: NoteInput) -> str:
        return await NoteService.update(note_id,note_data)