#!/usr/bin/python
# Generate a csv file like:
# NodeA,NodeB,Moment
# 1,2,1
# 1,3,1
# 2,3,1
# Each line indicates that a link between NodeA and NodeB appears at a particular Moment

import networkx as nx
from random import SystemRandom
# random.SystemRandom uses the system function os.urandom() to generate random numbers
# randrange generates a pseudo-random integer from the range indicated
# choice select a single item from a Python sequence type - that's any of str, unicode, list, tuple, bytearray, buffer, xrange -
# sample which does support sets

typeProbability = 2 # 1=Equal, 2=Connections, 3=Time
fullyConnectedNodes = 8 # on initial time, t0=1
totalNodes = 13
connectionsPerNode = 8
separator = ","

prgn = SystemRandom()
poolNodes = []

def getRandomsNodesToConnect(connect):
  #print poolNodes
  randomNodes = set()
  if typeProbability == 1 or typeProbability == 2:
    maxRange = len(poolNodes)
  while len(randomNodes) < connect:
    randomNode = poolNodes[prgn.randrange(maxRange)]
    if typeProbability == 1 or typeProbability == 2:
      randomNodes.add(randomNode)
  return randomNodes

def addNodeProbability(e1,e2):
  global poolNodes, G
  # https://zenagiwa.wordpress.com/2014/10/23/graphing-networks-for-beginners/
  G.add_edge(e1,e2)
  if (typeProbability == 1 or typeProbability == 3) and len(poolNodes) < e1:
    if len(poolNodes) == 0:
      poolNodes.append(1)
    poolNodes.append(e1)
  if typeProbability == 2:
    poolNodes.append(e1)
    poolNodes.append(e2)
  

def printEdges(e1,e2,t="",addNode=True):
  if __name__ == "__main__":
    print str(e1) + separator + str(e2) + separator + str(t)
  # http://pythoncentral.io/select-random-item-list-tuple-data-structure-python/
  if addNode:
    addNodeProbability(e1,e2)

def initialNodes():
  printEdges('"id1"', '"id2"', '"time"',False)
  for i in range (2,fullyConnectedNodes+1):
    j = i - 1
    while j > 0:
      printEdges(i,j,1)
      j = j - 1

def randomNodes():
  for i in range(fullyConnectedNodes+1,totalNodes+1):
    connect = i if i < connectionsPerNode else connectionsPerNode
    connections = getRandomsNodesToConnect(connect)
    #print "".join(str(i) + " " + str(e) + " " + str(i-fullyConnectedNodes+1) + "\n" for e in connections)[:-1]
    for e in connections:
      printEdges(i,e,i-fullyConnectedNodes+1)

def generateCsv(tn=totalNodes,tp=typeProbability,cpn=connectionsPerNode,fc=fullyConnectedNodes,se=separator):
  global G, poolNodes
  G = nx.Graph(name='n'+str(tn)+'p'+str(tp)) #creates a graph
  poolNodes = []
  global totalNodes,typeProbability,connectionsPerNode,fullyConnectedNodes,separator
  totalNodes=tn
  typeProbability=tp
  connectionsPerNode=cpn
  fullyConnectedNodes=fc
  separator=se
  initialNodes()
  # Limit the process, max 5 GB
  if typeProbability == 3 and totalNodes > 30:
    totalNodes = 31 
  randomNodes()
  return G

if __name__ == "__main__":
  generateCsv()