# importing relevant libraries for the python code to execute the functionalities.
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

# with successful database connection, feeding data to the database
with connection.cursor() as cursor:

    # database table should be created in the database schema using phpMyAdmin.
    # choose the columns from the database table into which the data should be fed into.
    # using the SQL INSERT functionality, insert the data into the database table columns as required.
    # with the help of defining datatypes in python, for ex: %(name)s as string data from the csv is read as string from the respective csv

    # inserting data into the database table columns with the below query

    state_sql = """INSERT INTO states(name,population,life_expectancy,abbreviation)
    VALUE (%(name)s,%(population)s,%(life_expectancy)s,%(abbreviation)s)"""

    # open the csv file and read the data from the csv file.
    with open('states.csv') as csvfile:
        # specifying the type of csv format used so that python knows and can format the file.
        myCSVReader = csv.DictReader(csvfile, delimiter=",", quotechar='"')

        # reading each and every row from the csv to validate the data, make corrections to the data,
        # and store the data in a temporary variable.
        for row in myCSVReader:

            # storing the value of the column "name" in a temporary string variable. Ex: state_name_spilt = "AlabamaAL"
            state_name_spilt = row['state_name_combined']
            # spilting the last 2 characters of the string "state_name_spilt" and storing in another temporary string variable as state_name. Ex: state_name = "Alabama"
            state_name = state_name_spilt[:-2]
            # reading the last 2 characters of the string "state_name_spilt" and storing in new temporary string variable, "state_abb". Ex: state_abb = "AL"
            state_abb = state_name_spilt[-2:]

            # storing changes made to the data in a dictionary as a key, value pair to insert the validated and corrected data into the database schema table.
            # The key represents the datatase column name so that the data sits in the required database column.
            # The value represents the corrected data that has to be fed into the database columns.
            # creating dictionary, "my_dict" with key, value pairs.
            my_dict = {'name': state_name,
                        'population': row['population'],
                        'life_expectancy': row['life_expectancy'],
                        'abbreviation': state_abb
                         }

            # using the functions from the python libraries, reading data from the temporary dictionary which was intially read from the csv,
            # and executing the sql query which inserts the data into the database columns.
            cursor.execute(state_sql, my_dict)
