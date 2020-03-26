# Jonathan Nguyen; #000918228

"""Delivery.py: This file's purpose is to make a class and functions for delivering packages
based on the shortest path given to us from the algorithm file. Once this has been done, we
will run the main.py file to lookup the total distances and delivery times."""

import math
import datetime
from Algorithm import *

# Here we set the start_time and new_start_time variables to be used to determine
# when our trucks leave.
start_time = datetime.datetime(2019, 3, 31, 8, 00)
new_start_time = datetime.datetime(2019, 3, 31, 8, 00)


class Delivery:
    """The delivery class's purpose is to define 3 functions, one for each truck, in order
    to keep track of and deliver the packages according to the list given by the algorithm.
    As for scalability, each function can simply be copied, with only the variable names
    changed to reflect the truck ID. This means that it should theoretically be able to expand
    or shrink to any size without issue."""

    # The __init__ function is here to set the self variables to be used in our other 3 functions.
    def __init__(self):
        self.start_time = datetime.datetime(2019, 3, 31, 8, 00)
        self.start_time_2 = datetime.datetime(2019, 3, 31, 8, 00)
        self.delivery_time = datetime.timedelta(minutes=0)
        self.speed = 0
        self.total_distance_1 = 0
        self.total_distance_2 = 0
        self.total_distance_3 = 0
        self.last_distance_1 = 0
        self.last_distance_2 = 0
        self.last_distance_3 = 0
        self.current_distance = 0

    # This function's purpose is to use the values and average speed to
    # determine what time the packages will be delivered. Once it has,
    # the function will remove the item from the truck.
    def delivery_truck_one(self, truck_1_list):
        truck_1_list.pop("hub")

        # This simply calculates the total distance the truck traveled.
        # The reason we multiply it by 2 is because it travels out,
        # and then has to travel back the exact same length.
        self.total_distance_1 = int(sum(truck_1_list.values())) + self.last_distance_1

        # This while loop will sets variables, and determines the time of delivery
        # based on the distance time the time it takes to travel 1 mile.
        # The big O complexity for this while loop is (O(N^2)).
        while len(truck_1_list) > 0:
            # The for loop will run through the keys/values and use that
            # to determine the time the package will be delivered based
            # off the speed and total time travel once the node is reached.
            # The big O complexity for this loop is (O(N)).
            for location, distance in truck_1_list.items():

                # This if statement will run when the length of our
                # list is 1. From here, we will check to see how many
                # miles our trucks needs to travel back to the hub.
                # Once that information is gathered, we simply add the value
                # to our total_distance variable to calculate miles traveled.
                # The big O complexity for this is O(1).
                if len(truck_1_list) == 1:
                    for hub, dist in distances[location].items():
                        if hub == "hub":
                            self.last_distance_1 = dist
                # Here we set the speed. At 18 MPH, for each mile traveled
                # is 3.33 minutes. So we simply take the distance and multiply
                # it by 3.33. We use the math.ceil in order to round up the float.
                # The reason for this is it because it gives a more accurate
                # delivery time.
                self.speed = math.ceil(distance * 3.33)

                # This for loop runs through the length of the items in the truck.
                # As the previous loop runs through the keys and values, this loop
                # will check the hash table information to see if the nodes match.
                # If they do, we can change that package data to the time it
                # it was delivered.
                # The big O complexity for this loop is (O(N)).
                for i in range(len(priority_truck)):
                    # This loop changes the delivery time to the one found
                    # when multiplyting the distance traveled by 3.33.
                    # The big O complexity for this loop is (O(N)).
                    if location == priority_truck[i]["Delivery Node"]:
                        self.delivery_time = self.start_time + datetime.timedelta(
                            minutes=self.speed
                        )
                        id = priority_truck[i]["Package_ID"]
                        package = p.search(id)
                        package["Delivery Time"] = self.delivery_time.time()
                # In order to ensure that our start time is based on when the prior
                # package was delivered, we simply add the amount of minutes found
                # when computing the speed and update the minutes based on that.
                self.start_time += datetime.timedelta(minutes=self.speed)
                break
            # Here we remove the current location from the passed list, so that we
            # do not visit it again and so that the loop can break.
            truck_1_list.pop(location)

    def delivery_truck_two(self, truck_2_list):
        # This function is exactly the same as delivery_truck_two, save for a
        # few variable names. The loops and complexities are identical.
        truck_2_list.pop("hub")

        self.total_distance_2 = int(sum(truck_2_list.values())) + self.last_distance_2

        while len(truck_2_list) > 0:
            for location, distance in truck_2_list.items():

                if len(truck_2_list) == 1:
                    for hub, dist in distances[location].items():
                        if hub == "hub":
                            self.last_distance_2 = dist

                self.speed = math.ceil(distance * 3.33)

                for i in range(len(truck_2)):
                    if location == truck_2[i]["Delivery Node"]:
                        self.delivery_time = self.start_time_2 + datetime.timedelta(
                            minutes=self.speed
                        )
                        id = truck_2[i]["Package_ID"]
                        package = p.search(id)
                        package["Delivery Time"] = self.delivery_time.time()

                self.start_time_2 += datetime.timedelta(minutes=self.speed)
                break

            truck_2_list.pop(location)

    def delivery_truck_three(self, truck_3_list):
        # This function is exactly the same as delivery_truck_two, save for a
        # few variable names and the start time. The start time needs to be adjusted
        # because we have to wait for one of thew other trucks to return. We do this by
        # seeing which truck has a shorter overall time. By doing so, we can ensure the
        # quickest delivery possible.
        truck_3_list.pop("hub")
        self.total_distance_3 = int(sum(truck_3_list.values())) + self.last_distance_3

        # This if/else statement simply compares the total time taken for
        # truck one and truck two. Whichever is shorter will be the truck used,
        # and the starting time is also changed to reflect the time the truck
        # returned.
        # The big O complexity for this loop is (O(1)):
        if self.total_distance_1 > self.total_distance_2:
            new_start_time = start_time + datetime.timedelta(
                minutes=int(self.total_distance_2 * 3.33)
            )
        else:
            new_start_time = start_time + datetime.timedelta(
                minutes=int(self.total_distance_1 * 3.33)
            )

        while len(truck_3_list) > 0:
            for location, distance in truck_3_list.items():

                if len(truck_3_list) == 1:
                    for hub, dist in distances[location].items():
                        if hub == "hub":
                            self.last_distance_3 = dist

                self.speed = math.ceil(distance * 3.33)

                for i in range(len(truck_3)):
                    if location == truck_3[i]["Delivery Node"]:
                        self.delivery_time = new_start_time + datetime.timedelta(
                            minutes=self.speed
                        )
                        id = truck_3[i]["Package_ID"]
                        package = p.search(id)
                        package["Delivery Time"] = self.delivery_time.time()
                new_start_time += datetime.timedelta(minutes=self.speed)
                break
            truck_3_list.pop(location)


# Here we set the variable d to the Delivery class.
# Then we simply pass the node list from our algorithm to each one of the
# appropriate functions.
d = Delivery()
d.delivery_truck_one(a.touched)
d.delivery_truck_two(a.touched_2)
d.delivery_truck_three(a.touched_3)

# Now that all the packages have been delivered, we can move to our interface program,
# rightly named Main.py.
