from os.path import dirname

from baelfire.recipe import Recipe
from bael.project.recipe import ProjectRecipe

from .tasks import (
    CreateDataDir,
    DevelopmentInit,
)


class BaelScriptRecipe(Recipe):

    def _add_path(self, name, dirname, basename):
        if dirname is None:
            self.paths[name] = basename
        else:
            self.paths[name] = ['%%(%s)s' % (dirname,), basename]

    def create_settings(self):
        self._add_path(
            'project:main',
            None,
            dirname(dirname(dirname(__file__))))
        self._add_path('project:src', 'project:main', 'src')
        self._add_path('baelscript', 'project:main', 'baelscript')
        self._add_path('baelscript:src', 'baelscript', 'src')
        self._add_path(
            'templates:frontend.ini',
            None,
            'frontend.ini')
        self._add_path('data', 'project:main', 'data')
        self._add_path('data:frontend.ini', 'data', 'frontend.ini')
        self._add_path('data:log', 'data', 'all.log')
        self._add_path('uwsgi:socket', None, '/tmp/uwsgi.socket')
        self._add_path('uwsgi:socket', None, '/tmp/uwsgi.socket')
        self._add_path(
            'venv:site-packages',
            'virtualenv_path',
            'lib/python3.4/site-packages/')

        self.settings['project:name'] = 'KasaMoja'
        self.settings['develop'] = True

    def final_settings(self):
        self._add_path('virtualenv_path', 'project:main', 'venv')

    def gather_recipes(self):
        self.add_recipe(ProjectRecipe())

    def gather_tasks(self):
        self.add_task(CreateDataDir)
        self.add_task(DevelopmentInit)
