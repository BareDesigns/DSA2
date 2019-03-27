import json


class Packages:
    '''This class is the bedrock of making the package hastable, finding
    the hash bucket if it exists, and removing it if necessary'''

    # make the initial list for packages to be put into
    def __init__(self, blocks=10):
        self.table = []
        for i in range(blocks):
            self.table.append([])

    # Add the Package details to the Hash Table, make a bucket that will store the hash key
    def add(self, item):
        # bucket = hash(item[0]['Package_ID']) % len(self.table)
        bucket = hash(item[0]) % len(self.table)
        bucket_list = self.table[bucket]

        # Add the package to the hash table
        bucket_list.append(item)

    # Use package_ID to search indexes and see if exists within Hash Table
    def search(self, ID):
        bucket = hash(ID[0]) % len(self.table)
        bucket_list = self.table[bucket]

        # If ID is found through Hash Key, statement will return the information
        if ID in bucket_list:
            package_index = bucket_list.index(ID)
            return bucket_list[package_index]
        # If ID is not found, return NONE
        else:
            return None

    # Function to find and remove an item from the Package Table
    def remove(self, ID):
        bucket = hash(ID[0]) % len(self.table)
        bucket_list = self.table[bucket]

        # If ID is found, will remove from hash table
        if ID in bucket_list:
            bucket_list.remove(ID)


# Set p as the package variable for ease of use
p = Packages()

# Load the JSON file in order to append the data to the Hash Table
data = json.load(open('Package_data.json'))
package_list = []

for i in range(1):
    ID = data['Packages'][i]['Package_ID']
    total = data['Packages'][i]
    fooga = data['Packages'][i]['Package_Name']
    name = ID, total
    p.add(name)
    print(p.table)
    print(p.search(fooga))
    print(p.search(name))

foo = data['Packages'][0]['Package_Name']
