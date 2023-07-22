"""Importing a CSV file into a table using sqlite3 tool
In the first scenario, you want to import data from CSV file into a table that does not exist in the SQLite database.

First, the sqlite3 tool creates the table. The sqlite3 tool uses the first row of the CSV file as the names of the columns of the table.
Second, the sqlite3 tool import data from the second row of the CSV file into the table.
We will import a CSV file named city.csv with two columns: name and population. You can download it here for practicing.

Download the city.csv file

To import the c:\sqlite\city.csv file into the cities table:

First, set the mode to CSV to instruct the command-line shell program to interpret the input file as a CSV file. To do this, you use the .mode command as follows:

sqlite> .mode csv
Second, use the command .import FILE TABLE to import the data from the city.csv file into the cities table.

sqlite>.import c:/sqlite/city.csv cities
To verify the import, you use the command .schema to display the structure of the cities table.

sqlite> .schema cities
CREATE TABLE cities(
  "name" TEXT,
  "population" TEXT
);
Code language: SQL (Structured Query Language) (sql)
To view the data of the cities table, you use the following SELECT statement.

SELECT
   name,
   population
FROM
   cities;
Code language: SQL (Structured Query Language) (sql)
In the second scenario, the table is already available in the database and you just need to import the data.

First, drop the cities table that you have created.

DROP TABLE IF EXISTS cities;
Code language: SQL (Structured Query Language) (sql)
Second, use the following CREATE TABLE statement to create the table cities.

CREATE TABLE cities(
  name TEXT NOT NULL,
  population INTEGER NOT NULL
);
Code language: SQL (Structured Query Language) (sql)
If the table already exists, the sqlite3 tool uses all the rows, including the first row, in the CSV file as the actual data to import. Therefore, you should delete the first row of the CSV file.

The following commands import the city_without_header.csv file into the cities table.

sqlite> .mode csv
sqlite> .import c:/sqlite/city_no_header.csv cities
Code language: SQL (Structured Query Language) (sql)
Import a CSV file into a table using SQLite Studio
Most SQLite GUI tools provide the import function that allows you to import data from a file in CSV format, tab-delimited format, etc., into a table.

We will use the SQLite Studio to show you how to import a CSV file into a table with the assumption that the target table already exists in the database.

First, from the menu choose tool menu item.

SQLite Import csv to table Step 1
Second, choose the database and table that you want to import data then click the Next button.

SQLite Import csv to table Step 2
Third, choose CSV as the data source type, choose the CSV file in the Input file field, and choose the ,(comma) option as the Field separator as shown in the picture below. Then click the Finish button to import the data.

SQLite Import csv to table Step 3
In this tutorial, you have learned how to use the sqlite3 and SQLite Studio to import data from a CSV file into a table in the SQLite database.

"""
