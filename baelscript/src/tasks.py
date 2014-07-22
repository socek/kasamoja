from os import mkdir, path

from baelfire.task import Task
from baelfire.template import TemplateTask
from baelfire.dependencies import (
    AlwaysRebuild,
    FileDoesNotExists,
)


class CreateDataDir(Task):
    name = 'Creating data directory'
    path = '/kasamoja/data'

    directorie_names = [
        'data',
    ]

    @property
    def directories(self):
        for name in self.directorie_names:
            yield self.paths[name]

    def generate_dependencies(self):
        for directory in self.directories:
            self.add_dependecy(FileDoesNotExists(directory))

    def make(self):
        for directory in self.directories:
            if not path.exists(directory):
                mkdir(directory)


class FrontendIni(TemplateTask):
    name = 'Creating frontend.ini file'
    path = '/kasamoja/frontend.ini'

    def generate_links(self):
        super().generate_links()
        self.add_link(CreateDataDir)

    def get_output_file(self):
        return self.paths['data:frontend.ini']

    def get_template_path(self):
        return self.paths['templates:frontend.ini']


class Serve(Task):
    name = 'Run development server'
    path = '/kasamoja/serve'

    def generate_dependencies(self):
        self.add_dependecy(AlwaysRebuild())

    def generate_links(self):
        self.add_link(FrontendIni)
        self.add_link('bael.project.virtualenv:Develop')

    def make(self):
        self.command(['pserve %(data:frontend.ini)s --reload' % (self.paths)])
