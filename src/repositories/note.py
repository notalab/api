""" Defines the Note repository """

import random
import string
import time

import bcrypt
from sqlalchemy.orm import load_only
from werkzeug.exceptions import Forbidden, UnprocessableEntity

from models import Note


class NoteRepository:
    @staticmethod
    def create(user, notebook_id, title, content):
        """ Create a new note """

        current_time = int(time.time())
        note = Note(
            notebook_id=notebook_id,
            title=title,
            content=content,
            user_id=user.id,
            created_at=current_time,
            updated_at=current_time
        )

        note.save()

        return note.transform()
    
    @staticmethod
    def update(user, id, title, content):
        """ Update a notebook by ID """

        current_time = int(time.time())
        note = Note.query.filter_by(id=id, user_id=user.id).first()

        if not note:
            raise UnprocessableEntity(description="NOTE_NOT_FOUND")
        
        note.title = title
        note.content = content
        note.updated_at = current_time
        note.save()

        return note.transform()
