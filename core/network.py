#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       network.py


from Tfsuite.parser.base import select_parser
import xmlrpclib


class Network(object):

    def __init__(self, source=None, format="ppsimple", name=None):
        self.name = name
        self.nodes = {}
        self.interaction_type = None
        self.cytoscape_connection = False
        self.cytoscape = None
        self.cytoscape_id = None
        read = select_parser(source, format)
        read(source, obj=self)

    def __iter__(self):
        #We are an iterable, so return our iterator
        for i in self.nodes:
            yield i, self.nodes[i]

    def edges(self):
        "Does not work right now!"
        from_nodes = []
        to_nodes = []
        for node in self.nodes:
            for i in range(len(self.nodes[node])):
                from_nodes.append(node)
            for to_node in self.nodes[node]:
                to_nodes.append(to_node)
        return from_nodes, to_nodes

    def connect_to_cytoscape(self, server=None):
        if not self.cytoscape_connection:
            server = xmlrpclib.ServerProxy(server)
            self.cytoscape = server.Cytoscape
            self.cytoscape_connection = True
        elif self.cytoscape_connection:
            print "Connection to Cytoscape already established!"

    def create_cytoscape_network(self):
        if self.cytoscape_connection:
            if self.cytoscape.hasCurrentNetwork():
                old_id = self.cytoscape.getNetworkID()
                self.cytoscape.destroyNetwork(old_id)
                self.cytoscape.createNetwork(self.name)
                self.cytoscape_id = self.cytoscape.getNetworkID()
                self.__populate_cytoscape_network()
                print self.name
            else:
                self.cytoscape.createNetwork(self.name)
                self.cytoscape_id = self.cytoscape.getNetworkID()
                self.__populate_cytoscape_network()
                print "Created a new Cytoscape network with title %s!" % self.name
        else:
            print "No Cytoscape connection recognized!"

    def __populate_cytoscape_network(self):
        from_nodes, to_nodes = self.edges()
        self.cytoscape.createNodes(self.nodes.keys())
        self.cytoscape.createEdges(from_nodes, to_nodes)
        self.cytoscape.performLayout("force-directed")

    def scale_nodesize_by_connectivity(self, r):
        size = 70
        for i in r:
            for node in self.cytoscape.getNodes():
                connections = len(self.cytoscape.getNodeNeighbors(self.cytoscape_id,
                                                                  node))
                if connections >= i:
                    self.cytoscape.setNodeProperty(node,
                                                   "Node Size",
                                                   str(size))
            size += 6

    def color_by_cluster(self, cluster, color):
        r, g, b = color[0], color[1], color[2]
        for member in cluster.members:
            if member.species == "hsap":
                for node in self.cytoscape.getNodes():
                    if member.associated_name == str(node):
                        self.cytoscape.setNodeFillColor(self.cytoscape_id,
                                                        [node], r, g, b)

    def color_by_arrangement(id, cytoscape, arag_dic):
        colors = load_colors(options.yaml)
        for arag, members in arag_dic.items():
            color_name = colors[0][0]
            color_rgb = colors[0][1]
            #print color_rgb
            r,g,b = color_rgb[0],color_rgb[1],color_rgb[2]
            #print color_name, arag, members
            for member in members:
                for node in cytoscape.getNodes():
                    if member == str(node):
                        cytoscape.setNodeFillColor(id,[node], r,g,b)
            del colors[0]

    def shape_by_arangement(arag_dic):
        shapes = ["trapezoid","rect_3d","round_rect","ellipse","triangle",
                  "diamond","octagon","parallelogram","trapezoid_2",
                  "rect","vee","hexagon"]
        if len(arag_dic) > len(shapes):
            print "Too many arangements, not enough shapes available!"
        else:
            for num, arangements in enumerate(arag_dic):
                for node in arag_dic[arangements]:
                    cytoscape.setNodeProperty(node,"Node Shape", shapes[num])

    def shape_by_cluster(id,cytoscape, clusters):
        shapes = ["trapezoid","rect_3d","round_rect","ellipse","triangle",
                  "diamond","octagon","parallelogram","trapezoid_2",
                  "rect","vee","hexagon"]
        if len(clusters.clusters) > len(shapes):
            print len(clusters.clusters)
            print "Too many clusters, not enough shapes available!"
        else:
            for num, cluster in enumerate(clusters):
                for member in cluster.members:
                    cytoscape.setNodeProperty(member,"Node Shape", shapes[num])

    def add_cluster_id_to_name(clusters, species):
            for cluster in clusters:
                id = "_CL"+cluster.name.split("_")[1]
                for member in cluster.members:
                    if member.species == species:
                        for node in cytoscape.getNodes():
                            if member.associated_name == str(node):
                                cl_name = member.associated_name+id
                                cytoscape.setNodeProperty(node,"Node Label",cl_name)
