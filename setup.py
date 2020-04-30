#! /usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

setup(
    name='arc_code',
    version='0.0.0',
    description="",
    author='',
    author_email='',
    classifiers=[
        'Topic :: Scientific/Engineering',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Programming Language :: Python'
    ],
    packages=find_packages(),
    install_requires=[
        'tensorflow',
        'numpy',
    ]
)
