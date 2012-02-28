#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       network.py


class Network:

    def __init__(self):
        self.name = ""
        self.nodes = {}
        self.interaction_type = None

    def __iter__(self):
        #We are an iterable, so return our iterator
        for i in self.nodes:
            yield i, self.nodes[i]

    def edges(self):
        from_nodes = []
        to_nodes = []
        for node in self.nodes:
            for i in range(len(self.nodes[node])):
                from_nodes.append(node)
            for to_node in self.nodes[node]:
                to_nodes.append(to_node)
        return from_nodes, to_nodes
