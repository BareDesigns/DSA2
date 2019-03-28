# Jonathan Nguyen; #000918228
from HashTable import *

# Initialize our trucks for use
priority_truck = []
truck_2 = []
truck_3 = []


# The for loop will run and append our values to each truck
for i in range(1, len(p.table)+1):
    # The priority truck gets all the packages with an actual deadline
    if p.table[i]['Delivery Deadline'] != "5:00 PM" and len(priority_truck) < 16:
        priority_truck.append(p.table[i])
    # Truck 2 gets the maximum capacity of 16
    elif len(truck_2) < 16:
        truck_2.append(p.table[i])
    # Truck 3 gets the remaining packages
    else:
        truck_3.append(p.table[i])
