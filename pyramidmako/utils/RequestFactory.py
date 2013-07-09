from pyramid.config import Configurator
from pyramid.request import Request
from pyramid.decorator import reify
from pyramid.security import authenticated_userid
from pyramidmako.models import DBSession, User


class MyRequest(Request):
    def __init__(self, *args, **kwargs):
        super(Request, self).__init__(*args, **kwargs)

    @reify
    def user(self):
        log = authenticated_userid(self)
        if log:
            return DBSession.query(User).filter(User.name == log).first()

config = Configurator()
config.set_request_factory(MyRequest)
