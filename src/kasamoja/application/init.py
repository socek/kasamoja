from pyramid.config import Configurator
from smallsettings import Factory

from .routes import make_routes


class Application(object):

    """Prepering and configuring project."""

    def __call__(self, settings={}):
        self.settings = self.generate_settings(settings)
        # self.initialize_logging()
        self.create_config()
        self.config.scan('kasamoja')
        # self.connect_database()
        # self.mail_access()
        # self.config.include('pyramid_jinja2')
        self.config.registry['settings'] = self.settings
        # self.config.registry['jinja2'] = self.config.get_jinja2_environment()

        # self.config.add_request_method(self.get_user, 'user', reify=True)
        # self.config.add_request_method(self.unique_num, 'unique_num',
        #                                property=True)
        # self.config.add_request_method(self.add_s3, 's3', reify=True)

        return self.config.make_wsgi_app()

    def generate_settings(self, settings):
        settings, paths = self.get_settings(settings)
        merged = settings.merged(paths)
        return merged.to_dict()

    @classmethod
    def get_settings(cls, settings={}):
        factory = Factory('kasamoja.application')
        settings, paths = factory.make_settings(
            settings=settings,
            additional_modules=[
                ('local', False),
            ])
        return settings, paths

    def create_config(self):
        # authentication_policy = self.create_authentication_policy()
        # authorization_policy = ACLAuthorizationPolicy()

        self.config = Configurator(
            settings=self.settings,
            # authentication_policy=authentication_policy,
            # authorization_policy=authorization_policy,
            # root_factory=EntryFactory,
            # session_factory=self.create_session(),
        )
        self.make_pyramid_includes()
        make_routes(self)
        # subscriber(self.config)
        # self.config.add_renderer('json', json_renderer)

    def make_pyramid_includes(self):
        for include in self.settings['includes']:
            self.config.include(include)

main = Application()
