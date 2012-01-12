#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       fasta.py

import yaml

class Color:
    def __init__(self):
        self.colors = {}

    def __iter__(self):
        #We are an iterable, so return our iterator
        for color in self.colors:
            yield color, self.colors[color]

    def load(self,file):


    def store(self,file):
        yaml.dump(self.colors)

