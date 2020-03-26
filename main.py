# Jonathan Nguyen; #000918228

"""main.py: This program's purpose is to provide the user an option to look up package
details on an individual basis, or on a whole at any given time throughout the day."""

from Delivery import *


# The while loop will as a series of questions which require input from the user.
# Depending on what they choose, the program will navigate them on the preset
# path to give the user what information they were searching for.
while True:

    question = input(
        "\nIs there a specific package number you want to see the details of? Y/N \n"
    )

    # Here we ask if the user is looking for information on a sole package.
    # If so, we use the hash table search function built in Hashtable.py.
    # The big O complexity for this is (O(1)).
    if question.upper() == "Y":
        package_number = int(input("\nWhat is the package number?\n"))
        package_information = p.search(package_number)
        print(f"\nPackage #{package_number}:\n{package_information}")

    # If the user wants to see the status of all the packages, they are able
    # to pick the time (24 hour format) and it will return where the packages
    # are at that given time.
    else:
        total_list = input("\nDo you want to see the status of all the packages? Y/N\n")

        # The big O complexity for this loop is (O(1)).
        if total_list.upper() == "Y":
            time_question = input(
                "\nFor what time do you want to see their status? (13:00:00)\n"
            )

            # This for loop sets variables for our package information in order to
            # make the print statement cleaner. It will loop up the ID and time
            # and return that information to the user.
            # The big O complexity for this loop is (O(N)).
            for i in range(1, len(p.table) + 1):
                package_id = p.table[i]["Package_ID"]
                status = p.search(i)
                final_status = status["Delivery Status"]
                delivery_time = status["Delivery Time"]
                # If the time inputted is greater than the delivered time, this
                # means that the package has already been delivered. If that
                # happens we simply return the delivery time for those packages.
                # The big O complexity for this loop is (O(1)).
                if str(time_question) > str(delivery_time):
                    print(f"Package {package_id} was delivered at {delivery_time}")
                else:
                    print(f"Package {package_id} status is {final_status}")

        # Should the user only want to see the mileage for the trucks, we ask that question
        else:
            miles_answer = input(
                "\nWould you like to see the total distances of the trucks at the end of they day?\n"
            )

            # if the user answers Y, we pull the total distance information from Delivery.py
            # and give that end information to the user.
            # The big O complexity for this is (O(1)):
            if miles_answer.upper() == "Y":

                # In order to get a better view of all the trucks distances, we make
                # a total_overall_distance variable to show the sum of the three trucks
                total_overall_distance = (
                    d.total_distance_1 + d.total_distance_2 + d.total_distance_3
                )

                # Here we print the mileage information for the user
                print(
                    f"""\nThe total miles for truck 1: {d.total_distance_1} miles
                    truck 2: {d.total_distance_2} miles
                    truck 3: {d.total_distance_3} miles
                    All trucks: {total_overall_distance} miles"""
                )

            # If the user wants none of these things, we print goodbye and break the loop
            else:
                print("Goodbye!\n")
                break

# Once the user selects no for everything, the program simply prints goodbye and exits.
