#!/usr/bin/env python

# Bootstrap installation of Distribute
from distribute_setup import use_setuptools
use_setuptools()

import os.path

from setuptools import setup

def whole_tree(prefix, path):
    files = []
    for f in (f for f in os.listdir(os.path.join(prefix, path))):
        new_path = os.path.join(path, f)
        if os.path.isdir(os.path.join(prefix, new_path)):
            files.extend(whole_tree(prefix, new_path))
        else:
            files.append(new_path)
    return files

setup(
    name='DjangoSkel',
    version='0.1.3',
    author='Radek Czajka',
    author_email='radek.czajka@gmail.com',
    packages=['djangoskel'],
    package_data={'djangoskel': whole_tree(
                os.path.join(os.path.dirname(__file__), 'djangoskel'),
                'skel')},
    scripts=['bin/djangoskel'],
    url='https://github.com/yappari/djangoskel',
    license=open('LICENSE').read(),
    description="Django project skeleton",
    long_description=open('README.rst').read(),
    install_requires = [
        'skeleton==0.6-ypr',
    ],
    dependency_links = [
       'http://github.com/yappari/skeleton/tarball/master#egg=skeleton-0.6-ypr',
    ],
)
