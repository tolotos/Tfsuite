#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       clustergroup.py

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
            if protein.gene_name in seqs:
                protein.seq = seqs[protein.gene_name]

    def attach_domains(self, domains=None, format="xdom"):
        read = select_parser(domains, format)
        domains = read(domains, 1e-3)
        for protein in self.iter_proteins():
            if protein.gene_name in domains:
                protein.domains = domains[protein.gene_name]

    def attach_arangement(self, arangement=None, format="arag"):
        read = select_parser(arangement, format)
        arag = read(arangement)
        for protein in self.iter_proteins():
            if protein.gene_name in arag:
                protein.species = arag[protein.gene_name][0]
                protein.arangement = arag[protein.gene_name][1]

    def attach_families(self, family=None, format="fam"):
        read = select_parser(family, format)
        family = read(family)
        for protein in self.iter_proteins():
            protein.add_family(family)

    def attach_biomart(self, biomart=None, format="biomart"):
        read = select_parser(biomart, format)
        biomart = read(biomart)
        for protein in self.iter_proteins():
            if protein.gene_name in biomart:
                protein.associated_name = biomart[protein.gene_name][1]
                protein.uniprot_id = biomart[protein.gene_name][0]

    def get_proteins_by_species(self, species):
        proteins = []
        for protein in self.iter_proteins():
            if protein.species == species:
                proteins.append(protein)
        return proteins

    def iter_clusters(self):
        for cluster in self.clusters.values():
            yield cluster

    def iter_proteins(self):
        for cluster in self.iter_clusters():
            for protein in cluster.proteins:
                yield protein
