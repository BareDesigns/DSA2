# Jonathan Nguyen; #000918228

import json
import pandas
from string import ascii_uppercase


class Vertex:
    def __init__(self, label):
        self.label = label


class Graph:
    # This class is for setting up graphs and edges

    def __init__(self):
        # INIT function
        self.adjacency_list = {}
        self.edge_weights = {}

    def add_vertex(self, new_vertex):
        # Function to add a vertex
        self.adjacency_list[new_vertex] = []

    def add_dir_edge(self, from_vertex, to_vertex, weight=1.0):
        # Function to add a direct edge and the weight of that edge
        self.edge_weights[(from_vertex, to_vertex)] = weight
        self.adjacency_list[from_vertex].append(to_vertex)

    def add_undir_edge(self, vertex_a, vertex_b, weight=1.0):
        # Function to add an undirected edge and the weight of that edge
        self.add_dir_edge(vertex_a, vertex_b, weight)
        self.add_undir_edge(vertex_b, vertex_a, weight)


def master_list():
    '''This function puts the location names and vertex names into 1 dictionary'''

    with open('Distance_Table.json') as data_file:
        places = json.load(data_file)
        for b in places['locations']:
            location_names.append(b)
    for letter in ascii_uppercase:
        vertex_names.append('vertex_' + letter)
    location_dict1 = dict(zip((vertex_names), (location_names)))
    return location_dict1


g = Graph()
vertex_HUB = Vertex("WGU")
# Creating list variables for merging with function
location_names = []
vertex_names = []
location_dict1 = {}


# Assign the graph variables to the location names
for v, x in location_dict1.items():
    v = Vertex(str(x))

print(master_list())
print(Graph)
