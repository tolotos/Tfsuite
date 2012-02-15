#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       xdom.py


def read_xdom(xdom):
    prots = {}
    with open(xdom, "r") as xdom:
        for line in xdom.readlines():
            line = line.rstrip().split()
            if len(line) > 0:
                if line[0].startswith(">"):
                    gene_name = line[0].split("|")[1]
                    prots[gene_name] = []
                else:
                    prots[gene_name].append(",".join(line[0:3]))
    return prots
