""" Defines the Notebook repository """

from models import Notebook
from sqlalchemy.orm import load_only
import bcrypt
import string
import random
from werkzeug.exceptions import UnprocessableEntity, Forbidden
import time


class NotebookRepository:

    @staticmethod
    def create(user, name, color):
        """ Create a new notebook """

        if len(name) > 24:
            raise UnprocessableEntity(description="NOTEBOOK_NAME_MAX_LENGTH")

        current_time = int(time.time())
        notebook = Notebook(
            name=name,
            color=color,
            user=user.id,
            created_at=current_time,
            updated_at=current_time
        )

        notebook.save()

        return notebook.transform()
    
    @staticmethod
    def getAll(user):
        """ Get all notebooks for the authenticated user """

        notebooks = Notebook.query.filter_by(user=user.id).all()

        ret = []
        for notebook in notebooks:
            ret.append({
                'name': notebook.name,
                'color': notebook.color
            })
        
        return ret
