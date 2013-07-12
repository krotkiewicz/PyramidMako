import datetime
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from pyramid.security import remember, forget

from .models import DBSession, HistoryModel, User
from nokaut.lib import nokaut_api, NokautError
from lib.allegro_modu1 import FindEroor, ConnectionError, result
from FormValidate import FormReg, FormLog

@view_config(
    route_name='home',
    renderer='pyramidmako:templates/main.mako',
    permission='main'
)
def my_view(request):
    return {}


@view_config(
    route_name='login',
    renderer='pyramidmako:templates/login.mako',
)
def log_view(request):
    form = FormLog(request.POST)
    if not request.method == 'POST' or not form.validate():
        return dict(form=form)
    login = form.login.data
    password = form.pass1.data
    if not login or not password:
        return dict(form=form)
    in_database = DBSession.query(User).filter(login == User.name) \
        .filter(password == User.password).first()
    if in_database:
        headers = remember(request, in_database.id_)
        return HTTPFound(location='/', headers=headers)
    return dict(form=form)


@view_config(route_name='logout', permission='user_log')
def logout_view(request):
    headers = forget(request)
    return HTTPFound(location=request.route_url('login'), headers=headers)


@view_config(
    route_name='history',
    renderer='pyramidmako:templates/history.mako',
    permission='user_log',
)
def history_view(request):
    history = DBSession.query(
        HistoryModel).filter(HistoryModel.user_id_ == request.user.id_).order_by(HistoryModel.date.desc())
    return {'history': history}


@view_config(
    route_name='history_popular',
    renderer='pyramidmako:templates/history.mako',
    permission='user_log',
)
def history_popular_view(request):
    history = DBSession.query(
        HistoryModel).filter(HistoryModel.user_id_ == request.user.id_).order_by(HistoryModel.count.desc())
    history = history[:3]
    return {'history': history}


@view_config(
    route_name='register',
    renderer='pyramidmako:templates/register.mako'
)
def reg_view(request):
    form = FormReg(request.POST)
    if request.method != 'POST' or not form.validate():
        return dict(form=form)
    login = form.login.data
    password = form.pass1.data
    password2 = form.pass2.data
    if not login or not password or not password2 or password != password2:
        return {}
    in_database = DBSession.query(User).filter(login == User.name).first()
    if in_database:
        return {}
    model = User(
        name=login,
        password=password,
    )
    DBSession.add(model)
    DBSession.flush()
    headers = remember(request, model.id_)
    return HTTPFound(location='/', headers=headers)


@view_config(
    route_name='sec',
    renderer='pyramidmako:templates/res.mako',
    permission='user_log',
)
def res_view(request):
    name = request.GET.get('product')
    if not name:
        url = request.route_url('home')
        return HTTPFound(location=url)
    model = HistoryModel()
    product = DBSession.query(HistoryModel).filter(name == HistoryModel.name).first()
    if product is not None:
        product.count += 1
        if (datetime.datetime.now() - product.date).days > 1:
            model = product
        else:
            return dict(entry=product)
    model.name = name
    try:
        w1 = result(name)
    except (FindEroor, ConnectionError) as e:
        model.status_allegro = str(e)
    else:
        model.status_allegro = ''
        model.price_allegro = w1[0]
        model.url_allegro = w1[1]
    try:
        w2 = nokaut_api(name, request.registry.settings.get('NokautKey'))
    except NokautError as e:
        model.status_nokaut = str(e)
    else:
        model.status_nokaut = ''
        model.price_nokaut = w2[0]
        model.url_nokaut = w2[1]
    model.user_id_ = request.user.id_
    if model.status_allegro and model.status_nokaut:
        pass
    elif model.status_allegro or model.status_nokaut:
        if model.status_allegro:
            model.comparison_nokaut = 'price win'
        else:
            model.comparison_allegro = 'price win'
    else:
        if model.price_allegro < model.price_nokaut:
            model.comparison_allegro = 'price win'
        elif model.price_allegro > model.price_nokaut:
            model.comparison_nokaut = 'price win'

    DBSession.add(model)
    DBSession.flush()
    return dict(
        entry=model,
    )
