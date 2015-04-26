#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Setup script for spyderplugins.p_autopep8
"""
from setuptools import setup, find_packages


def readme():
    return str(open('README.rst').read())


setup(
    name='spyderplugin.autopep8',
    namespace_packages=['spyderplugins'],
    version="0.1.0",
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    keywords=["spyder ide plugin addon"],
    url='https://github.com/Nodd/spyder_line_profiler',
    license='MIT',
    author='Joseph Martinot-Lagarde',
    author_email='contrebasse@gmail.com',
    description='A plugin to run the autopep8 python linter from within the spyder editor',
    long_description=readme(),
    install_requires=['autopep8', 'spyder>=2.3'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: X11 Applications :: Qt',
        'Environment :: Win32 (MS Windows)',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Widget Sets'])
