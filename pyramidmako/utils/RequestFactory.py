from pyramid.config import Configurator
from pyramid.request import Request
from pyramid.decorator import reify
from pyramid.security import authenticated_userid
from pyramidmako.models import DBSession, User


class MyRequest(Request):

    @reify
    def user(self):
        id = authenticated_userid(self)
        if id:
            return DBSession.query(User).filter(User.id_ == id).first()
