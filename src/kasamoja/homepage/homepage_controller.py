from kasamoja.application.controller import DatabaseController as Controller


class HomepageController(Controller):
    renderer = 'homepage.jinja2'

    def make(self):
        return {
            'szef': 10,
        }
