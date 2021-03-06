"""
Defines the blueprint for notebooks
"""
from flask import Blueprint
from flask_restful import Api

from resources import NotebookResource, NotebooksResource, NoteResource, NotesResource

APP_BLUEPRINT = Blueprint("app", __name__)
Api(APP_BLUEPRINT).add_resource(NotebookResource, "/app/notebook/<int:id>")

Api(APP_BLUEPRINT).add_resource(NotebooksResource, "/app/notebooks")

Api(APP_BLUEPRINT).add_resource(NoteResource, "/app/note/<int:id>")

Api(APP_BLUEPRINT).add_resource(NotesResource, "/app/notes")
