""" Defines the User repository """

import random
import string

import bcrypt
from sqlalchemy.orm import load_only
from werkzeug.exceptions import Forbidden, UnprocessableEntity

from models import User


class UserRepository:
    @staticmethod
    def create(username, email, password):
        """ Create a new user """

        try:
            exists_username = bool(User.query.filter_by(username=username).first())
        except Exception as e:
            return {"err": str(e)}

        exists_email = bool(User.query.filter_by(email=email).first())
        if exists_username:
            raise UnprocessableEntity(description="USER_USERNAME_EXISTS")

        if exists_email:
            raise UnprocessableEntity(description="USER_EMAIL_EXISTS")

        hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        secret = "".join(
            random.choices(
                string.ascii_uppercase + string.ascii_lowercase + string.digits, k=16
            )
        )

        user = User(username=username, email=email, password=hashed, secret=secret)

        user.save()

        ret = {"user": user.serialized(), "token": user.generateToken()}

        return ret

    @staticmethod
    def authenticate(username, password):
        """ Authenticate a user """

        user = User.query.filter_by(username=username).first()

        if user:
            if bcrypt.checkpw(password.encode("utf-8"), user.json["password"]):
                return {"user": user.serialized(), "token": user.generateToken()}
            else:
                raise Forbidden(description="USER_PASSWORD_INCORRECT")
        else:
            raise Forbidden(description="USER_USER_NOT_FOUND")

    @staticmethod
    def refresh(user):
        """ Refresh user token """

        user = User.query.filter_by(username=user.json["username"]).first()

        return {"user": user.serialized(), "token": user.generateToken()}
