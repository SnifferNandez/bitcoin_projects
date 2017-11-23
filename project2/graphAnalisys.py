#!/usr/bin/python
# For begginers https://programminghistorian.org/lessons/exploring-and-analyzing-network-data-with-python

import networkx as nx
#import matplotlib.pyplot as plt
from nodesConnectionsGenerator import generateCsv as gen

G = gen(1000)
print nx.info(G)
# Functions
print "Density: " + str(nx.density(G))
#print "Degrees: " + str(nx.degree(G))

# Distance Measures
print "Diameter: " + str(nx.diameter(G))
#print "Eccentricity: " + str(nx.eccentricity(G))
print "Center: " + str(nx.center(G))
#print "Periphery: " + str(nx.periphery(G))

#Export your into Gephi's GEXF format
#nx.write_gexf(G, 'bitcoin_network.gexf')
