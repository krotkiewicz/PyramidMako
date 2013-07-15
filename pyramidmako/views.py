#-*- coding: utf-8 -*-

import datetime
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.security import remember, forget

from .models import DBSession, History, User
from nokaut.lib import nokaut_api, NokautError
from lib.allegro_modu1 import FindEroor, ConnectionError, result
from FormValidate import FormReg, FormLog


@view_config(
    route_name='home',
    renderer='pyramidmako:templates/main.mako',
    permission='main'
)
def home_view(request):
    return {}


@view_config(
    route_name='login',
    renderer='pyramidmako:templates/login.mako',
)
def login_view(request):
    form = FormLog(request.POST)
    if not request.method == 'POST' or not form.validate():
        return dict(form=form)
    login = form.login.data
    password = form.pass1.data
    user = DBSession.query(User).filter(login == User.name) \
                                .filter(password == User.password).first()
    headers = remember(request, user.id_)
    return HTTPFound(location='/', headers=headers)


@view_config(route_name='logout', permission='user_login')
def logout_view(request):
    headers = forget(request)
    return HTTPFound(location=request.route_url('login'), headers=headers)


@view_config(
    route_name='history',
    renderer='pyramidmako:templates/history.mako',
    permission='user_login',
)
def history_view(request):
    history = DBSession.query(History)\
                       .filter(History.user_id_ == request.user.id_)\
                       .order_by(History.date.desc())
    return {'history': history}


@view_config(
    route_name='history_popular',
    renderer='pyramidmako:templates/history.mako',
    permission='user_login',
)
def history_popular_view(request):
    history = DBSession.query(History)\
                       .filter(History.user_id_ == request.user.id_)\
                       .order_by(History.count.desc())
    history = history[:3]
    return {'history': history}


@view_config(
    route_name='register',
    renderer='pyramidmako:templates/register.mako'
)
def register_view(request):
    form = FormReg(request.POST)
    if request.method != 'POST' or not form.validate():
        return dict(form=form)
    login = form.login.data
    password = form.pass1.data
    model = User(
        name=login,
        password=password,
    )
    DBSession.add(model)
    DBSession.flush()
    headers = remember(request, model.id_)
    return HTTPFound(location='/', headers=headers)


@view_config(
    route_name='result',
    renderer='pyramidmako:templates/result.mako',
    permission='user_login',
)
def result_view(request, _=None):
    name = request.GET.get('product')
    if not name:
        url = request.route_url('home')
        return HTTPFound(location=url)
    model = History()
    product = DBSession.query(History).filter(name == History.name).first()
    if product is not None:
        product.count += 1
        if (datetime.datetime.now() - product.date).days > 1:
            model = product
        else:
            return dict(entry=product)
    model.name = name
    name_encode = name.encode('utf-8')
    try:
        price, url = result(name_encode)
    except (FindEroor, ConnectionError) as e:
        model.status_allegro = str(e)
    else:
        model.status_allegro = ''
        model.price_allegro = price
        model.url_allegro = url
    try:
        price, url = nokaut_api(name_encode, request.registry.settings.get('nokaut.key'))
    except NokautError as e:
        model.status_nokaut = str(e)
    else:
        model.status_nokaut = ''
        model.price_nokaut = price
        model.url_nokaut = url

    model.user_id_ = request.user.id_
    DBSession.add(model)
    DBSession.flush()
    return dict(
        entry=model,
    )
