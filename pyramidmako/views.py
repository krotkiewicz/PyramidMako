#from pyramid.response import Response
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from lib.allegro_modu1 import FindEroor, ConnectionError, result
from nokaut.lib import nokaut_api, NokautError


@view_config(route_name='home', renderer='pyramidmako:templates/mytemplate_main.mako')
def my_view(request):
    return {}


@view_config(route_name='sec', renderer='pyramidmako:templates/mytemplate_res.mako')
def res_view(request):
        name = request.GET.get('product')

        if not name:
            url = request.route_url('home')
            return HTTPFound(location=url)

        response = {
            'name': '',
            'allegro': {
                'price': '',
                'url': '',
                'status': '',
                'comparison': 'price'
            },
            'nokaut': {
                'price': '',
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

        return response
