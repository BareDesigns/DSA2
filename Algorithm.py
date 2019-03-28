# Jonathan Nguyen; #000918228

import sys
import json
import operator
import datetime
from Trucks import *
from Graph import *

start_time = datetime.datetime(2019, 3, 31, 8, 00)
new_start_time = datetime.datetime(2019, 3, 31, 8, 00)


class dj_algorithm:
    '''This class holds all of the different trucks and the information in them'''

    def __init__(self):
        '''Initialize all of the variable that will be used in the trucks'''
        self.speed = 0
        self.new_time = datetime.timedelta(minutes=0)
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

    def truck_one(self, master_list):
        # The for loop will append only the truck values to the untouched list
        for i in range(len(master_list)):
            delivery_node = master_list[i]['Delivery Node']
            self.untouched[delivery_node] = None
            self.untouched['hub'] = 0

        # The while loop will continue until all of the necessary nodes have been visited
        # This main function has a big O notation of big O(n^2)
        while len(self.untouched) > 0:
            # for loop to compare keys,values to untouched list
            for neighbor, dist in distances[self.current_node].items():
                # if the key is not in the untouched, ignore it and move on
                if neighbor not in self.untouched:
                    continue

                # set the new distance to the dict value and add it to the current distance
                new_distance = self.current_distance + dist
                # the "speed" is used to calculate how much time has passed between the nodes
                speed = int(new_distance * 3.33)
                # set the time variable to add the "speed" minutes to the time
                new_time = start_time + datetime.timedelta(minutes=speed)

                # the if loop will apply the lower distance
                if self.untouched[neighbor] is None or self.untouched[neighbor] > new_distance:
                    self.untouched[neighbor] = new_distance

            # The for loop will check if the node is in the imported list
            # if the node is found, change the delivery time to the new time
            for i in range(len(master_list)):
                if self.current_node == master_list[i]['Delivery Node']:
                    foo = master_list[i]['Package_ID']
                    data['Packages'][foo-1]['Delivery Time'] = new_time.time()

            # set the sorted_nodes to the items distances, from smallest to largest
            sorted_nodes = sorted(
                distances[self.current_node].items(), key=lambda x: x[1])

            # Set the current node to the current distance
            self.touched[self.current_node] = self.current_distance

            # Delete the current node from the untouched list so that we don't visit them again
            del self.untouched[self.current_node]

            # This for loop will check the sorted nodes values to the untouched list
            # If it is not in the untouched list, we don't need to set the current node to that value
            for i in range(len(sorted_nodes)):
                # if sorted_nodes is in untouched, go ahead and set the values and quit the for loop
                if sorted_nodes[i][0] in self.untouched:
                    self.current_node = sorted_nodes[i][0]
                    self.current_distance = sorted_nodes[i][1]
                    break
                # if not in untouched, keep looking until one is found
                else:
                    self.current_node = sorted_nodes[i][0]
                    self.current_distance = sorted_nodes[i][1]

            ''' This will set the total distance to the sum of the values in all 
            the touched dictionary. This will be compared for truck 3 to so the 
            truck that arrives back first is used by the next driver'''
            self.total_distance_1 = int(sum(self.touched.values()) * 2)

    def truck_two(self, list_2):
        '''This function is the same as truck_one, save the variable names'''
        for i in range(len(list_2)):
            delivery_node_2 = list_2[i]['Delivery Node']
            self.untouched_2[delivery_node_2] = None
            self.untouched_2['hub'] = 0

        while len(self.untouched_2) > 0:
            for neighbor, dist in distances[self.current_node_2].items():
                if neighbor not in self.untouched_2:
                    continue

                new_distance = self.current_distance_2 + dist
                speed = int(new_distance * 3.33)
                new_time = start_time + datetime.timedelta(minutes=speed)

                if self.untouched_2[neighbor] is None or self.untouched_2[neighbor] > new_distance:
                    self.untouched_2[neighbor] = new_distance

            for i in range(len(list_2)):
                if self.current_node_2 == list_2[i]['Delivery Node']:
                    foo = list_2[i]['Package_ID']
                    data['Packages'][foo-1]['Delivery Time'] = new_time.time()

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

            self.total_distance_2 = int(sum(self.touched_2.values()) * 2)

    def truck_three(self, list_3):
        '''This function is the same as the first 2, save for the new_start_time change'''
        global new_start_time

        # The new_time is set to the shortest time back
        if self.total_distance_1 > self.total_distance_2:
            new_start_time = start_time + datetime.timedelta(
                minutes=int(self.total_distance_2*3.33))
        else:
            new_start_time = start_time + datetime.timedelta(
                minutes=int(self.total_distance_1*3.33))

        for i in range(len(list_3)):
            delivery_node = list_3[i]['Delivery Node']
            self.untouched_3[delivery_node] = None
            self.untouched_3['hub'] = 0

        while len(self.untouched_3) > 0:
            for neighbor, dist in distances[self.current_node_3].items():
                if neighbor not in self.untouched_3:
                    continue

                new_distance = self.current_distance_3 + dist
                speed = int(new_distance * 3.33)
                new_time = new_start_time + datetime.timedelta(minutes=speed)

                if self.untouched_3[neighbor] is None or self.untouched_3[neighbor] > new_distance:
                    self.untouched_3[neighbor] = new_distance

            for i in range(len(list_3)):
                if self.current_node_3 == list_3[i]['Delivery Node']:
                    foo = list_3[i]['Package_ID']
                    data['Packages'][foo-1]['Delivery Time'] = new_time.time()

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
