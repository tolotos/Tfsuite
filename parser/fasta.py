#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       fasta.py

def read_fasta(source, obj=None):
    SG = {}
    try:
        with open(source, "r") as file:
            for line in file.readlines():
                if line[0] == ">":
                    name = line[1:].rstrip()
                    if name[4] == "|":  # Account for species
                        name = name.split("|")[1]
                        SG[name] = ""
                    else:
                        SG[name] = ""
                else:
                    SG[name] += line.rstrip()
            return SG
    except IOError:
        print "File does not exit!"

def write_fasta(sequences):
    pass
