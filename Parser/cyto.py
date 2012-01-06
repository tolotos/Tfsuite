#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       cyto.py

import glob
import sys

class Cyto:

    def __init__(self):
        self.name = ""
        self.nodes = {}
        self.interaction_type = None

    def __iter__(self):
        #We are an iterable, so return our iterator
        for i in self.nodes:
            yield i, self.nodes[i]


    def load(self,cyto_file):
        cyto_file = open(cyto_file, "r").readlines()
        for line in cyto_file:
            line = line.rstrip().split()
            if self.nodes.has_key(line[0]):
                self.nodes[line[0]].append(line[2])
            else:
                self.nodes[line[0]] = [line[2]]
            if self.interaction_type == None:
                self.interaction_type = line[1]
            else:
                if line[1] != self.interaction_type:
                    print "More then one interaction type detected!"

    def edges(self):
        from_nodes = []
        to_nodes = []
        for node in self.nodes:
            for i in range(len(self.nodes[node])):
                from_nodes.append(node)
            for to_node in self.nodes[node]:
                to_nodes.append(to_node)
        return from_nodes, to_nodes
