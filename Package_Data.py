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

# Make the package variables, with the Package Key first, and the remaining data afterwards
package_1 = [data['Packages'][0]['Package_ID'], data['Packages'][0]]
package_2 = [data['Packages'][1]['Package_ID'], data['Packages'][1]]
package_3 = [data['Packages'][2]['Package_ID'], data['Packages'][2]]
package_4 = [data['Packages'][3]['Package_ID'], data['Packages'][3]]
package_5 = [data['Packages'][4]['Package_ID'], data['Packages'][4]]
package_6 = [data['Packages'][5]['Package_ID'], data['Packages'][5]]
package_7 = [data['Packages'][6]['Package_ID'], data['Packages'][6]]
package_8 = [data['Packages'][7]['Package_ID'], data['Packages'][7]]
package_9 = [data['Packages'][8]['Package_ID'], data['Packages'][8]]
package_10 = [data['Packages'][9]['Package_ID'], data['Packages'][9]]
package_11 = [data['Packages'][10]['Package_ID'], data['Packages'][10]]
package_12 = [data['Packages'][11]['Package_ID'], data['Packages'][11]]
package_13 = [data['Packages'][12]['Package_ID'], data['Packages'][12]]
package_14 = [data['Packages'][13]['Package_ID'], data['Packages'][13]]
package_15 = [data['Packages'][14]['Package_ID'], data['Packages'][14]]
package_16 = [data['Packages'][15]['Package_ID'], data['Packages'][15]]
package_17 = [data['Packages'][16]['Package_ID'], data['Packages'][16]]
package_18 = [data['Packages'][17]['Package_ID'], data['Packages'][17]]
package_19 = [data['Packages'][18]['Package_ID'], data['Packages'][18]]
package_20 = [data['Packages'][19]['Package_ID'], data['Packages'][19]]
package_21 = [data['Packages'][20]['Package_ID'], data['Packages'][20]]
package_22 = [data['Packages'][21]['Package_ID'], data['Packages'][21]]
package_23 = [data['Packages'][22]['Package_ID'], data['Packages'][22]]
package_24 = [data['Packages'][23]['Package_ID'], data['Packages'][23]]
package_25 = [data['Packages'][24]['Package_ID'], data['Packages'][24]]
package_26 = [data['Packages'][25]['Package_ID'], data['Packages'][25]]
package_27 = [data['Packages'][26]['Package_ID'], data['Packages'][26]]
package_28 = [data['Packages'][27]['Package_ID'], data['Packages'][27]]
package_29 = [data['Packages'][28]['Package_ID'], data['Packages'][28]]
package_30 = [data['Packages'][29]['Package_ID'], data['Packages'][29]]
package_31 = [data['Packages'][30]['Package_ID'], data['Packages'][30]]
package_32 = [data['Packages'][31]['Package_ID'], data['Packages'][31]]
package_33 = [data['Packages'][32]['Package_ID'], data['Packages'][32]]
package_34 = [data['Packages'][33]['Package_ID'], data['Packages'][33]]
package_35 = [data['Packages'][34]['Package_ID'], data['Packages'][34]]
package_36 = [data['Packages'][35]['Package_ID'], data['Packages'][35]]
package_37 = [data['Packages'][36]['Package_ID'], data['Packages'][36]]
package_38 = [data['Packages'][37]['Package_ID'], data['Packages'][37]]
package_39 = [data['Packages'][38]['Package_ID'], data['Packages'][38]]
package_40 = [data['Packages'][39]['Package_ID'], data['Packages'][39]]

# Add the created package variables to the Hash Table
p.add(package_1)
p.add(package_2)
p.add(package_3)
p.add(package_4)
p.add(package_5)
p.add(package_6)
p.add(package_7)
p.add(package_8)
p.add(package_9)
p.add(package_10)
p.add(package_11)
p.add(package_12)
p.add(package_13)
p.add(package_14)
p.add(package_15)
p.add(package_16)
p.add(package_17)
p.add(package_18)
p.add(package_19)
p.add(package_20)
p.add(package_21)
p.add(package_22)
p.add(package_23)
p.add(package_24)
p.add(package_25)
p.add(package_26)
p.add(package_27)
p.add(package_28)
p.add(package_29)
p.add(package_30)
p.add(package_31)
p.add(package_32)
p.add(package_33)
p.add(package_34)
p.add(package_35)
p.add(package_36)
p.add(package_37)
p.add(package_38)
p.add(package_39)
p.add(package_40)
