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
    nx.draw_networkx_nodes(weightedGraph, position, node_color = nodeColor)
    # draws the specific edges and places them into position
    nx.draw_networkx_edges(weightedGraph, position)
    # draws the specific labels and places them into position
    nx.draw_networkx_labels(weightedGraph, position)

    # variable edge_labels from the module is used to make the distance data true from the csv file
    edge_labels = {(nodeOne, nodeTwo): weight['weight'] for nodeOne, nodeTwo, weight in weightedGraph.edges(data = True)}
    # draws the distance numbers along with the graph
    nx.draw_networkx_edge_labels(weightedGraph, position, edge_labels = edge_labels)

    # shows the graph using the matpilotlib module
    plt.show()

# function for dijkstras algorithm that used the graph, originNode, and destination node variables
def dijkstraAlg(graph, originNode, destination):
    # originally makes the node not visited in for the nodes within the graph
    nodeVisited = {node: False for node in graph.nodes()}
    # makes the distance originally infinity for from one node to another for all nodes in the graph
    distance = {node: float('inf') for node in graph.nodes()}
    # makes the distance of the starting node 0
    distance[originNode] = 0

    # while loop for when the destination node is not visited
    while not nodeVisited[destination]:
        # minimum distance variable is infinite
        minimumDist = float('inf')
        # minimum node variable is none
        minimumNode = None
        # for loop for nodes within the graph
        for node in graph.nodes():
            # if statement for when nodes are not visited and the distance of a node is less the minimum distance
            if not nodeVisited[node] and distance[node] < minimumDist:
                # minimum distance is set to the distance towards the node
                minimumDist = distance[node]
                # minimum node is now the node that was visited
                minimumNode = node
        
        # the minimum node that was visited is set to true
        nodeVisited[minimumNode] = True
        # for loop for the next node and weight for the minium node in the graph
        for nextNode, weight in graph[minimumNode].items():
            # if statement for when the next node is not visited and the distance towards minimum node and weight is less then the distance to the next node
            if not nodeVisited[nextNode] and distance[minimumNode] + weight['weight'] < distance[nextNode]:
                # next node distane is set to the distance of the minimum node plus weight
                distance[nextNode] = distance[minimumNode] + weight['weight']
    # returns the destination distance
    return distance[destination]

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
# while statement that is true is created
while True:
    # startNode will be input variable for the user to put in the starting node
    startNode = input("Enter the node you would like to start at (A-W): ")
    # if statement for when the user puts in "exit"
    if startNode.lower() == 'exit':
        # breaks loop and program ends
        break
    # elif statement for when user enter either X, Y, Z or an integer is entered, or the user enters letters not within the data of the cvs file
    elif startNode.upper() in {'X', 'Y', 'Z'} or startNode.isdigit() or len(startNode) != 1 or startNode.upper() not in weightedGraph.nodes():
        # invalid message is printed
        print("These are not nodes! Please try again!")
        # continues with the process
        continue
    # if a legit node is entered
    else:
        # user input will automatically turn into a capital letter if a lower case letter is entered
        startNode = startNode.upper()
        # list for the charging station nodes
        chargingNode = ['H', 'K', 'Q', 'T']

        # initially sets the closest destination to none
        closestDest = None
        # sets the shortest length to infinity
        shortestLength = float('inf')

        # dictionary for shortest paths is empty
        shortestPaths = {}
        # for loop for the EV nodes within the charging node list
        for evNode in chargingNode:
            # shortest paths dictionary from the EV nodes will represent what occurs in the dijkstra algorithm function
            shortestPaths[evNode] = dijkstraAlg(weightedGraph, startNode, evNode)
            # if statement for when the shortest path from the EV node is smaller then the shortest length
            if shortestPaths[evNode] < shortestLength:
                # EV node becomes the shortest destination
                closestDest = evNode
                # EV shortest path becomes the shortest lentgh
                shortestLength = shortestPaths[evNode]
        # for statement for the EV node, shortest path and the items in the shortest paths dictionary
        for evNode, shortestPath in shortestPaths.items():
            # prints the shortest path from each start node to all the charging nodes
            print("Shortest path length from", startNode, "to", evNode, ":", shortestPath)
        # prints the closest destination to the start node
        print("The closest destination to", startNode, "is", closestDest)
