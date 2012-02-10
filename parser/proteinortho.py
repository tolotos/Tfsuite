#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       proteinortho.py

import os
from Tfsuite.core.cluster import Cluster


def read_proteinortho(source, obj=None):

        if obj is None:
            from Tfsuite.core import clustergroup
            CG = clustergroup.ClusterGroup()
        else:
            CG = obj

        clust_id = 0

        try:
            basename = os.path.basename(source)

            with open(source, "r") as file:
                for line in file.readlines():
                    if line.startswith("#") or not line:
                        continue
                    else:
                        name = basename + "_" + str(clust_id)
                        line = line.rstrip().split()

                        species, count, conn = line[0], int(line[1]), float(line[2])
                        members = line[3:]
                        members = split_items(members)

                        CL = Cluster(name, members)
                        CG.clusters[name] = CL

                        clust_id += 1
                return CG
        except IOError:
            print "File does not exit!"


def split_items(items):
    items = list(set(items))
    items.remove("*")
    split_items = []
    for item in items:
        split_items.append(item.split(","))
    items = [item for sublist in split_items for item in sublist]
    return items
