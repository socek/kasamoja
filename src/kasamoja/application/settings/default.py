def make_settings(settings, paths):
    settings['includes'] = [
        'pyramid_debugtoolbar',
        'pyramid_beaker', ]
    settings['jinja2.directories'] = 'kasamoja:templates'
    settings['authentication_debug'] = False
    settings['session.type'] = 'file'
    settings['session.key'] = 'needtochangethis'
    settings['session.secret'] = 'needtochangethistoo'
    settings['session.cookie_on_exception'] = True

    paths['session.data_dir'] = ["%(data)s", 'sessions', 'data']
    paths['session.lock_dir'] = ["%(data)s", 'sessions', 'lock']

    paths['data'] = 'data'
    paths['frontend'] = ['%(data)s', 'frontend.ini']
    paths['logging:config'] = '%(frontend)s'

    paths['sqlite_db'] = ["%(data)s", 'database.db']
    settings['db:url'] = 'sqlite:///%(sqlite_db)s' % paths
