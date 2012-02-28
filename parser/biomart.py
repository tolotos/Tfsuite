#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       biomart.py

import sys


def read_biomart(source, obj=None):
    biomart = {}

    try:
        with open(source, "r") as file:
            for line in file.readlines():
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
                    biomart[gene_name] = [uniprot_id, associated_name]
            return biomart
    except IOError:
        print "!----ERROR----!"
        print "File %s does not exit!" % source
        sys.exit(1)
    except KeyboardInterrupt:
        sys.exit(1)
