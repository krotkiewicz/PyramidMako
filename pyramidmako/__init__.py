from pyramid.config import Configurator
from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from sqlalchemy import engine_from_config

from .models import DBSession, User
from utils.RequestFactory import MyRequest


def groupfinder(log, request):
    user = DBSession.query(User).filter(User.name == log).first()
    return [g.groupname for g in user.mygroups]


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    authn_policy = AuthTktAuthenticationPolicy('seekrit', hashalg='sha512')
    authz_policy = ACLAuthorizationPolicy()
    config = Configurator(settings=settings, request_factory=MyRequest)
    config.set_default_permission('view')
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('sec', '/res')
    config.add_route('register', '/reg')
    config.add_route('login', '/log')
    config.add_route('logout', '/logout')
    config.scan()
    return config.make_wsgi_app()
