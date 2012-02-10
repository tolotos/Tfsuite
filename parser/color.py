#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       fasta.py

import yaml
import random

class Color:
    def __init__(self):
        self.rgb = {}
        self.hex = {}
    def __iter__(self):
        #We are an iterable, so return our iterator
        for color in self.rgb:
            yield color, self.rgb[color]

    def load(self,file):
        f = open(file, "r")
        self.rgb = yaml.load(f)
        f.close()

    def store(self,file):
        f = open(file, "w")
        yaml.dump(self.rgb,f)
        f.close()

    #def lighter():

    #def darker()

    def rgb_to_hex(self):
        #Needs some more work!
        for i in self.rgb:
            self.hex[i] = []
            for int in self.rgb[i]:
                self.hex[i].append(hex(int))

    def random_rgb(self):
        color = [0,0,0]
        for i in range(3):
            color[i] = random.randint(0,255)
        return color
