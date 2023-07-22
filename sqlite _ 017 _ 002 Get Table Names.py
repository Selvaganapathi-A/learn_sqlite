"""Showing tables using the sqlite command line shell program
To show tables in a database using the sqlite command-line shell program, you follow these steps:

First, open the database that you want to show the tables:

sqlite3 c:\sqlite\db\chinook.db
Code language: SQL (Structured Query Language) (sql)
The above statement opened the database named  chinook.db that locates in the c:\sqlite\db directory.

Second, type the .tables command:

tables
Code language: SQL (Structured Query Language) (sql)
The .tables command lists all tables in the chinook database

albums          employees       invoices        playlists
artists         genres          media_types     tracks
customers       invoice_items   playlist_track
Code language: SQL (Structured Query Language) (sql)
Note that both .tables, .table have the same effect. In addition, the command .ta should work too.

The .tables command also can be used to show temporary tables. See the following example:

First, create a new temporary table named temp_table1:

CREATE TEMPORARY TABLE temp_table1( name TEXT );
Code language: SQL (Structured Query Language) (sql)
Second, list all tables from the database:

.tables
Code language: SQL (Structured Query Language) (sql)
The following shows the output:

albums            employees         invoices          playlists
artists           genres            media_types       temp.temp_table1
customers         invoice_items     playlist_track    tracks
Code language: SQL (Structured Query Language) (sql)
Because the schema of temporary tables is temp, the command showed the names of schema and table of the temporary table such as temp.temp_table1.

If you want to show tables with the specific name, you can add a matching pattern:

.tables pattern
Code language: SQL (Structured Query Language) (sql)
The command works the same as LIKE operator. The pattern must be surrounded by single quotation marks ( ').

For example, to find tables whose names start with the letter ‘a’, you use the following command:

.table 'a%'
Code language: SQL (Structured Query Language) (sql)
Here is the output:

albums   artists
Code language: plaintext (plaintext)
To shows the tables whose name contains the string ck, you use the %ck% pattern as shown in the following command:

.tables '%ck%'
Code language: SQL (Structured Query Language) (sql)
The output is as follows:

playlist_track  tracks
Code language: SQL (Structured Query Language) (sql)
Showing tables using SQL statement
Another way to list all tables in a database is to query them from the sqlite_schema table.

SELECT
    name
FROM
    sqlite_schema
WHERE
    type ='table' AND
    name NOT LIKE 'sqlite_%';
Code language: SQL (Structured Query Language) (sql)
Here is the output:

SQLite Show Tables Command
In this query, we filtered out all tables whose names start with sqlite_ such as  sqlite_stat1 and sqlite_sequence tables. These tables are the system tables managed internally by SQLite.

Note that SQLite changed the table sqlite_master to sqlite_schema.

In this tutorial, you have learned how to show all tables in a database using the .tables command or by querying data from the sqlite_schema table.

"""
