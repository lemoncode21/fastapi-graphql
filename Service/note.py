from Model.note import Note
from Repository.note import NoteRepository
from schema import NoteInput, NoteType


class NoteService:

    @staticmethod
    async def add_note(note_data: NoteInput):
        note = Note()
        note.name = note_data.name
        note.description = note_data.description
        await NoteRepository.create(note)

        return NoteType(id=note.id, name=note.name, description=note.description)

    @staticmethod
    async def get_all_note():
        list_note = await NoteRepository.get_all()
        return [NoteType(id=note.id, name=note.name, description=note.description) for note in list_note]

    @staticmethod
    async def get_by_id(note_id: int):
        note = await NoteRepository.get_by_id(note_id)
        return NoteType(id=note.id, name=note.name, description=note.description)

    @staticmethod
    async def delete(note_id: int):
        await NoteRepository.delete(note_id)
        return f'Successfully deleted data by id {note_id}'

    @staticmethod
    async def update(note_id:int, note_data: NoteInput):
        note = Note()
        note.name = note_data.name
        note.description = note_data.description
        await NoteRepository.update(note_id,note)

        return f'Successfully updated data by id {note_id}'
