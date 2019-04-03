# Read the details from the blood_banks table.
# SELECT *
# FROM blood_banks
#
# Join states table to the blood_banks table based on the foriegn keys.
# SELECT *
# FROM blood_banks
#     JOIN states
#       ON states.id = people.state_id
#
# Join inventories table to the blood_banks and states tables based on the foriegn keys.
# SELECT *
# FROM blood_banks
#     JOIN states
#       ON states.id = people.state_id
#     JOIN inventories
#       ON inventories.blood_bank_id = blood_banks.id
#
# Group people by the states they live are living in.
# SELECT *
# FROM blood_banks
#     JOIN states
#       ON states.id = people.state_id
#     JOIN inventories
#       ON inventories.blood_bank_id = blood_banks.id
# GROUP BY states.names
#
# Also, group people by the blood types to figure out statistics.
# SELECT *
# FROM blood_banks
#     JOIN states
#       ON states.id = people.state_id
#     JOIN inventories
#       ON inventories.blood_bank_id = blood_banks.id
# GROUP BY states.names, inventories.blood_type
#
# Select columns to export the information required, statewise blood type, blood type availabilty, blood banks and states.
# SELECT states.name AS State_name, inventories.blood_type AS Blood_Type, SUM(inventories.quantity_cc) AS Available_Blood, blood_banks.name AS BloodBank_Name
# FROM blood_banks
#     JOIN states
#       ON states.id = people.state_id
#     JOIN inventories
#       ON inventories.blood_bank_id = blood_banks.id
# GROUP BY states.names, inventories.blood_type
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
    analysis2_sql = """SELECT states.name AS State_name, inventories.blood_type AS Blood_Type, SUM(inventories.quantity_cc) AS
                        Available_Blood, blood_banks.name AS BloodBank_Name FROM blood_banks JOIN states
                        ON blood_banks.state_id = states.id JOIN inventories ON inventories.blood_bank_id =
                        blood_banks.id GROUP BY states.name, inventories.blood_type """

    # using the functions from the python libraries, executing the query to extract the data
    cursor.execute(analysis2_sql)
    # storing the data executed above in a temporary list
    results = cursor.fetchall()
    # reading the column names of the database table to keep them as headers while writing data into csv
    column_names = results[0].keys()

    # opening the named csv, "analysis2.csv" and writing the data into the csv with the use of function 'w'
    with open('analysis2.csv', 'w') as csvfile:

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
