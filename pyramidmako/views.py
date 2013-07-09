#import datetime
#from pyramid.response import Response
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config, forbidden_view_config
from pyramid.security import remember, forget, NO_PERMISSION_REQUIRED

from .models import DBSession, HistoryModel, User
from nokaut.lib import nokaut_api, NokautError
from lib.allegro_modu1 import FindEroor, ConnectionError, result


@view_config(route_name='home', renderer='pyramidmako:templates/mytemplate_main.mako')
def my_view(request):
    return {}


@view_config(
    route_name='login',
    renderer='pyramidmako:templates/mytemplate_login.mako',
    permission=NO_PERMISSION_REQUIRED,
)
def log_view(request):
    if not request.method == 'POST':
        return {}
    login = request.POST.get('login')
    password = request.POST.get('password')
    if not login or not password:
        return {}
    in_database = DBSession.query(User).filter(login == User.name)\
        .filter(password == User.password).first()
    if in_database:
        headers = remember(request, login)
        return HTTPFound(location='/', headers=headers)
    return {}


@view_config(route_name='logout')
def logout_view(request):
    headers = forget(request)
    return HTTPFound(location=request.route_url('login'), headers=headers)


@view_config(
    route_name='register',
    renderer='pyramidmako:templates/mytemplate_register.mako',
    permission=NO_PERMISSION_REQUIRED,
)
def reg_view(request):
    if not request.method == 'POST':
        return {}
    login = request.POST.get('name')
    password = request.POST.get('pass')
    password2 = request.POST.get('pass2')
    if not login or not password or not password2 or password != password2:
        return {}
    in_database = DBSession.query(User).filter(login == User.name).first()
    if in_database:
        return {}
    model = User(login, password)
    DBSession.add(model)
    headers = remember(request, login)
    return HTTPFound(location='/', headers=headers)


@view_config(route_name='sec', renderer='pyramidmako:templates/mytemplate_res.mako')
def res_view(request):
    name = request.GET.get('product')

    if not name:
        url = request.route_url('home')
        return HTTPFound(location=url)

    response = {
        'name': name,
        'allegro': {
            'price': 0,
            'url': '',
            'status': '',
            'comparison': 'price'
        },
        'nokaut': {
            'price': 0,
            'url': '',
            'status': '',
            'comparison': 'price'
        },
        'status': ''
    }

    try:
        w1 = result(name)
    except (FindEroor, ConnectionError) as e:
        response['allegro']['status'] = e
    else:
        response['allegro']['status'] = ''
        response['allegro']['price'] = w1[0]
        response['allegro']['url'] = w1[1]
    try:
        w2 = nokaut_api(name, request.registry.settings.get('NokautKey'))
    except NokautError as e:
        response['nokaut']['status'] = e
    else:
        response['nokaut']['status'] = ''
        response['nokaut']['price'] = w2[0]
        response['nokaut']['url'] = w2[1]

    if response.get('allegro').get('status') and response.get('nokaut').get('status'):
        return response
    elif response.get('allegro').get('status') or response.get('allegro').get('status'):
        if response.get('allegro').get('status'):
            response['nokaut']['comparison'] = 'price win'
        else:
            response['allegro']['comparison'] = 'price win'
    else:
        if response['allegro']['price'] < response['nokaut']['price']:
            response['allegro']['comparison'] = 'price win'
        elif response['allegro']['price'] > response['nokaut']['price']:
            response['nokaut']['comparison'] = 'price win'

    model = HistoryModel(
        response['name'],
        response['allegro']['price'],
        response['allegro']['url'],
        response['nokaut']['price'],
        response['nokaut']['url'],
    )
    DBSession.add(model)
    return response
