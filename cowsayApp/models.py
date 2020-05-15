from django.db import models

# Create your models here.
class WhatTheCowsay(models.Model):
    what_does_the_cowsay = models.CharField(max_length=142)
    def __str__(self):
        return self.what_does_the_cowsay