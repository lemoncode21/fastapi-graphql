from Model.note import Note
from config import db
from sqlalchemy.sql import select
from sqlalchemy import update as sql_update, delete as sql_delete


class NoteRepository:

    @staticmethod
    async def create(note_data: Note):
        async with db as session:
            async with session.begin():
                session.add(note_data)
            await db.commit_rollback()

    @staticmethod
    async def get_by_id(note_id: int):
        async with db as session:
            stmt = select(Note).where(Note.id == note_id)
            result = await session.execute(stmt)
            note = result.scalars().first()
            return note

    @staticmethod
    async def get_all():
        async with db as session:
            query = select(Note)
            result = await session.execute(query)
            return result.scalars().all()

    @staticmethod
    async def update(note_id: int, note_data: Note):
        async with db as session:
            stmt = select(Note).where(Note.id == note_id)
            result = await session.execute(stmt)

            note = result.scalars().first()
            note.name = note_data.name
            note.description = note_data.description

            query = sql_update(Note).where(Note.id == note_id).values(
                **note.dict()).execution_options(synchronize_session="fetch")

            await session.execute(query)
            await db.commit_rollback()

    @staticmethod
    async def delete(note_id: int):
        async with db as session:
            query = sql_delete(Note).where(Note.id == note_id)
            await session.execute(query)
            await db.commit_rollback()
