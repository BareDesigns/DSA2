# Jonathan Nguyen; #000918228

from Graph import *
from HashTable import *
from Trucks import *
from Algorithm import *


while True:
    paused = input('')

    print(f'CURRENT TIME: {start_time.time()}')

    for i in range(40):
        id = data['Packages'][i]['Package_ID']
        status = data['Packages'][i]['Delivery Status']
        deliv_time = data['Packages'][i]['Delivery Time']

        if str(start_time.time()) > str(data['Packages'][i]['Delivery Time']):
            print(f'Package {id} - Delivered at {deliv_time}')

        else:
            print(f'Package {id} - waiting to be delivered')

    start_time += datetime.timedelta(minutes=5)
