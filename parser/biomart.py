#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       biomart.py


class Biomart:
    def __init__(self):
        self.ids = {}

    def __iter__(self):
        #We are an iterable, so return our iterator
        for i in self.seqs:
            yield i, self.seqs[i]

    def load(self,file):
        lines = open(file, "r").readlines()
        for line in lines:
            if line.startswith("#"):
                continue
            elif line.startswith("Ensemble"):
                continue
            else:
                line = line.rstrip().split(",")
                gene_name = line[0]
                if len(line[1]) == 0:
                    uniprot_id = None
                else:
                    uniprot_id = line[1]
                associated_name = line[2]
                self.ids[gene_name] = [uniprot_id,associated_name]
