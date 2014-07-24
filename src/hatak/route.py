class Route(object):
    controller_values = [
        'permission',
        'attr',
        'renderer',
        'http_cache',
        'wrapper',
        'decorator',
        'mapper',
        'context',
        'request_type',
        'request_method',
        'request_param',
        'match_param',
        'containment',
        'xhr',
        'accept',
        'header',
        'path_info',
        'check_csrf',
        'physical_path',
        'effective_principals',
        'custom_predicates',
        'predicates',
    ]

    def __init__(self, app, prefix=None):
        self.app = app
        self.prefix = prefix

    @property
    def config(self):
        return self.app.config

    def add(self, controller_url, route, url, *args, **kwargs):
        self.config.add_route(
            route,
            url,
            *args,
            **kwargs)

        url = self.convert_url(controller_url)

        controller_class = self.config.maybe_dotted(url)
        kwargs = {}
        for name in self.controller_values:
            self.set_controller_config(kwargs, controller_class, name)

        self.config.add_view(url, route_name=route, **kwargs)

    def convert_url(self, url):
        return self.prefix + url

    def set_controller_config(self, kwargs, controller, name):
        value = getattr(controller, name, None)
        if value:
            kwargs[name] = value
