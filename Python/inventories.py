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

    # SELECT statement to fetch the blood bank ids - to generate a connection between the database tables using the primary key and foreign key relation
    select_blood_bank = "SELECT id from blood_banks WHERE website = %(website)s"

    # inserting data into the database table columns with the below query
    insert_inventories = """INSERT INTO inventories(quantity_cc,blood_type,blood_bank_id)
                    VALUE (%(quantity_cc)s, %(blood_type)s, %(blood_bank_id)s)"""

    # open the csv file and read the data from the csv file.
    with open('inventories.csv') as csvfile:
        # specifying the type of csv format used so that python knows and can format the file.
        myCSVReader = csv.DictReader(csvfile, delimiter=",", quotechar='"')

        # reading each and every row from the csv to validate the data, make corrections to the data,
        # and store the data in a temporary variable.
        for row in myCSVReader:

            # executing the SELECT query to fetch all the states id from the states database table which was created earlier.
            cursor.execute(select_blood_bank, row)
            # storing the results in a list. Using fetchone() function since each query executed fetches single record. For better performance using the fetchone() functionality.
            results = cursor.fetchone()
            # eliminating null values
            if(results!=()):
                blood_bank_id = results['id']

            # storing changes made to the data in a dictionary as a key, value pair to insert the validated and corrected data into the database schema table.
            # The key represents the datatase column name so that the data sits in the required database column.
            # The value represents the corrected data that has to be fed into the database columns.
            # creating dictionary, "my_dict" with key, value pairs.
            my_dict = {'blood_bank_id': blood_bank_id,
                          'quantity_cc': row['quantity_cc'],
                          'blood_type': row['blood_type']}

            # using the functions from the python libraries, reading data from the temporary dictionary which was intially read from the csv,
            # and executing the sql query which inserts the data into the database columns.
            cursor.execute(insert_inventories, my_dict)
