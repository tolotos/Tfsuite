#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       base.py

from Tfsuite.parser.proteinortho import read_proteinortho
from Tfsuite.parser.fasta import read_fasta, write_fasta

parser = {
    "proteinortho": [read_proteinortho, None, {}],
    "orthomcl": [],
    "fasta": [read_fasta, write_fasta, {}]
}


def select_parser(input, format):
    format = format.lower()
    if validate_input(input, format):
        return parser[format][0]


def validate_input(input, format):
    if input is not None:
        if format in parser:
            return True
        else:
            raise ValueError("Unsupported format: %s" % format)
    else:
        raise IOError("Please supply an input file!")


# def validate_object(format, obj_type):
#     if obj_type is not None:
#         supported = parser[format][2]
#         if supported[obj_type]:
#             return True
#         else:
#             raise ValueError("This input file is not supported for the given object type!")
#     else:
#         raise ValueError("Please support an object with type!")
