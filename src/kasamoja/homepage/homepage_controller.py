from kasamoja.application.controller import Controller


class HomepageController(Controller):
    renderer = 'homepage.jinja2'

    def make(self):
        return {
            'szef': 10,
        }
