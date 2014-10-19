# `tvtagger`

`tvtagger` is a utility which to tags video files (by retrieving the episode name using data from [`tvdb_api`](http://github.com/dbr/tvdb_api))

## To install

Download the latest version of the code, either from <http://github.com/marceloOrigoni/tvtagger/tarball/master> or by running:

    git clone git://github.com/marceloOrigoni/tvtagger.git

..then `cd` into the directory, and run:

    sudo python setup.py install

## Basic usage

From the command line, simply run:

    tvtagger -f the.file.s01e01.avi
    tvtagger -d the.folder

## Command line arguments

There are various flags you can use with `tvtagger`, run..

    tvtagger --help

..to see them, and a short description of each.

  `-r`, `--recursive` Parse directory recursively
  
  `-e`, `--erase` Erase all existing tags
  
  `-n`, `--no-tagging` Don't tag files
  
  `-c`, `--comment` [COMMENT]  Comment to be saved in the comment frame