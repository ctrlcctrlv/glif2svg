#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os
import glob

thelibFolder = os.path.dirname(os.path.realpath(__file__))
requirementPath = thelibFolder + '/requirements.txt'
install_requires = []
if os.path.isfile(requirementPath):
    with open(requirementPath) as f:
        install_requires = f.read().splitlines()

scripts = glob.glob("bin/*")

config = {
    'name': 'glif2svg',
    'author': 'Fredrick R. Brennan',
    'url': 'https://github.com/ctrlcctrlv/glif2svg',
    'description': 'Convert UFO .glif files to SVG',
    'long_description': open('README.md', 'r').read(),
    'license': 'MIT',
    'version': '1.0.3',
    'install_requires': install_requires,
    'classifiers': [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 4 - Beta"

    ],
    'package_dir': {'glif2svg': '.'},
    'packages': find_packages(),
    'scripts': scripts,
    'zip_safe': False
}

if __name__ == '__main__':
    setup(**config)
