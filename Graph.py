import json
from string import ascii_lowercase


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

    def edge_data(self, vertex_1, vertex_2, weight=1.0):
        self.edge_weights[(vertex_1, vertex_2)] = weight
        self.adjacency_list[vertex_1].append(vertex_2)

    def add_edge(self, vertex_1, vertex_2, weight=1.0):
        self.edge_data(vertex_1, vertex_2, weight)
        self.edge_data(vertex_2, vertex_1, weight)

    # Set empty lists/dict for later use in the code
location_names = []
vertex_names = []
location_dict = {}

# Open the JSON file and use the names as variables
with open('Distance_Table.json') as data_file:
    places = json.load(data_file)
    for b in places['locations']:
        location_names.append(b)

# Make a dictionary that holds all the vertex names and keys for looping
for letter in ascii_lowercase:
    vertex_names.append('vertex_' + letter)

# Set the location_dict to hold all the vertex names and locations names from JSON
location_dict = dict(zip((vertex_names), (location_names)))

# Set graph variable
g = Graph()

# Assign the graph variables to the location names
# First part will assign the key names to the Vertex names
# Second part makes a variable to add to vertex class
for k, v in location_dict.items():
    globals()[k] = Vertex(v)
    foo = globals()[k]
    g.add_vertex(foo)

vertex_hub = Vertex("WGU")
g.add_vertex(vertex_hub)

# Make graph edges
g.add_edge(vertex_hub, vertex_t, 1.2)
g.add_edge(vertex_hub, vertex_v, 2.4)
g.add_edge(vertex_hub, vertex_q, 2.0)
g.add_edge(vertex_t, vertex_u, 2.0)
g.add_edge(vertex_v, vertex_x, 1.7)
g.add_edge(vertex_v, vertex_c, 6.1)
g.add_edge(vertex_x, vertex_z, 1.3)
g.add_edge(vertex_c, vertex_w, 9.7)
g.add_edge(vertex_w, vertex_p, 7.5)
g.add_edge(vertex_w, vertex_j, 0.4)
g.add_edge(vertex_q, vertex_d, 0.5)
g.add_edge(vertex_d, vertex_r, 1.7)
g.add_edge(vertex_d, vertex_k, 1.5)
g.add_edge(vertex_k, vertex_n, 2.6)
g.add_edge(vertex_n, vertex_r, 2.2)
g.add_edge(vertex_n, vertex_m, 1.3)
g.add_edge(vertex_m, vertex_g, 1.6)
g.add_edge(vertex_r, vertex_o, 2.2)
g.add_edge(vertex_r, vertex_e, 1.1)
g.add_edge(vertex_o, vertex_i, 4.0)
g.add_edge(vertex_i, vertex_e, 1.5)
g.add_edge(vertex_i, vertex_b, 6.3)
g.add_edge(vertex_e, vertex_s, 3.5)
g.add_edge(vertex_e, vertex_a, 3.5)
g.add_edge(vertex_a, vertex_f, 10.9)
g.add_edge(vertex_s, vertex_y, 1.8)
g.add_edge(vertex_s, vertex_l, 1.0)
g.add_edge(vertex_l, vertex_h, 7.7)
