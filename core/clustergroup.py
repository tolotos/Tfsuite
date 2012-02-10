#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       Cluster.py

from Tfsuite.parser.proteinortho import read_proteinortho


class ClusterGroup(object):

    def __init__(self, clusters=None, format="proteinortho", name=None):
        self.name = name
        self.clusters = {}
        self.parser = {
                "proteinortho": [read_proteinortho, {}],
                "orthomcl": []
        }

        if clusters is not None:
                format = format.lower()
                if format in self.parser:
                        read = self.parser[format][0]
                        read(clusters, obj=self)
                else:
                        raise ValueError("Unsupported format: [%s]" % format)
