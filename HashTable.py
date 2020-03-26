# Jonathan Nguyen; #000918228

"""HashTable.py: The purpose of this file is to create a dictionary hash table
using a class and functions. Included will be an add function,
a search function, and a remove function."""

import json


class Packages:
    """ In this Packages class we are adding functions to setup the hashtable. The functions
    that I am including is init, to initialize our hash table. The next is
    the add() function, which will require the user to pass a package element,
    and use a hash key to add it to our table. The search() function will hash
    the passed variable and see if it exists in our hash table.
    If it does not, it will simply return none.
    Finally, the remove() function will first search for the hash key,
    and if it exists, remove the package from the table."""

    # The first function is the __init__ one, which passes only self.
    # This function will be used to setup the dictionary for our hash table.
    def __init__(self):
        self.table = {}

    # The add function passes a package from our JSON table and matches the hash with the
    # Package_ID. After that, it will append the package to our hash table according to the hash key.
    # For scalability, as long as each package ID is unique this should be able to scale indefinitely.
    # The big O complexity for this function is O((c)).
    def add(self, package):
        key = hash(package["Package_ID"])
        self.table[package["Package_ID"]] = package

    # The search function passes an ID inputted by the user, runs the hash on the ID, and returns the
    # package information if the key is found in the table. If it is not found, it returns does not exist.
    # The big O complexity for this function is (O(c)).
    def search(self, ID):
        key = hash(ID)

        if key in self.table:
            return self.table[key]
        else:
            return "This package does not exist."

    # The remove function will pass an ID inputted by the user, and set the key to the
    # hash value of that ID. If the key is found in the hashtable, the function will remove
    # the data from the hashtable. If it is not found, it will simply do nothing.
    # The big O complexity for this function is (O(c)).
    def remove(self, ID):
        key = hash(ID)

        if key in self.table:
            self.table.pop(key)


# To keep things simple, the first thing we are going to do is set our variables, so that it is more
# readable and easy to understand. We first set p to the Packages class, and then we will set data
# as a variable for the loaded JSON file.
p = Packages()
data = json.load(open("Package_data.json"))

# Instead of manually adding every single package to our hash table using the add function in the
# Packages class, we will simply run a for loop set to the length of our data list in the JSON file.
# In the for loop, we set the variable "package_id" to the package number found in the JSON data file.
# Once that is done, we simply add the package data to our hash table using the p.add() function.
# The big O complexity for this for loop is (O(n)).
for i in range(len(data["Packages"])):
    package_id = data["Packages"][i]
    p.add(package_id)


# From here, we will need to initialize our data graphs, which is the Graph.py file.
