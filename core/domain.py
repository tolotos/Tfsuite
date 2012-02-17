#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       Domain.py
class Domain:

###  class-method: defines all possible data of an domain  ###
	def __init__(self, id, begin, end, evalue):	# required data
		self.name = None		
		self.id = id
		self.begin = int(begin)
		self.end = int(end)
		self.evalue = float(evalue)
		self.species = None				# optional data
		self.length = self.end-self.begin				# calculated value
		self.description = None	
		self.sequence=None
	
###  class-method: assigns optional data to object, if existing  ###
	def set_species(self,species):
		if species != "":				# replaces None if there's an entry for species
			self.species = species

	def set_description(self, description):
		if description != "":
			self.description = description

	def set_name(self, name):
		if name != "":
			self.name = name