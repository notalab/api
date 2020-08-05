import jwt

from . import db
from .abc import BaseModel, MetaBaseModel


class Note(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The Note Model """

    __tablename__ = "notes"

    id = db.Column(db.Integer, primary_key=True)
    notebook_id = db.Column(db.Integer(), db.ForeignKey("notebooks.id"), nullable=False)
    title = db.Column(db.String(32), nullable=False)
    content = db.Column(db.String())
    user_id = db.Column(db.Integer(), nullable=False)
    created_at = db.Column(db.Integer(), nullable=False)
    updated_at = db.Column(db.Integer(), nullable=False)

    def __init__(self, notebook_id, title, content, user_id, created_at, updated_at):
        """ Create a new Note """
        self.notebook_id = notebook_id
        self.title = title
        self.content = content
        self.user_id = user_id
        self.created_at = created_at
        self.updated_at = updated_at

    def transform(self):
        return {"data": 25000}
