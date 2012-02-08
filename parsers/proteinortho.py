#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       proteinortho.py

import os
from Tfsuite.Classes.cluster import Cluster

class ProteinOrtho:

    def __init__(self):
        self.clusters = {}

    def __iter__(self):
        #We are an iterable, so return our iterator
        for i in self.clusters:
            yield self.clusters[i]

    def load(self, file):
        basename = os.path.basename(file)
        file = open(file, "r").readlines()
        for line in file:
            if line.startswith("#"):
                continue
            else:
                line = line.rstrip().split()
                species = line[0]
                count = int(line[1])
                conn = float(line[2])
                members = line[3:]
                members = self.split(members)
            for nr, member in enumerate(members):
                name = basename+"_"+str(nr)
                if self.clusters.has_key(name):
                    self.clusters[name].members.append(member)
                else:
                    self.clusters[name] = Cluster(name,member)

    def split(self,items):
        items = list(set(items))
        items.remove("*")
        split_items = []
        for item in items:
            split_items.append(item.split(","))
        items = [item for sublist in split_items for item in sublist]
        return items
