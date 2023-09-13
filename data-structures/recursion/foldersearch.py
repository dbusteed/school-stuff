#!/usr/bin/env python3
import os
import fnmatch


IMAGE_GLOBS = {
    '*.png',
    '*.jpg',
    '*.gif',
}

def is_image(filename):
    '''
    Returns True if the given filename matches one of the IMAGE_GLOBS patterns.
    Just check the filename itself (don't inspect the file contents).
    '''

    for glob in IMAGE_GLOBS:
        if fnmatch.fnmatch(filename.lower(), glob):
            return True

    return False


def find_images(rootpath, subpath=''):
    '''
    Generator function that returns the images in the given directory
    tree (includes subdirectories). The returned image paths are relative to
    the given path.

    Use os.listdir() to get the files in the current directory (don't use os.walk
    or glob.glob).
    '''

    path = os.path.join(rootpath, subpath)

    if os.path.isdir(path):
        for item in os.listdir(path):
            yield from find_images(rootpath, os.path.join(subpath, item))

    else:
        if is_image(path):
            yield path
