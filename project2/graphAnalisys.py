#!/usr/bin/python
# For begginers I recomend
# https://programminghistorian.org/lessons/exploring-and-analyzing-network-data-with-python

numberOfGraphs = 20
numberOfNodesPerGraph = 1000
typeOfProbability = 2 # 1=Equal, 2=Connections, 3=Time
connectionsPerNode = 8

headers = True # Generate the CSV header row
separator = ',' # CSV separator, in some cases people use semicolon
saveGEXF = False # Export G into Gephi's GEXF format

# Select the analysis functions, some take a lot of time:
density = False
diameter = False
degrees = False
eccentricity = False
center = False
periphery = False

# End of customizable options

import networkx as nx
from nodesConnectionsGenerator import generateCsv as gen
selected = [density,diameter,degrees,eccentricity,center,periphery]

def parseCSVGraphAnalysis(G):
  global headers
  row = ''
  data = nx.info(G).split('\n')
  nameG = data[0].split(':')[1].strip()
  if saveGEXF:
  	nx.write_gexf(G, nameG+'.gexf')
  if headers:
    row = 'Name' + separator + separator.join(val.split(':')[0] for val in data[2:])
    row += (separator + 'Density') if selected[0] else ''
    row += (separator + 'Diameter') if selected[1] else ''
    row += (separator + 'Degrees') if selected[2] else ''
    row += (separator + 'Eccentricity') if selected[3] else ''
    row += (separator + 'Center') if selected[4] else ''
    row += (separator + 'Periphery') if selected[5] else ''
    row += '\n'
    headers = False
  row += nameG + separator + separator.join(val.split(':')[1].strip() for val in data[2:])
  row += (separator + str(nx.density(G))) if selected[0] else ''
  row += (separator + str(nx.diameter(G))) if selected[1] else ''
  row += (separator + str(nx.degree(G))) if selected[2] else ''
  row += (separator + str(nx.eccentricity(G))) if selected[3] else ''
  row += (separator + str(nx.center(G))) if selected[4] else ''
  row += (separator + str(nx.periphery(G))) if selected[5] else ''
  return row

def generateGraphs(n,t):
  for i in range (numberOfGraphs):
    G = gen(n,t,connectionsPerNode,id=i+1)
    print parseCSVGraphAnalysis(G)

# ToDo: Add multiprocessing
generateGraphs(numberOfNodesPerGraph,typeOfProbability)