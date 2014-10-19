#!/usr/bin/env python

"""Main tvtagger utility functionality
"""

import os
import argparse
import sys
import tvdb_api
import tvnamer.utils
import taglib


def read_directory(dir, rec):
    files = []
    nodes = os.listdir(dir)

    for node in nodes:
        if os.path.isdir(dir + '/' + node):
            if rec == 1:
                children = read_directory(dir + '/' + node, rec)
                for child in children:
                    files.append(child)
        else:
            files.append(dir + '/' + node)
    return files


def main():
    parser = argparse.ArgumentParser(description='Automatic TV episode tagger')
    parser.add_argument('-f', dest='file', nargs='?', default=' ', help='file to parse')
    parser.add_argument('-d', dest='dir', nargs='?', default=' ', help='directory to parse')
    parser.add_argument('-r', '--recursive', dest='rec', nargs='?', const=1, default=0, help='Parse directory recursively')
    parser.add_argument('-e', '--erase', dest='erase', nargs='?', const=1, default=0, help='Erase all existing tags')
    parser.add_argument('-n', '--no-tagging', dest='tag', nargs='?', const=0, default=1, help='Don\'t tag files')
    parser.add_argument('-c', '--comment', dest='comment', nargs='?', default='',help='Comment to be saved in the comment frame')

    args = parser.parse_args()

    files = []

    if args.dir != ' ':
        if os.path.isdir(args.dir):
            files = read_directory(args.dir, args.rec)
        else:
            print 'Directory Doesn\'t Exists'
    elif args.file != ' ':
        if os.path.isfile(args.file):
            files.append(args.file)
        else:
            print 'File Doesn\'t Exists'
    else:
        print 'Please input a file or directory to parse'
        quit()

    t = tvdb_api.Tvdb()

    for fil in files:
        f = taglib.File(fil)

        if args.erase == 1:
            for tag in f.tags:
                del f.tags[tag]

        ep = tvnamer.utils.FileParser(fil).parse()
        ep.populateFromTvdb(t)
        season = t[ep.seriesname][ep.seasonnumber]

        full_title_txt = str(ep.seriesname) + " - S" + "{0:02d}".format(ep.seasonnumber) + 'E' + "{0:02d}".format(ep.episodenumbers[0]) + " - " + str(ep.episodename[0])

        series_tag = 'ALBUM'
        title_tag = 'TITLE'
        comment_tag = 'COMMENT'
        track_tag = 'TRACKNUMBER'

        if args.comment != '':
            f.tags[comment_tag] = [args.comment]

        f.tags[series_tag] = [str(ep.seriesname) + " - S" + "{0:02d}".format(ep.seasonnumber)]
        f.tags[title_tag] = [full_title_txt]
        f.tags[track_tag] = ["{0:02d}".format(ep.seasonnumber) + "/" + "{0:02d}".format(len(season.keys()))]

        if args.tag == 1:
            ret = f.save()
            print 'File:' + fil + ' Processed: ' + full_title_txt