from hatak.route import Route


def make_routes(app):
    route = Route(app, 'kasamoja.')
    route.add(
        'homepage.homepage_controller.HomepageController',
        'homepage',
        '/')
