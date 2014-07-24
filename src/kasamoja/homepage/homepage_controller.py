from hatak.controller import DatabaseController


class HomepageController(DatabaseController):
    renderer = 'homepage.jinja2'

    def make(self):
        return {
            'szef': 10,
        }
