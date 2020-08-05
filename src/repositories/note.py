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
