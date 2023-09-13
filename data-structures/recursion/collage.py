#!/usr/bin/env python3
import argparse
import os
from PIL import Image               # pip3 install pillow
from foldersearch import find_images
# from random import shuffle
from math import ceil


THUMNAILS_PER_ROW = 4
THUMBNAIL_WIDTH = 200
THUMBNAIL_HEIGHT = 200



########################
###  Main program

def main(args):
    '''
    Creates a collage by recursively finding images in a directory path.
    '''
    # find the images
    imgpaths = []
    for filepath in find_images(os.path.abspath(args.searchpath)):
        imgpaths.append(filepath)
    if len(imgpaths) == 0:
        print('No images found')
        return

    # create a new, RGB image
    collage = Image.new('RGB', [(THUMBNAIL_WIDTH * THUMNAILS_PER_ROW), (THUMBNAIL_HEIGHT * (ceil(len(imgpaths)/4)))])

    # shuffle(imgpaths)

    # place the thumbnails
    for imgnum, imgpath in enumerate(imgpaths):
        print(f'=> {imgpath}')
        
        # open the image and convert to RGB
        im = Image.open(imgpath)
        im.convert('RGB')

        # resize to a thumnail
        im = im.resize([THUMBNAIL_WIDTH, THUMBNAIL_HEIGHT])

        # paste in next position
        collage.paste(im, [((imgnum % THUMNAILS_PER_ROW) * 200), ((imgnum // THUMNAILS_PER_ROW) * 200)])

    # save the image
    print(f'\nWriting {args.collage}')
    collage.save(args.collage)


########################
###  Bootstrap

parser = argparse.ArgumentParser(description='Creates a collage by recursively finding images in a directory path')
parser.add_argument('collage', help='file name to write the collage to')
parser.add_argument('searchpath', help='directory path to start searching')
args = parser.parse_args()
main(args)
