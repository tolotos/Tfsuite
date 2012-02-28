#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       xdom.py

from Tfsuite.core.domain import Domain


def read_xdom(xdom, evalue):
    prots = {}
    with open(xdom, "r") as xdom:
        for line in xdom.readlines():
            line = line.rstrip().split()
            if len(line) > 0:
                if line[0].startswith(">"):
                    gene_name = line[0].split("|")[1]
                    prots[gene_name] = []
                else:
                    if float(line[3]) <= float(evalue):
                        domain = Domain(line[2], line[0], line[1], line[3])
                        prots[gene_name].append(domain)
    return prots
