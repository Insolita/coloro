#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

import coloro

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='coloro',
    version=coloro.__version__,
    packages=find_packages(),
    install_requires=['clipboard>=0.0.3'],
    description='A console tool for output text with highlighted hex colors',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Insolita',
    author_email='webmaster100500@ya.ru',
    url='https://github.com/Insolita/coloro',
    download_url='https://github.com/Insolita/coloro/tarball/master',
    license='MIT',
    keywords='terminal, color, term_color, clipboard, console',
    classifiers=[
        'Programming Language :: Python :: 3',
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.4',
    entry_points={
        'console_scripts': [
            'coloro = coloro.main:main'
        ]
    },
)
