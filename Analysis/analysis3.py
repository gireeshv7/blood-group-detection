# Reading person information from the people table.
# SELECT *
# FROM people
#
# joining states table to know how many people stay in those respective states.
# SELECT *
# FROM people
#     JOIN states
#       ON states.id = people.state_id
#
# joining blood_banks table to determine the blood banks in every state.
# SELECT *
# FROM people
#     JOIN states
#       ON states.id = people.state_id
#     JOIN blood_banks
#       ON blood_banks.state_id = states.id
#
# joining inventories table to find out the availability of blood types in respective states.
# SELECT *
# FROM people
#     JOIN states
#       ON states.id = people.state_id
#     JOIN blood_banks
#       ON blood_banks.state_id = states.id
#     JOIN inventories
#       ON inventories.blood_bank_id = blood_banks.id
#
# determining the amount of blood required from the blood bank for a person where the blood bank and person are in the same state.
# SELECT *
# FROM people
#     JOIN states
#       ON states.id = people.state_id
#     JOIN blood_banks
#       ON blood_banks.state_id = states.id
#     JOIN inventories
#       ON inventories.blood_bank_id = blood_banks.id
# WHERE people.first_name = "Ilene" and people.blood_type = inventories.blood_type and inventories.quantity_cc > '4000'
#
# grouping it by blood types to match the blood type in the inventory and the donee's blood type
# SELECT *
# FROM people
#     JOIN states
#       ON states.id = people.state_id
#     JOIN blood_banks
#       ON blood_banks.state_id = states.id
#     JOIN inventories
#       ON inventories.blood_bank_id = blood_banks.id
# WHERE people.first_name = "Ilene" and people.blood_type = inventories.blood_type and inventories.quantity_cc > '4000'
# GROUP BY inventories.blood_type
#
# selecting columns of person name, bllod type, quantity available, blood bank details and state name
# SELECT concat(people.first_name,' ' , people.last_name) AS Person_Name, people.blood_type AS Blood_Type, inventories.quantity_cc AS Quantity_of_Blood, states.name AS State_name,
# blood_banks.name AS Blood_Bank_name, blood_banks.website AS BB_Website, blood_banks.contact AS BB_Contact
# FROM people
#     JOIN states
#       ON states.id = people.state_id
#     JOIN blood_banks
#       ON blood_banks.state_id = states.id
#     JOIN inventories
#       ON inventories.blood_bank_id = blood_banks.id
# WHERE people.first_name = "Ilene" and people.blood_type = inventories.blood_type and inventories.quantity_cc > '4000'
# GROUP BY inventories.blood_type
# import the relevant python libraries to use the functionalities.
import pymysql.cursors
import pprint
import csv

# Set up connection with database using the connection variable below
connection = pymysql.connect(
            host="localhost", # server details
            user="milind_siddhanti",  # username for authentication
            passwd="nokiayu7k",  # password to connect with the database
            db="milind_siddhanti_project", # schema name of the database
            autocommit=True, # executes commit functionality in database
            cursorclass=pymysql.cursors.DictCursor # python libraries
            )

# with successful database connection, read data from the database
with connection.cursor() as cursor:

    # build up of the SQL query is shown at the start of the file
    analysis3_sql = """SELECT concat(people.first_name,' ' , people.last_name) AS Person_Name, people.blood_type AS Blood_Type, inventories.quantity_cc AS Quantity_of_Blood, states.name AS State_name,
                        blood_banks.name AS Blood_Bank_name, blood_banks.website AS BB_Website, blood_banks.contact AS BB_Contact FROM people
                        JOIN states ON states.id = people.state_id JOIN blood_banks ON blood_banks.state_id = states.id JOIN inventories ON inventories.blood_bank_id = blood_banks.id
                        WHERE people.id in ("1", "20", "87", "98") and people.blood_type = inventories.blood_type
                        and inventories.quantity_cc > '400' GROUP BY inventories.blood_type"""

    # using the functions from the python libraries, executing the query to extract the data
    cursor.execute(analysis3_sql)
    # storing the data executed above in a temporary list
    results = cursor.fetchall()
    # reading the column names of the database table to keep them as headers while writing data into csv
    column_names = results[0].keys()

    # opening the named csv, "analysis3.csv" and writing the data into the csv with the use of function 'w'
    with open('analysis3.csv', 'w') as csvfile:

        # writing the data into the csv using functions like, delimiter to limit the values with a comma in this case,
        # reading the values from the database inside the quotes and with the column names extracted before.
        myCsvWriter = csv.DictWriter(csvfile,
                                     delimiter=',',
                                     quotechar='"',
                                     fieldnames = column_names)
        myCsvWriter.writeheader()

        # going through each and every row of the results of the SQL query and writing into the csv used, "analysis1.csv"
        for row in results:

            # writing each row of values in results to the csv file format for better analysis purpose
            myCsvWriter.writerow(row)
