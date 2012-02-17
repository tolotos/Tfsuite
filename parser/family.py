#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       fasta.py

import os

def read_family(source, obj=None):
    family2arrangement = {}

    try:
        basename = os.path.basename(source)

        with open(source, "r") as file:
            for line in file.readlines():
                line = line.split()
                family2arrangement[line[0]] = line[1]
            return family2arrangement
    
    except IOError:
        print "File does not exit!"