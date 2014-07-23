# -*- encoding: utf-8 -*-
from setuptools import setup, find_packages

install_requires = [
    'pyramid',
    'sqlalchemy',
    'sqlalchemy-migrate',
    'pastedeploy',
    'waitress',
    'smallsettings',
    'pyramid_debugtoolbar',
    'pyramid_jinja2',
    'psycopg2',
    'pyramid_beaker',
    'sqlalchemy-migrate',
]

if __name__ == '__main__':
    setup(name='KasaMoja',
          version='0.1',
          packages=find_packages('src'),
          package_dir={'': 'src'},
          install_requires=install_requires,
          include_package_data=True,
          entry_points=(
              '[paste.app_factory]\n'
              'main = kasamoja.application.init:main\n'),
          )
