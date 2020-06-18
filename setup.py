# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in atc_app/__init__.py
from atc_app import __version__ as version

setup(
	name='atc_app',
	version=version,
	description='atc-app',
	author='frappe',
	author_email='atcqw@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
