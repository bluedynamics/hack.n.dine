# -*- coding: utf-8 -*-
"""Installer for the hack.n.dine package."""

from setuptools import find_packages
from setuptools import setup


long_description = (
    open('README.rst').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.rst').read()
    + '\n' +
    open('CHANGES.rst').read()
    + '\n')


setup(
    name='hack.n.dine',
    version='0.1',
    description="hack'n'dine page",
    long_description=long_description,
    # Get more from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 5",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ],
    keywords='Plone Python',
    author='Robert Niederreiter',
    author_email='office@squarewave.at',
    url='http://pypi.python.org/pypi/hack.n.dine',
    license='GPL',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['hack', 'hack.n'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'plone.api',
        'setuptools',
        'z3c.jbot',
    ],
    extras_require={
        'test': [
            'plone.app.testing',
            'plone.app.robotframework',
        ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
