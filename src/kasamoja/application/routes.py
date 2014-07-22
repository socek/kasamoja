class Route(object):

    def __init__(self, app):
        self.app = app

    def add(self, route, url, *args, **kwargs):
        # kwargs['factory'] = 'edrna_backend.application.security.EntryFactory'
        return self.app.config.add_route(
            route,
            url,
            *args,
            **kwargs)


def make_routes(app):
    route = Route(app)
    route.add('homepage', '/')
