import json


class Packages:
    '''The package class handles the add, remove, and 
    search functions for the hash table'''

    # __init__ will initialize the hashtable/dictionary
    def __init__(self):
        self.table = {}

    # the add function takes the hash of th package ID and adds it to
    # the table
    def add(self, package):
        key = hash(package['Package_ID'])
        self.table[package['Package_ID']] = package

    # this function finds a key and returns the value if it exists
    def search(self, ID):
        key = hash(ID['Package_ID'])

        if key in self.table:
            return self.table[key]
        else:
            return None

    # this function finds a key and deletes the value if it exists
    def remove(self, ID):
        key = hash(ID['Package_ID'])

        if key in self.table:
            self.table.pop(key)


# set p as the variable for the package class
p = Packages()
# set data as the variable for the JSON file
data = json.load(open('Package_data.json'))

# the for loop will run through our JSON and append the values to the
# Hash table
for i in range(len(data['Packages'])):
    foo = data['Packages'][i]
    p.add(foo)
