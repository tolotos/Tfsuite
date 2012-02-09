#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       proteinortho.py

import os
from Tfsuite.Classes.cluster import Cluster


def read_proteinortho(source, obj=None):
        
        if obj is None:
            from Tfsuite.core import clustergroup
            CG = clustergroup.ClusterGroup()
        else:
            CG = obj
        
        basename = os.path.basename(source)
        
        with open(source, "r").readlines() as file:
            for line in file:
                if line.startswith("#") or not line:
                    continue
                else:
                    line = line.rstrip().split()
                    species, count, conn = line[0], int(line[1]), float(line[2])
                    members = line[3:]
                    members = split_items(members)

                    print members
                    # for nr, member in enumerate(members):
                    #     name = basename+"_"+str(nr)
                    #     if self.clusters.has_key(name):
                    #         self.clusters[name].members.append(member)
                    #     else:
                    #         self.clusters[name] = Cluster(name,member)

def split_items(self,items):
    items = list(set(items))
    items.remove("*")
    split_items = []
    for item in items:
        split_items.append(item.split(","))
    items = [item for sublist in split_items for item in sublist]
    return items
