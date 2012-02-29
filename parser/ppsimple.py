#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       cyto.py

import os
import sys


def read_ppsimple(source, obj=None):

        if obj is None:
            from Tfsuite.core import network
            NET = network.Network()
        else:
            NET = obj

        try:
            #basename = os.path.basename(source)

            with open(source, "r") as file:
                for line in file.readlines():
                    line = line.rstrip().split()
                    if line[0] in NET.nodes:
                        NET.nodes[line[0]].append(line[2])
                    else:
                        NET.nodes[line[0]] = [line[2]]

                    if NET.interaction_type == None:
                        NET.interaction_type = line[1]
                    elif line[1] != NET.interaction_type:
                        print "More then one interaction type"
                return NET
        except IOError:
            print "!----ERROR----!"
            print "File %s does not exit!" % source
            sys.exit(1)
        except KeyboardInterrupt:
            sys.exit(1)
