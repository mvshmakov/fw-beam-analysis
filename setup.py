#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

with open('README.md') as f:
    long_description = '\n' + f.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='fw-beam-analysis',
    version='0.1',
    description='Perform preliminary fw-beam interaction modelling.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Shmakov Maxim',
    author_email='mvshmakovmv@gmail.com',
    python_requires='>=3.6.0',
    url='https://github.com/mvshmakov/fw-beam-analysis',
    packages=find_packages(),
    install_requires=required,
    include_package_data=True,
    license='WTFPL',
    classifiers=[
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Environment :: MacOS X',
        'Environment :: Win32 (MS Windows)',
        'Environment :: X11 Applications :: Qt',
        'Intended Audience :: Science/Research',
        'License :: Free For Educational Use',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)
