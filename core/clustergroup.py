#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       Cluster.py


from Tfsuite.parser.base import select_parser


class ClusterGroup(object):

    def __init__(self, clusters=None, format="proteinortho", name=None):
        self.name = name
        self.clusters = {}

        read = select_parser(clusters, format)
        read(clusters, obj=self)

    def attach_sequences(self, sequences=None, format="fasta"):
        read = select_parser(sequences, format)
        seqs = read(sequences)
        for protein in self.iter_proteins():
            if protein in seqs:
                protein.seq = seqs[protein]


    def attach_domains():
        read = select_parser(sequences, format)

    def attach_biomart():
        pass

    def iter_clusters(self):
        for cluster in self.clusters.values():
            yield cluster

    def iter_proteins(self):
        for proteins in self.iter_clusters():
            yield proteins
