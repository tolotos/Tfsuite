#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       proteine.py


class Protein:

    def __init__(self, gene_name):
        self.gene_name = gene_name
        self.seq = ""
        self.cluster = None
        self.species = None
        self.domains = []
        self.family = None
        self.uniprot_id = None
        self.associated_name = None
        self.secondary_ids = []





    def add_identifiers(self, biomart):
        if self.gene_name in biomart.ids:
            self.uniprot_id = biomart.ids[self.gene_name][0]
            self.associated_name = biomart.ids[self.gene_name][1]

    def collapse_domains(self):
        domain_list = []
        for domain in self.domains:
            if len(self.domains) > 2:
                if len(domain_list) < 2:
                    domain_list.append(domain)
                elif domain_list[-1] == domain and domain_list[-2] == domain:
                    pass
                else:
                    domain_list.append(domain)
                if len(domain_list) > 0:
                    self.domains = domain_list
                else:
                    pass
    def export_fasta(self):
        return ">"+self.species+"_"+self.gene_name+"\n", self.seq+"\n"


    def add_cluster(self,clusters):
        '''Adds the id of the to a protein. This is slow, if not necessary use
           "add_cluster_to_members" function for each cluster, which is much
           faster.'''
        for cluster in clusters:
            if self.gene_name in cluster.members:
                self.cluster = cluster.name

    def add_family(self, family):
        '''Uses the mapping file that was provided before and compares the
        domain arrangements in the hmmout to the family mapping. If a hit is
        found, the family is set, otherwise it stays "None".'''
        #self.collapse_domains()
        domains =";".join(self.domains)
        if domains in family.mapping:
            self.family = family.mapping[domains]

    #def add_species(self, species):
        #if self.gene_name in species.specmap:
            #self.species = species.specmap[self.gene_name]
    def add_species(self):
        self.species = self.gene_name.split("|")[0]

