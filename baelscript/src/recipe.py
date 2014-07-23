from os.path import dirname

from baelfire.recipe import Recipe
from bael.project.recipe import ProjectRecipe

from .tasks import (
    CreateDataDir,
    Serve,
    MigrationVersioning,
    Migration,
)

from .frontendtask import FrontendIni


class BaelScriptRecipe(Recipe):

    def create_settings(self):
        self.set_path(
            'project:main',
            None,
            dirname(dirname(dirname(__file__))))
        self.set_path('project:src', 'project:main', 'src')
        self.set_path('baelscript', 'project:main', 'baelscript')
        self.set_path('baelscript:src', 'baelscript', 'src')
        self.set_path(
            'templates:frontend.ini',
            None,
            'frontend.ini')
        self.set_path('data', 'project:main', 'data')
        self.set_path('data:frontend.ini', 'data', 'frontend.ini')
        self.set_path('data:log', 'data', 'all.log')
        self.set_path('uwsgi:socket', None, '/tmp/uwsgi.socket')
        self.set_path('uwsgi:socket', None, '/tmp/uwsgi.socket')
        self.set_path(
            'venv:site-packages',
            'virtualenv_path',
            'lib/python3.4/site-packages/')

        self.set_path('kmflags', 'data', 'flags')
        self.set_path('flags:dbversioning', 'kmflags', 'versioning.flag')
        self.set_path('flags:dbmigration', 'kmflags', 'dbmigration.flag')

        self.set_path('migration:main', 'project:main', 'migrations')
        self.set_path('migration:manage', 'migration:main', 'manage.py')
        self.set_path('migration:versions', 'migration:main', 'versions')

        self.settings['project:name'] = 'KasaMoja'
        self.settings['develop'] = True

    def final_settings(self):
        self.set_path('virtualenv_path', 'project:main', 'venv')

    def gather_recipes(self):
        self.add_recipe(ProjectRecipe())

    def gather_tasks(self):
        self.add_task(CreateDataDir)
        self.add_task(FrontendIni)
        self.add_task(Serve)
        self.add_task(MigrationVersioning)
        self.add_task(Migration)
