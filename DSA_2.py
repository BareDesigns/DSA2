# Jonathan Nguyen; #000918228

import json
from string import ascii_lowercase
# from vertex_data import *


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
        self.add_dir_edge(vertex_a, vertex_b, weight)
        self.add_dir_edge(vertex_b, vertex_a, weight)


location_names = []
vertex_names = []
location_dict = {}

with open('Distance_Table.json') as data_file:
    places = json.load(data_file)
    for b in places['locations']:
        location_names.append(b)
for letter in ascii_lowercase:
    vertex_names.append('vertex_' + letter)
location_dict = dict(zip((vertex_names), (location_names)))

g = Graph()

# Assign the graph variables to the location names
for k, v in location_dict.items():
    globals()[k] = Vertex(v)


vertex_hub = Vertex("WGU")
g.add_vertex(vertex_hub)

g.add_undir_edge(vertex_hub, vertex_t, 1.2)
g.add_undir_edge(vertex_HUB, vertex_v, 2.4)
g.add_undir_edge(vertex_HUB, vertex_q, 2.0)
