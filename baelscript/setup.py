# -*- encoding: utf-8 -*-
from setuptools import setup, find_packages

install_requires = [
    'bael.project==0.1',
]

if __name__ == '__main__':
    setup(name='baelscript',
          version='0.1',
          packages=find_packages('src'),
          install_requires=install_requires,
          zip_safe=False,
          )
