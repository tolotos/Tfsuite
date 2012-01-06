#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       domains.py


from Tfsuite.Classes.protein import Protein

class Arangements:

    def __init__(self):
        self.proteins = {}

    def __iter__(self):
        #We are an iterable, so return our iterator
        for i in self.proteins:
            yield self.proteins[i]

    def load(self, file):
        file = open(file, "r").readlines()
        for line in file:
            line = line.rstrip().split()
            id = line[0].split("|")
            species, gene_name = id[0], id[1]
            domains = line[1:]
            self.proteins[gene_name] = Protein(gene_name)
            self.proteins[gene_name].domains = domains
            self.proteins[gene_name].species = species
