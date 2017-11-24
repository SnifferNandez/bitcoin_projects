#!/usr/bin/python
# For begginers https://programminghistorian.org/lessons/exploring-and-analyzing-network-data-with-python

import networkx as nx
#import matplotlib.pyplot as plt
from nodesConnectionsGenerator import generateCsv as gen

numberOfGraphs = 100
numberOfNodesPerGraph = 1000
typeOfProbability = 1 # 1=Equal, 2=Connections, 3=Time
headers = True

def parseCSVGraphInfo(G):
  global headers
  row = ""
  data = nx.info(G).split('\n')
  if headers:
  	row = ",".join(val.split(':')[0] for val in data) + "\n"
  	headers = False
  row = row + ",".join(val.split(':')[1].strip() for val in data)
  return row

def generateGrapsh(n,t):
  for i in range (numberOfGraphs):
  	G = gen(n,t,id=i)
  	print parseCSVGraphInfo(G)
    print "Center: " + str(nx.center(G))
    # Functions
    #print "Density: " + str(nx.density(G))
    #print "Degrees: " + str(nx.degree(G))

    # Distance Measures, take a lot of time
    #print "Diameter: " + str(nx.diameter(G))
    #print "Eccentricity: " + str(nx.eccentricity(G))
    #print "Center: " + str(nx.center(G))
    #print "Periphery: " + str(nx.periphery(G))

#Export your into Gephi's GEXF format
#nx.write_gexf(G, 'bitcoin_network.gexf')

generateGrapsh(numberOfNodesPerGraph,typeOfProbability)