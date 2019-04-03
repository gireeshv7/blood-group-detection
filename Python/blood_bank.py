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
    # with the help of defining datatypes in python, for ex: %(first_name)s as string, data from the csv is read as string from the respective csv

    # SELECT statement to fetch the state ids - to generate a connection between the database tables using the primary key and foreign key relation
    select_state = "SELECT id from states WHERE name = %(state)s"

    # inserting data into the database table columns with the below query
    insert_blood_bank = """INSERT INTO blood_banks(state_id,name,website,contact)
                    VALUE (%(state_id)s, %(name)s, %(website)s, %(contact)s)"""

    # open the csv file and read the data from the csv file.
    with open('blood_bank.csv') as csvfile:
        # specifying the type of csv format used so that python knows and can format the file.
        myCSVReader = csv.DictReader(csvfile, delimiter=",", quotechar='"')

        # reading each and every row from the csv to validate the data, make corrections to the data,
        # and store the data in a temporary variable.
        for row in myCSVReader:

            # executing the SELECT query to fetch all the states id from the states database table which was created earlier.
            cursor.execute(select_state, row)
            # storing the results in a list. Using fetchone() function since each query executed fetches single record. For better performance using the fetchone() functionality.
            results = cursor.fetchone()
            # eliminating null values
            if(results != ()):
                state_id = results['id']

            # storing changes made to the data in a dictionary as a key, value pair to insert the validated and corrected data into the database schema table.
            # The key represents the datatase column name so that the data sits in the required database column.
            # The value represents the corrected data that has to be fed into the database columns.
            # creating dictionary, "my_dict" with key, value pairs.
            my_dict = {'state_id': state_id,
                          'name': row['name'],
                          'website': row['website'],
                          'contact': row['contact']}

            # using the functions from the python libraries, reading data from the temporary dictionary which was intially read from the csv,
            # and executing the sql query which inserts the data into the database columns.
            cursor.execute(insert_blood_bank, my_dict)
