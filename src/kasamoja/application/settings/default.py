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

    settings['db:url'] = (
        '%(db:type)s://%(db:login)s:%(db:password)s@%(db:host)s:%(db:port)s'
        '/%(db:db)s')
    settings['db:type'] = 'postgresql'
    settings['db:login'] = 'develop'
    settings['db:password'] = 'develop'
    settings['db:host'] = 'localhost'
    settings['db:port'] = '5432'
    settings['db:db'] = 'develop'

    paths['data'] = 'data'
    paths['frontend'] = ['%(data)s', 'frontend.ini']
    paths['logging:config'] = '%(frontend)s'
