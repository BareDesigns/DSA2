# Jonathan Nguyen; #000918228

from Graph import *
from HashTable import *
from Trucks import *
from Algorithm import *

# set the variable a to the dj_algorithm class
a = dj_algorithm()

# run the trucks through the functions
a.truck_one(priority_truck)
a.truck_two(truck_2)
a.truck_three(truck_3)

# The while loop will show the package statuses until a key interrupt is input
while True:
    # Any key input will run the loop again
    paused = input('')

    # Print the current time at the top of the loop
    print(f'CURRENT TIME: {start_time.time()}')

    # This for loop will run through the lists and also compare times in order to show statuses
    for i in range(40):
        # set variables
        id = data['Packages'][i]['Package_ID']
        status = data['Packages'][i]['Delivery Status']
        deliv_time = data['Packages'][i]['Delivery Time']

        # if the start time is greater then the delivery time, the package is delivered
        if str(start_time.time()) > str(data['Packages'][i]['Delivery Time']):
            print(f'Package {id} - Delivered at {deliv_time}')

        else:
            print(f'Package {id} - waiting to be delivered')

    # add 5 minutes per enter in order to check the package statuses
    start_time += datetime.timedelta(minutes=5)
