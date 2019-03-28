# Jonathan Nguyen; #000918228

import json


class Packages:
    ''' In this Packages class we are adding functions to setup the hashtable. The functions
    that I am including is init, to initialize our hash table. The next is the add() function, which
    will require the user to pass a package element, and use a hash key to add it to our table. The search()
    function will hash the passed variable and see if it exists in our hash table. If it does not, it will simply return none.
    Finally, the remove() function will first search for the hash key, and if it exists, remove the package from the table.'''

    # The first function is the __init__ one, which passes only self.
    # This function will be used to setup the dictionary for our hash table.
    def __init__(self):
        self.table = {}

    # The add function passes a package from our JSON table and matches the hash with the
    # Package_ID. After that, it will append the package to our hash table according to the hash key.
    # For scalability, as long as each package ID is unique this should be able to scale indefinitely.
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
