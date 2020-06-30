#!/usr/bin/env python

from setuptools import setup

setup(
      name='ftntlib',
      version='0.4.0.dev20',
      description='Python modules to interact with Fortinet products',
      install_requires=['requests','suds-jurko','lxml'],
      author='Original: Ashton Turpin, Maintainer: Jean-Pierre Forcioli, Contributors: Jeremy Parente',
      author_email='jpforcioli@fortinet.com, jparente@fortinet.com',
      url='https://fndn.fortinet.net',
      packages=['ftntlib'],
      )
