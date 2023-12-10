from django.db import models

class Board(models.Model):
    name = models.CharField(max_length=255)
    tiles = models.TextField()
    owner = models.CharField(max_length=255)