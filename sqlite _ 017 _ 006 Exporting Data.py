"""Export SQLite Database to a CSV file using sqlite3 tool
SQLite project provides you with a command-line program called sqlite3 or sqlite3.exe on Windows. By using the sqlite3 tool, you can use the SQL statements and dot-commands to interact with the SQLite database.

To export data from the SQLite database to a CSV file, you use these steps:

Turn on the header of the result set using the .header on command.
Set the output mode to CSV to instruct the sqlite3 tool to issue the result in the CSV mode.
Send the output to a CSV file.
Issue the query to select data from the table to which you want to export.
The following commands select data from the customers table and export it to the data.csv file.

>sqlite3 c:/sqlite/chinook.db
sqlite> .headers on
sqlite> .mode csv
sqlite> .output data.csv
sqlite> SELECT customerid,
   ...>        firstname,
   ...>        lastname,
   ...>        company
   ...>   FROM customers;
sqlite> .quit
If you check the data.csv file, you will see the following output.

SQLite Export CSV example
Besides using the dot-commands, you can use the options of the sqlite3 tool to export data from the SQLite database to a CSV file.

For example, the following command exports the data from the tracks table to a CSV file named tracks.csv.

>sqlite3 -header -csv c:/sqlite/chinook.db "select * from tracks;" > tracks.csv
Code language: SQL (Structured Query Language) (sql)
SQLite Export CSV one-liner option
If you have a file named query.sql that contains the script to query data, you can execute the statements in the file and export data to a CSV file.

>sqlite3 -header -csv c:/sqlite/chinook.db < query.sql > data.csv
Export SQLite database to a CSV file using SQliteStudio
The SQLiteStudio provides the export function that allows you to export data in a table or the result of a query to a CSV file.

The following steps show you how to export data from a table to a CSV file.

First, click the Tools > Export menu item

SQLite Export CSV Step 1
Next, choose the database and table that you want to export data; check the Export table data.

SQLite Export CSV Step 3
Then, choose a single table to export the data.

SQLite Export CSV Step 2
After that, (1) choose the CSV as the export format, (2) specify the CSV file name, (3) check the column names in the first row, (4) choose comma (,) as the column separator, (5) treat the NULL value as empty string, (6) click Finish button to complete exporting.

SQLite Export CSV Step 4
Finally, check the customer.csv file, you will see the following content:

SQLite Export CSV Result Customers Data
In this tutorial, you have learned various ways to export data in the SQLite database to a CSV file.
"""
