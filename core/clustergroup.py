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

    def attach_domains(self, domains=None, format="xdom"):
        read = select_parser(domains, format)
        domains = read(domains)
        for protein in self.iter_proteins():
            if protein.gene_name in domains:
                for domain in domains[protein.gene_name]:
                    domain = domain.split(",")
                    print domain

    def attach_arangement(self, arangement=None, format="arag"):
        read = select_parser(arangement, format)
        arag = read(arangement)
        print arag

    def attach_biomart():
        pass

    def iter_clusters(self):
        for cluster in self.clusters.values():
            yield cluster

    def iter_proteins(self):
        for cluster in self.iter_clusters():
            for protein in cluster.proteins:
                yield protein
