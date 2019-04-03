# Read the person details from the people table.
# SELECT *
# FROM people
#
# Join states table to the people table based on the foriegn keys.
# SELECT *
# FROM people
#     JOIN states
#       ON states.id = people.state_id
#
# Group people by the states they live are living in.
# SELECT *
# FROM people
#     JOIN states
#       ON states.id = people.state_id
# GROUP BY states.id
#
# Also, group people by the blood types to figure out statistics.
# SELECT *
# FROM people
#     JOIN states
#       ON states.id = people.state_id
# GROUP BY states.id, people.blood_type
#
# Select columns to export the information required, count of people, the blood type and states.
# SELECT states.name, people.blood_type, COUNT(*) AS Count_of_People_BloodType_in_every_State
# FROM people
#     JOIN states
#       ON states.id = people.state_id
# GROUP BY states.id, people.blood_type

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
    analysis1_sql = """SELECT states.name, people.blood_type, COUNT(*) AS Count_of_People_BloodType_in_every_State FROM people
                        JOIN states ON states.id = people.state_id GROUP BY states.id, people.blood_type """

    # using the functions from the python libraries, executing the query to extract the data
    cursor.execute(analysis1_sql)
    # storing the data executed above in a temporary list
    results = cursor.fetchall()
    # reading the column names of the database table to keep them as headers while writing data into csv
    column_names = results[0].keys()

    # opening the named csv, "analysis1.csv" and writing the data into the csv with the use of function 'w'
    with open('analysis1.csv', 'w') as csvfile:

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
