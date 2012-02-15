#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       domains.py


def read_arangement(source):
        ARAG = {}
        with open(source, "r") as source:
            for line in source.readlines():
                line = line.rstrip().split()
                id = line[0].split("|")
                species, gene_name = id[0], id[1]
                domains = line[1:]
                ARAG[id[1]] = [species, domains]
        return ARAG
