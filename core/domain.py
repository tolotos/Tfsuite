#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       Domain.py


class Domain:

    def __init__(self, id, begin, end, evalue):
        self.name = None
        self.id = id
        self.begin = int(begin)
        self.end = int(end)
        self.evalue = float(evalue)
        self.species = None
        self.length = self.end - self.begin
        self.description = None
        self.sequence = None

    def set_species(self, species):
        if species != "":
            self.species = species

    def set_description(self, description):
        if description != "":
            self.description = description

    def set_name(self, name):
        if name != "":
            self.name = name
