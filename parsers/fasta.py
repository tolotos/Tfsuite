#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       fasta.py

def read_fasta(sequences):
    seqs = {}
    with open(sequences, "r").readlines() as lines:    
        for line in lines:
            if line[0] == ">":
                name = line[1:].rstrip()
                if name[4] == "|": # Account for species
                    name = name.split("|")[1]
                    seqs[name] = ""
                else:
                    seqs[name] = ""
            else:
                seqs[name] += line.rstrip()
    return seqs
   
        if sequences is not None:
            format = format.lower()
            if format in self.parsers:
                read = self.parsers[format][0]
                seqs = read(sequences)