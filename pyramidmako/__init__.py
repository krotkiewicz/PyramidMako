from pyramid.config import Configurator
from pyramid.security import Deny, Allow, Everyone, Authenticated
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from sqlalchemy import engine_from_config

from .models import DBSession, Base,  User
from utils.RequestFactory import MyRequest
from .views import logout_view


class RootFactory(object):
    __acl__ = [
        (Deny, Authenticated, 'view'),
        (Allow, Everyone, ('view', 'main')),
        (Allow, Authenticated, ('main', 'user_log')),
    ]

    def __init__(self, request):
        pass


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    authentication = AuthTktAuthenticationPolicy('secretstring')
    authorization = ACLAuthorizationPolicy()
    config = Configurator(
        settings=settings,
        request_factory=MyRequest,
        root_factory=RootFactory
    )
    config.set_default_permission('view')
    config.set_authentication_policy(authentication)
    config.set_authorization_policy(authorization)
    config.add_forbidden_view(view=logout_view)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('sec', '/res')
    config.add_route('register', '/reg')
    config.add_route('login', '/log')
    config.add_route('logout', '/logout')
    config.add_route('history', '/his')
    config.scan()
    return config.make_wsgi_app()
