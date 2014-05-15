from distutils.version import StrictVersion
import os
from setuptools import setup
# from tests import PyTest
import sys

deps = ["sphinx"]

if sys.version_info[:2] == (2, 6):
    deps.append('argparse')

setup(
    name='sphinx-argparse',
    version='0.1.10',
    packages=[
        'sphinxarg',
    ],

    url='',
    license='MIT',
    author='Aleksandr Rudakov',
    author_email='ribozz@gmail.com',
    description='Sphinx extension that automatically document argparse commands and options',
    long_description='',
    install_requires=deps,

    extras_require={
        'dev': ['pytest', 'sphinx_rtd_theme', 'sphinx'],
    }
)
