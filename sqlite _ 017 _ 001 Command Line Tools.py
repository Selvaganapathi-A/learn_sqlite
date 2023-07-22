"""The SQLite project delivers a simple command-line tool named sqlite3 (or sqlite3.exe on Windows) that allows you to interact with the SQLite databases using SQL statements and commands.

Connect to an SQLite database
To start the sqlite3, you type the sqlite3 as follows:

>sqlite3
SQLite version 3.29.0 2019-07-10 17:32:03
Enter ".help" for usage hints.
Connected to a transient in-memory database.
Use ".open FILENAME" to reopen on a persistent database.
sqlite>
Code language: Shell Session (shell)
By default, an SQLite session uses the in-memory database, therefore, all changes will be gone when the session ends.

To open a database file, you use the .open FILENAME command. The following statement opens the chinook.db database:

sqlite> .open c:\sqlite\db\chinook.db
Code language: Shell Session (shell)
If you want to open a specific database file when you connect to the SQlite database, you use the following command:

>sqlite3 c:\sqlite\db\chinook.db
SQLite version 3.13.0 2016-05-18 10:57:30
Enter ".help" for usage hints.
sqlite>
Code language: Shell Session (shell)
If you start a session with a database name that does not exist, the sqlite3 tool will create the database file.

For example, the following command creates a database named sales in the C:\sqlite\db\ directory:

>sqlite3 c:\sqlite\db\sales.db
SQLite version 3.29.0 2019-07-10 17:32:03
Enter ".help" for usage hints.
sqlite>
Code language: Shell Session (shell)
Show all available commands and their purposes
To show all available commands and their purpose, you use the .help command as follows:

.help
Code language: Shell Session (shell)
Show databases in the current database connection
To show all databases in the current connection, you use the .databases command. The .databases command displays at least one database with the name: main.

For example, the following command shows all the databases of the current connection:

sqlite> .database
seq  name             file
---  ---------------  --------------------------
0    main             c:\sqlite\db\sales.db
sqlite>
Code language: Shell Session (shell)
To add an additional database in the current connection, you use the statement ATTACH DATABASE. The following statement adds the chinook database to the current connection.

sqlite> ATTACH DATABASE "c:\sqlite\db\chinook.db" AS chinook;
Code language: Shell Session (shell)
Now if you run the .database command again, the sqlite3 returns two databases: main and chinook.

sqlite> .databases
seq  name             file
---  ---------------  ---------------------
0    main             c:\sqlite\db\sales.db
2    chinook          c:\sqlite\db\chinook.db
Code language: Shell Session (shell)
Exit sqlite3 tool
To exit the sqlite3 program, you use the .exit command.

sqlite>.exit
Code language: Shell Session (shell)
Show tables in a database
To display all the tables in the current database, you use the .tables command. The following commands open a new database connection to the chinook database and display the tables in the database.

>sqlite3 c:\sqlite\db\chinook.db
SQLite version 3.29.0 2019-07-10 17:32:03
Enter ".help" for usage hints.
sqlite> .tables
albums          employees       invoices        playlists
artists         genres          media_types     tracks
customers       invoice_items   playlist_track
sqlite>
Code language: Shell Session (shell)
If you want to find tables based on a specific pattern, you use the .table pattern command. The sqlite3 uses the LIKE operator for pattern matching.

For example, the following statement returns the table that ends with the string es.

sqlite> .table '%es'
employees    genres       invoices     media_types
sqlite>
Code language: Shell Session (shell)
Show the structure of a table
To display the structure of a table, you use the .schema TABLE command. The TABLE argument could be a pattern. If you omit it, the .schema command will show the structures of all the tables.

The following command shows the structure of the albums table.

sqlite> .schema albums
CREATE TABLE "albums"
(
    [AlbumId] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    [Title] NVARCHAR(160)  NOT NULL,
    [ArtistId] INTEGER  NOT NULL,
    FOREIGN KEY ([ArtistId]) REFERENCES "artists" ([ArtistId])
                ON DELETE NO ACTION ON UPDATE NO ACTION
);
CREATE INDEX [IFK_AlbumArtistId] ON "albums" ([ArtistId]);
sqlite>
Code language: Shell Session (shell)
To show the schema and the content of the sqlite_stat tables, you use the .fullschema command.

sqlite>.fullschema
Code language: CSS (css)
Show indexes
To show all indexes of the current database, you use the .indexes command as follows:

sqlite> .indexes
IFK_AlbumArtistId
IFK_CustomerSupportRepId
IFK_EmployeeReportsTo
IFK_InvoiceCustomerId
IFK_InvoiceLineInvoiceId
IFK_InvoiceLineTrackId
IFK_PlaylistTrackTrackId
IFK_TrackAlbumId
IFK_TrackGenreId
IFK_TrackMediaTypeId
Code language: Shell Session (shell)
To show the indexes of a specific table, you use the .indexes TABLE command. For example, to show indexes of the albums table, you use the following command:

sqlite> .indexes albums
IFK_AlbumArtistId
Code language: CSS (css)
To show indexes of the tables whose names end with es, you use a pattern of the LIKE operator.

sqlite> .indexes %es
IFK_EmployeeReportsTo
IFK_InvoiceCustomerId
Code language: Shell Session (shell)
Save the result of a query into a file
To save the result of a query into a file, you use the .output FILENAME command. Once you issue the .output command, all the results of the subsequent queries will be saved to the file that you specified in the FILENAME argument. If you want to save the result of the next single query only to the file, you issue the .once FILENAME command.

To display the result of the query to the standard output again, you issue the .output command without arguments.

The following commands select the title from the albums table and write the result to the albums.txt file.

sqlite> .output albums.txt
sqlite> SELECT title FROM albums;
Code language: Shell Session (shell)
Execute SQL statements from a file
Suppose we have a file named commands.txt in the c:\sqlite\ folder with the following content:

SELECT albumid, title
FROM albums
ORDER BY title
LIMIT 10;
Code language: Shell Session (shell)
To execute the SQL statements in the commands.txt file, you use the .read FILENAME command as follows:

sqlite> .mode column
sqlite> .header on
sqlite> .read c:/sqlite/commands.txt
AlbumId     Title
----------  ----------------------
156         ...And Justice For All
257         20th Century Masters -
296         A Copland Celebration,
94          A Matter of Life and D
95          A Real Dead One
96          A Real Live One
285         A Soprano Inspired
139         A TempestadeTempestade
203         A-Sides
160         Ace Of Spades
Code language: Shell Session (shell)
In this tutorial, you have learned many useful commands in the sqlite3 tool to perform various tasks that deal with the SQLite database.

#
#
#

Introduction to the SQLite ATTACH DATABASE statement
When you connect to a database, its name is main regardless of the database file name. In addition, you can access the temporary database that holds temporary tables and other database objects via the temp database.

Therefore, every SQLite database connection has the main database and also temp database in case you deal with temporary database objects.

To attach an additional database to the current database connection, you use the ATTACH DATABASE statement as follows:

ATTACH DATABASE file_name AS database_name;
Code language: SQL (Structured Query Language) (sql)
The statement associates the database file file_name with the current database connection under the logical database name database_name.

If the database file file_name does not exist, the statement creates a new database file.

Once the additional database attached, you can refer to all objects in the database under the name database_name. For example, to refer to the people table in the contacts database, you use the contacts.people.

In case you want to create a new memory database and attach it to the current database connection, you use :memory: filename.

You can attach multiple in-memory databases at the same time with a condition that each memory database must be unique.

If you specify an empty file name '', the statement creates a temporary file-backed database.

Note that SQLite automatically deletes all temporary and memory databases when the database connection is closed.

SQLite ATTACH DATABASE example
First, connect to the chinook sample database using sqlite3 command as follows:

>sqlite3 c:\sqlite\db\chinook.db;
Code language: CSS (css)
Next, use the .databases command to list all databases in the current database connection.

sqlite> .databases
Code language: SQL (Structured Query Language) (sql)
SQLite returns the following output.

seq  name             file
---  ---------------  ----------------------------------------------------------
0    main             c:\sqlite\db\chinook.db
Code language: CSS (css)
Then, use the ATTACH DATABASE statement to create a new database named contacts and associates it in the current database connection.

sqlite> attach database 'c:\sqlite\db\contacts.db' as contacts;
Code language: JavaScript (javascript)
Fourth, use the .database command to display all databases in the current database connection.

sqlite> .databases
Code language: SQL (Structured Query Language) (sql)
SQLite returns 2 databases as follows:

seq  name             file
---  ---------------  ----------------------------------------------------------
0    main             c:\sqlite\db\chinook.db
2    contacts         c:\sqlite\db\contacts.db
Code language: SQL (Structured Query Language) (sql)
After that, create a new table named people in the contacts database and populate data from the customers table in the main database.

sqlite> CREATE TABLE contacts.people(first_name text, last_name text);
sqlite> INSERT INTO contacts.people SELECT firstName, lastName FROM customers;
Code language: CSS (css)
Notice that we referred to the people table in the contacts database using the contacts.people naming convention.

Finally, query data from the people table in the contacts database.

SELECT * FROM contacts.people;
Code language: SQL (Structured Query Language) (sql)
For more information on the ATTACH DATABASE statement, check out its documentation.

In this tutorial, you have learned how to use the SQLite ATTACH DATABASE statement to associate additional databases in the current database connection.
"""
