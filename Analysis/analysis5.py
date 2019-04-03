# Querying the database table inventories
# SELECT * FROM inventories
#
# joining data from database table blood banks for comparing
# SELECT * FROM inventories
# 	JOIN blood_banks
# 	  ON blood_banks.id = inventories.blood_bank_id
#
# joining states database table to compare the inventories for each state
# SELECT * FROM inventories
# 	JOIN blood_banks
# 	  ON blood_banks.id = inventories.blood_bank_id
# 	JOIN states
# 	  ON states.id = blood_banks.state_id
#
# ordering the data by states to compare statewise data
# SELECT * FROM inventories
# 	JOIN blood_banks
# 	  ON blood_banks.id = inventories.blood_bank_id
# 	JOIN states
# 	  ON states.id = blood_banks.state_id
# ORDER BY states.name
#
# grouping this data by states
# SELECT states.name FROM inventories
# 	JOIN blood_banks
# 	  ON blood_banks.id = inventories.blood_bank_id
# 	JOIN states
# 	  ON states.id = blood_banks.state_id
# GROUP BY states.name
#
# grouping by blood types along with states to combine the data for analysis
# SELECT states.name, inventories.blood_type FROM inventories
# 	JOIN blood_banks
# 	  ON blood_banks.id = inventories.blood_bank_id
# 	JOIN states
# 	  ON states.id = blood_banks.state_id
# GROUP BY states.name, inventories.blood_type
#
# summing the quantity available in the blood banks across every state and blood types available in that respective state
# SELECT states.name, inventories.blood_type, SUM(inventories.quantity_cc) AS Quantity FROM inventories
# 	JOIN blood_banks
# 	  ON blood_banks.id = inventories.blood_bank_id
# 	JOIN states
# 	  ON states.id = blood_banks.state_id
# GROUP BY states.name, inventories.blood_type
#
# ordering the above availed data with every state. this data consists of every blood type available in each state with their quantities
# SELECT states.name, inventories.blood_type, SUM(inventories.quantity_cc) AS Quantity FROM inventories
# 	JOIN blood_banks
# 	  ON blood_banks.id = inventories.blood_bank_id
# 	JOIN states
# 	  ON states.id = blood_banks.state_id
# GROUP BY states.name, inventories.blood_type
# ORDER BY states.name

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
    analysis5_sql = """SELECT states.name, inventories.blood_type, SUM(inventories.quantity_cc) AS Quantity FROM inventories JOIN blood_banks ON blood_banks.id = inventories.blood_bank_id
                       JOIN states ON states.id = blood_banks.state_id GROUP BY states.name, inventories.blood_type ORDER BY states.name"""

    # using the functions from the python libraries, executing the query to extract the data
    cursor.execute(analysis5_sql)
    # storing the data executed above in a temporary list
    results = cursor.fetchall()
    # reading the column names of the database table to keep them as headers while writing data into csv
    column_names = results[0].keys()

    # opening the named csv, "analysis5.csv" and writing the data into the csv with the use of function 'w'
    with open('analysis5.csv', 'w') as csvfile:

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
