#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       uniprot.py


class Uniprot:

    def __init__(self):
        self.ac = {}

    def __iter__(self):
        #We are an iterable, so return our iterator
        for i in self.ac:
            yield i, self.ac[i]

    def load(self,uniprot_file, organism):
        for line in open(uniprot_file, "r"):
            if line.startswith("ID"):
                line = line.rstrip().split()
                id = line[1]
                if id.split("_")[1] == "HUMAN":
                    self.ac[id] = []
            elif line.startswith("AC"):
                line = line.rstrip().split()
                ac = line[1].split(";")
                if self.ac.has_key(id):
                    for i in ac:
                        if len(i) > 0:
                            self.ac[id].append(i)
