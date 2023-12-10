#!/usr/bin/python3

from play.models import Board

b = Board()
b.name = 'cool game'
b.tiles = 'something|another thing|blah blah|a longer named one|yup'
b.owner = 'site_admin'
b.save()

b = Board()
b.name = 'test board'
b.tiles = 'number one|number two|the other one|and the other one|test test!'
b.owner = 'site_admin'
b.save()

b = Board()
b.name = 'favorite snacks'
b.tiles = 'chicken|carrots|bananas|raisins|cookies'
b.owner = 'site_admin'
b.save()