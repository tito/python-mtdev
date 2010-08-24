#!/usr/bin/env python

from distutils.core import setup
import mtdev

setup(name='python-mtdev',
      version=mtdev.__version__,
      description='Python bindings for libmtdev',
      author='Mathieu Virbel',
      author_email='mathieu@pymt.eu',
      url='http://github.com/tito/python-mtdev',
      py_modules=['mtdev'],
)

