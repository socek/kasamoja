from pyramid.response import Response
from pyramid.view import view_config as ctrl


@ctrl(route_name='homepage')
class Homepage(object):

    def __init__(self, request):
        self.request = request

    def __call__(self):
        return Response("This is homepage!")
