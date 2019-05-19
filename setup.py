#!/usr/bin/env python3

"""Test, build, or install the Sitewatch package.

Run tests:
  python setup.py test

Build and install:
  python setup.py build && python setup.py install
"""

from distutils.util import convert_path
from setuptools import setup

VER_FILEPATH = convert_path('sitewatch/version.txt')
with open(VER_FILEPATH) as file:
    __version__ = file.read()

setup(
    name='Sitewatch',
    description='A service that watches a website and notifies you when it changes',
    url='https://github.com/texruska/Sitewatch',
    author='Steven Burnett',
    license='GPLv3',
    author_email='texruska@users.noreply.github.com',
    packages=['sitewatch'],
    setup_requires=['pytest-runner'],
    tests_require=[
        'coverage',
        'pytest',
        'pytest-cov',
        'pytest-pylint'
    ],
    version=__version__,
    zip_safe=False
)
