from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument

from repositories import NoteRepository
from util import auth, parse_params


class NotesResource(Resource):
    @staticmethod
    @auth()
    @parse_params(
        Argument("notebook_id", location="json", required=True, help="Notebook ID."),
        Argument("title", location="json", required=True, help="Note Title."),
        Argument("content", location="json", required=True, help="Note Content."),
    )
    @swag_from("../swagger/auth/register.yml")
    def post(user, notebook_id, title, content):
        note = NoteRepository.create(
            user=user,
            notebook_id=notebook_id,
            title=title,
            content=content
        )

        return jsonify({"data": note})

class NoteResource(Resource):
    @staticmethod
    @auth(id)
    @parse_params(
        Argument("title", location="json", required=True, help="Note Title."),
        Argument("content", location="json", required=True, help="Note Content.")
    )
    @swag_from("../swagger/auth/register.yml")
    def put(user, id, title, content):
        note = NoteRepository.update(
            user=user,
            id=id,
            title=title,
            content=content
        )

        return jsonify({"data": note})
