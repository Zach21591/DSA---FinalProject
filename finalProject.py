# modules used to display graph are imported
import csv
import networkx as nx
import matplotlib.pyplot as plt

#function to load the csv file
def loadCSV(data):
    # variable called weightedGraph to represent the networkx module
    weightedGraph = nx.Graph()
    # opens the csv file and reads it
    with open(data, 'r') as file:
        # variable called read represents the csv file
        read = csv.DictReader(file)
        # for statement for the rows within the csv file represented by the read variable
        for row in read:
            # variable node will represent the nodes in the csv file
            node = row['Node']
            # variable edge will represent the edges in the csv file
            edge = row['Edge']
            # variable vertDist will represent the vertex distance in the csv file
            vertDist = int(row['Vertex Distance'])
            # weightedGraph variable will add the the variables above from that is gotten from the csv file
            weightedGraph.add_edge(node, edge, weight = vertDist)
    # returns the data from the csv file
    return weightedGraph

# function to show the graph
def graphDisplay(weightedGraph, nodeColor = None):
    # positions the graph
    position = nx.spring_layout(weightedGraph)
    # draws the graph using the networkx module
    nx.draw_networkx(weightedGraph, position, node_color = nodeColor)
    # shows the graph using the matpilotlib module
    plt.show()

# variable to that calls the csv file with the data in it
data = 'DSA Final Project - Weighted Graph.csv'
# allows the loadCSV to access the csv file
weightedGraph = loadCSV(data)

# list for the node colors
nodeColor = []
# for loop for nodes within the graph using data from the csv file
for node in weightedGraph.nodes():
    # if statement for when the node is either H, K, Q, or T
    if node == 'H' or node == 'K' or node == 'Q' or node == 'T':
        # color will be lime
        nodeColor.append('lime')
    # else statement for the rest of the nodes
    else:
        # color will be lightblue
        nodeColor.append('lightblue')

# Uses the graphDisplay to show the graph
graphDisplay(weightedGraph, nodeColor)
# prints the nodes
print("Nodes:", weightedGraph.nodes())
# prints the edges
print("Edges:", weightedGraph.edges())
