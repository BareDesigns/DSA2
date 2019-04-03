# Jonathan Nguyen; #000918228

'''Algorithm.py: This .py file's purpose is to run our truck/package data through 
dijkstra's algorithm.'''

import json
from Trucks import *
from Graph import *


class dj_algorithm:
    '''The purpose of this class is to hold three functions, one for each truck. In the __init__
    function, we establish all of the necessary variables needed for each function. As for scalability,
    each function can simply be copied, with only a few variable names being changed. Although, because
    the complexity is (O(n^2)), it might cause some slowdowns should it get too large, it should 
    theoretically be able to expand or shrink to any size without issue.'''

    # In this function we set 3 variables for the following functions. The touched dictionary will be the
    # nodes visited. The untouched dictionary will be the yet to be visited nodes. The current node
    # string establishes our starting point, and the sorted nodes will sort the remaining nodes by
    # shortest distance in order to complete the algorithm.
    # The big O complexity for this function is (O(1)).
    def __init__(self):
        self.touched = {}
        self.touched_2 = {}
        self.touched_3 = {}
        self.untouched = {}
        self.untouched_2 = {}
        self.untouched_3 = {}
        self.current_node = 'hub'
        self.current_node_2 = 'hub'
        self.current_node_3 = 'hub'
        self.current_distance = 0
        self.current_distance_2 = 0
        self.current_distance_3 = 0
        self.sorted_nodes = sorted(self.untouched)
        self.sorted_nodes_2 = sorted(self.untouched_2)
        self.sorted_nodes_3 = sorted(self.untouched_3)
        self.total_distance_1 = 0
        self.total_distance_2 = 0

    # The truck_one function will take the list information from the main truck, and
    # pass it through this version of dijkstra's algorithm. First, we set the initial node,
    # set the new distance, and finally set the closest node as the current one until all
    # have been put into the touched list.
    def truck_one(self, master_list):
        # This for loop simply appends the items from the first truck and puts them into
        # the untouched dictionary.
        # The big O complexity for this for loop is (O(N)).
        for i in range(len(master_list)):
            delivery_node = master_list[i]['Delivery Node']
            self.untouched[delivery_node] = None
            self.untouched['hub'] = 0

        # This while loop is the dijkstra algorithm. It will keep running until all of the items
        # from our untouched dictionary are moved into the touched dictionary.
        # This while loop has a Big O complexity of (O(n^2)).
        while len(self.untouched) > 0:
            print(a.untouched)
            print(a.touched)
            # This for loop will take the keys and values from our distances graph and
            # use them as comparison items to our touched/untouched dictionaries.
            # The big o complexity for this loop is (O(N)).
            for neighbor, dist in distances[self.current_node].items():
                # The the key is not in our untouched list, we can skip it in order
                # to ensure accuracy.
                if neighbor not in self.untouched:
                    continue

                new_distance = self.current_distance + dist

                # The big O complexity for this if loop is (O(1)).
                if self.untouched[neighbor] is None or self.untouched[neighbor] > new_distance:
                    self.untouched[neighbor] = new_distance

            # Here we sort the items with our key being lambda x, in order to ensure
            # that the lowest distance is put at the front of the list.
            sorted_nodes = sorted(
                distances[self.current_node].items(), key=lambda x: x[1])

            # Here we set the current node to the current distance.
            # Once it has made it into the touched dictionary, we can then remove
            # it from our untouched dictionary so the program can continue.
            self.touched[self.current_node] = self.current_distance
            del self.untouched[self.current_node]

            # This for loop is what determines what will be the next key/value for our
            # current_node and current_distance. It will check the first item in the list
            # and see if it is in the untouched dictionary. If it is, we simply use that key/value.
            # If it isn't we continue looping through until we find one that is in untouched.
            # Also, because we sorted the nodes based on value previously, we can ensure that
            # the first item found is going to be the correct one.
            # The big O complexity for this for loop is (O(N))
            for i in range(len(sorted_nodes)):
                if sorted_nodes[i][0] in self.untouched:
                    self.current_node = sorted_nodes[i][0]
                    self.current_distance = sorted_nodes[i][1]
                    break
                else:
                    self.current_node = sorted_nodes[i][0]
                    self.current_distance = sorted_nodes[i][1]

    # This function is exactly the same as the truck_one function. The only differences are
    # the variable names. Complexities and other such things are identical.
    def truck_two(self, list_2):
        for i in range(len(list_2)):
            delivery_node_2 = list_2[i]['Delivery Node']
            self.untouched_2[delivery_node_2] = None
            self.untouched_2['hub'] = 0

        while len(self.untouched_2) > 0:
            for neighbor, dist in distances[self.current_node_2].items():
                if neighbor not in self.untouched_2:
                    continue

                new_distance = self.current_distance_2 + dist

                if self.untouched_2[neighbor] is None or self.untouched_2[neighbor] > new_distance:
                    self.untouched_2[neighbor] = new_distance

            sorted_nodes_2 = sorted(
                distances[self.current_node_2].items(), key=lambda x: x[1])
            self.touched_2[self.current_node_2] = self.current_distance_2

            del self.untouched_2[self.current_node_2]

            for i in range(len(sorted_nodes_2)):
                if sorted_nodes_2[i][0] in self.untouched_2:
                    self.current_node_2 = sorted_nodes_2[i][0]
                    self.current_distance_2 = sorted_nodes_2[i][1]
                    break
                else:
                    self.current_node_2 = sorted_nodes_2[i][0]
                    self.current_distance_2 = sorted_nodes_2[i][1]

    # The truck_three function is exactly the same as the truck_one and truck_two,
    # including complexities and structures.
    def truck_three(self, list_3):
        for i in range(len(list_3)):
            delivery_node = list_3[i]['Delivery Node']
            self.untouched_3[delivery_node] = None
            self.untouched_3['hub'] = 0

        while len(self.untouched_3) > 0:
            for neighbor, dist in distances[self.current_node_3].items():
                if neighbor not in self.untouched_3:
                    continue

                new_distance = self.current_distance_3 + dist

                if self.untouched_3[neighbor] is None or self.untouched_3[neighbor] > new_distance:
                    self.untouched_3[neighbor] = new_distance

            sorted_nodes_3 = sorted(
                distances[self.current_node_3].items(), key=lambda x: x[1])
            self.touched_3[self.current_node_3] = self.current_distance_3

            del self.untouched_3[self.current_node_3]

            if not self.untouched_3:
                break

            for i in range(len(sorted_nodes_3)):
                if sorted_nodes_3[i][0] in self.untouched_3:
                    self.current_node_3 = sorted_nodes_3[i][0]
                    self.current_distance_3 = sorted_nodes_3[i][1]
                    break
                else:
                    self.current_node_3 = sorted_nodes_3[i][0]
                    self.current_distance_3 = sorted_nodes_3[i][1]


# For this part of the code, we set the variable a to the dj_algorithm class.
# Once that is complete, we simply pass our truck lists through each of the functions
# in the class.
a = dj_algorithm()
a.truck_one(priority_truck)
a.truck_two(truck_2)
a.truck_three(truck_3)

# Once this is complete, our next step is to deliver the packages, which will be in
# the Delivery.py file.
