"""Setup tools for tvtagger,
"""

import os
import sys

# Ensure dir containing script is on PYTHONPATH
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

needed_pkgs = []

needed_pkgs.append("tvdb_api>=1.5")
needed_pkgs.append("tvnamer>=2")
needed_pkgs.append("pytagger>=0.5")
needed_pkgs.append("pytaglib>=0.3")

from setuptools import setup
setup(
name = 'tvtagger',
version="1.0",
author='Marcelo Origoni',
author_email='marcelo@origoni.com.ar',
url='http://marcelo.origoni.com.ar/',
description='Automatic TV episode tagger',

license='MIT',

long_description="""\
Automatically tags downloaded/recorded TV-episodes, by parsing filenames and
retrieving show-names from www.thetvdb.com

Now deals with files containing multiple: show.name.s01e01e02.avi, anime
files: [SomeGroup] Show Name - 102 [A1B2C3].mkv and better handles files
containing unicode characters.
""",

packages = ['tvtagger'],

entry_points = {
    'console_scripts': [
        'tvtagger = tvtagger.main:main',
    ],
},

install_requires = needed_pkgs,

classifiers=[
    "Environment :: Console",
    "Intended Audience :: End Users/Desktop",
    "License :: Unlicense",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Topic :: Multimedia",
    "Topic :: Utilities",
],
)
