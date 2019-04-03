# Querying inventories table to find the inventories of the blood types
# SELECT * FROM inventories
#
# Joining blood banks table to inventories using the foreign key concept
# SELECT * FROM inventories
# 	JOIN blood_banks
# 	  ON blood_banks.id = inventories.blood_bank_id
#
# joining states table for analysis purpose
# SELECT * FROM inventories
# 	JOIN blood_banks
# 	  ON blood_banks.id = inventories.blood_bank_id
# 	JOIN states
# 	  ON states.id = blood_banks.state_id
#
# ordering the data by states
# SELECT * FROM inventories
# 	JOIN blood_banks
# 	  ON blood_banks.id = inventories.blood_bank_id
# 	JOIN states
# 	  ON states.id = blood_banks.state_id
# ORDER BY states.id
#
# grouping the data by states and blood types available in the inventory for analysis
# SELECT states.name, states.life_expectancy, inventories.blood_type FROM inventories
# 	JOIN blood_banks
# 	  ON blood_banks.id = inventories.blood_bank_id
# 	JOIN states
# 	  ON states.id = blood_banks.state_id
# GROUP BY states.id, inventories.blood_type
#
# sub-querying the results to fetch table "a" specific data
# SELECT *
# FROM (SELECT states.name, states.life_expectancy, inventories.blood_type
# 		FROM inventories
# 			JOIN blood_banks
# 			  ON blood_banks.id = inventories.blood_bank_id
# 			JOIN states
# 			  ON states.id = blood_banks.state_id
# GROUP BY states.id, inventories.blood_type) a
#
# ordering the data from table "a" by blood type and life expectancy
# SELECT a.blood_type, a.life_expectancy
# FROM (SELECT states.name, states.life_expectancy, inventories.blood_type
# 		FROM inventories
# 			JOIN blood_banks
# 			  ON blood_banks.id = inventories.blood_bank_id
# 			JOIN states
# 			  ON states.id = blood_banks.state_id
# GROUP BY states.id, inventories.blood_type) a
# ORDER BY a.blood_type, a.life_expectancy DESC
#
# sub-queryin the data set to fetch table "b" specific results
# SELECT *
# FROM (SELECT a.blood_type, a.life_expectancy
# 		FROM (SELECT states.name, states.life_expectancy, inventories.blood_type
# 				FROM inventories
# 					JOIN blood_banks
# 					  ON blood_banks.id = inventories.blood_bank_id
# 					JOIN states
# 					  ON states.id = blood_banks.state_id
# 		GROUP BY states.id, inventories.blood_type) a
# 		ORDER BY a.blood_type, a.life_expectancy DESC) b
#
# ordering table "b" by blood types
# SELECT *
# FROM (SELECT a.blood_type, a.life_expectancy
# 		FROM (SELECT states.name, states.life_expectancy, inventories.blood_type
# 				FROM inventories
# 					JOIN blood_banks
# 					  ON blood_banks.id = inventories.blood_bank_id
# 					JOIN states
# 					  ON states.id = blood_banks.state_id
# 		GROUP BY states.id, inventories.blood_type) a
# 		ORDER BY a.blood_type, a.life_expectancy DESC) b
# ORDER BY b.blood_type
#
# grouping by blood type after ordering the data in table "b"
# SELECT AVG(b.life_expectancy) as average, b.blood_type
# FROM (SELECT a.blood_type, a.life_expectancy
# 		FROM (SELECT states.name, states.life_expectancy, inventories.blood_type
# 				FROM inventories
# 					JOIN blood_banks
# 					  ON blood_banks.id = inventories.blood_bank_id
# 					JOIN states
# 					  ON states.id = blood_banks.state_id
# 		GROUP BY states.id, inventories.blood_type) a
# 		ORDER BY a.blood_type, a.life_expectancy DESC) b
# GROUP BY b.blood_type
#
# ordering the analysis results by average of life expectancy to find the blood type with better life expectancy average
# SELECT AVG(b.life_expectancy) as average, b.blood_type
# FROM (SELECT a.blood_type, a.life_expectancy
# 		FROM (SELECT states.name, states.life_expectancy, inventories.blood_type
# 				FROM inventories
# 					JOIN blood_banks
# 					  ON blood_banks.id = inventories.blood_bank_id
# 					JOIN states
# 					  ON states.id = blood_banks.state_id
# 		GROUP BY states.id, inventories.blood_type) a
# 		ORDER BY a.blood_type, a.life_expectancy DESC) b
# GROUP BY b.blood_type
# ORDER BY average DESC

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
    analysis4_sql = """SELECT AVG(b.life_expectancy) as average, b.blood_type FROM (SELECT a.blood_type, a.life_expectancy FROM
                        (SELECT states.name, states.life_expectancy, inventories.blood_type FROM inventories JOIN blood_banks ON blood_banks.id = inventories.blood_bank_id
                        JOIN states ON states.id = blood_banks.state_id GROUP BY states.id, inventories.blood_type) a
                        ORDER BY a.blood_type, a.life_expectancy DESC) b GROUP BY b.blood_type ORDER BY average DESC"""

    # using the functions from the python libraries, executing the query to extract the data
    cursor.execute(analysis4_sql)
    # storing the data executed above in a temporary list
    results = cursor.fetchall()
    # reading the column names of the database table to keep them as headers while writing data into csv
    column_names = results[0].keys()

    # opening the named csv, "analysis4.csv" and writing the data into the csv with the use of function 'w'
    with open('analysis4.csv', 'w') as csvfile:

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
