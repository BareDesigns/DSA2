# Jonathan Nguyen; #000918228

'''Trucks.py: The purpose of this file is to assign our packages
to the trucks based on maximum capacity, and delivery deadlines.'''

from HashTable import *

# The first thing we will do is initialize our trucks as lists.
# The first truck is named priority_truck because we will append
# those values that have a deadline different than 5:00 PM(EOD).
# Each list will be empty at the start.
priority_truck = []
truck_2 = []
truck_3 = []


''' This for loop will start by looking up the time deadline in the hash table. If
the value is anything other than 5: 00 PM, this means that it needs to be delivered first,
as 5: 00 PM is the very last time of the day. Another catch is that the trucks can hold
at most 16 packages, so when the length of each list in the truck reaches 16, the loop
will append the packages to the next available truck. Once the package is a particular truck,
the delivery status of the package is changed to say that it is on the truck  # .'''


# The for loop goes in the range of 1, to the length of our hashtable+1. This range
# is set because 0 is not in the table, and we want to append all of the packages
# to a truck, so we need the range to stop at 1 + the length of our list.
# The big O complexity for this for loop is (O(n)).
for i in range(1, len(p.table)+1):

    # Here we set the variables package_id, and delivery_status to their respective
    # values in the hash table. This will be so that we can append and update the
    # values with the truck information.
    package_id = p.table[i]['Package_ID']
    delivery_status = p.search(package_id)

    # This if statement will check our delivery deadline by searching the key's
    # Delivery Deadline value and seeing if it is anything other than 5:00 PM (EOD).
    # Once each truck sequentially has reached the maximum carrying capacity, done by
    # checking the length of the list, the loop will move and append the
    # items to the next truck.
    # The big O complexity for if, elif, and else is (O(n)).
    if p.table[i]['Delivery Deadline'] != "5:00 PM" and len(priority_truck) < 16:
        priority_truck.append(p.table[i])
        delivery_status['Delivery Status'] = 'On Truck 1'

    elif len(priority_truck) < 16:
        priority_truck.append(p.table[i])
        delivery_status['Delivery Status'] = 'On Truck 1'

    # Priority Truck is full, so now we append at most 16 packages to the truck_2 list.
    elif len(truck_2) < 16:
        truck_2.append(p.table[i])
        delivery_status['Delivery Status'] = 'On Truck 2'

    # Once the other 2 trucks are full, truck_3's list gets the remaining packages.
    else:
        truck_3.append(p.table[i])
        delivery_status['Delivery Status'] = 'On Truck 3'

# Next, we need to find the shortest path for each trucks packages, so we will
# continue by moving to the Algorithm.py file.

print(len(priority_truck))
print(len(truck_2))
print(len(truck_3))
