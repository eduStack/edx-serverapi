#!/usr/bin/env python
from setuptools import setup

PACKAGES = [
    'api_manager',
    'api_manager.courses',
    'api_manager.groups',
    'api_manager.management',
    'api_manager.migrations',
    'api_manager.organizations',
    'api_manager.sessions',
    'api_manager.system',
    'api_manager.users',
    'projects',
]

setup(
    name='edx-serverapi',
    version='0.7.3',
    author='edX',
    url='http://github.com/edx/edx-serverapi',
    description='edx-serverapi',
    license='AGPL',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    packages=PACKAGES,
)
