"""
Introduction to SQLite data types
If you come from other database systems such as MySQL and PostgreSQL, you notice that they use static typing. It means when you declare a column with a specific data type, that column can store only data of the declared data type.

Different from other database systems, SQLite uses dynamic type system. In other words, a value stored in a column determines its data type, not the column’s data type.

In addition, you don’t have to declare a specific data type for a column when you create a table. In case you declare a column with the integer data type, you can store any kind of data types such as text and BLOB, SQLite will not complain about this.

SQLite provides five primitive data types which are referred to as storage classes.

Storage classes describe the formats that SQLite uses to store data on disk. A storage class is more general than a data type e.g., INTEGER storage class includes 6 different types of integers. In most cases, you can use storage classes and data types interchangeably.

The following table illustrates 5 storage classes in SQLite:

Storage Class	Meaning
NULL	NULL values mean missing information or unknown.
INTEGER	Integer values are whole numbers (either positive or negative). An integer can have variable sizes such as 1, 2,3, 4, or 8 bytes.
REAL	Real values are real numbers with decimal values that use 8-byte floats.
TEXT	TEXT is used to store character data. The maximum length of TEXT is unlimited. SQLite supports various character encodings.
BLOB	BLOB stands for a binary large object that can store any kind of data. The maximum size of BLOB is, theoretically, unlimited.
SQLite determines the data type of a value based on its data type according to the following rules:

If a literal has no enclosing quotes and decimal point or exponent, SQLite assigns the INTEGER storage class.
If a literal is enclosed by single or double quotes, SQLite assigns the TEXT storage class.
If a literal does not have quote nor decimal point nor exponent, SQLite assigns REAL storage class.
If a literal is NULL without quotes, it assigned NULL storage class.
If a literal has the X’ABCD’ or x ‘abcd’, SQLite assigned BLOB storage class.
SQLite does not support built-in date and time storage classes. However, you can use the TEXT, INT, or REAL to store date and time values. For the detailed information on how to handle date and time values, check it out the SQLite date and time tutorial.

SQLites provides the typeof() function that allows you to check the storage class of a value based on its format. See the following example:

SELECT
	typeof(100),
	typeof(10.0),
	typeof('100'),
	typeof(x'1000'),
	typeof(NULL);
Code language: SQL (Structured Query Language) (sql)
SQLite Data Types - typeof function
A single column in SQLite can store mixed data types. See the following example.

First, create a new table named test_datatypes for testing.

CREATE TABLE test_datatypes (
	id INTEGER PRIMARY KEY,
	val
);
Code language: SQL (Structured Query Language) (sql)
Second, insert data into the test_datatypes table.

INSERT INTO test_datatypes (val)
VALUES
	(1),
	(2),
	(10.1),
	(20.5),
	('A'),
	('B'),
	(NULL),
	(x'0010'),
	(x'0011');
Code language: SQL (Structured Query Language) (sql)
Third, use the typeof() function to get the data type of each value stored in the val column.

SELECT
	id,
	val,
	typeof(val)
FROM
	test_datatypes;
Code language: SQL (Structured Query Language) (sql)
SQLite Data Types - mixed data types in a column
You may ask how SQLite sorts data in a column with different storage classes like val column above.

To resolve this, SQLite provides the following set of rules when it comes to sorting:

NULL storage class has the lowest value. It is lower than any other values. Between NULL values, there is no order.
The next higher storage classes are INTEGER and REAL. SQLite compares INTEGER and REAL numerically.
The next higher storage class is TEXT. SQLite uses the collation of TEXT values when it compares the TEXT values.
The highest storage class is the BLOB. SQLite uses the C function memcmp() to compare BLOB values.
When you use the ORDER BY clause to sort the data in a column with different storage classes, SQLite performs the following steps:

First, group values based on storage class: NULL, INTEGER, and REAL, TEXT, and BLOB.
Second, sort the values in each group.
The following statement sorts the mixed data in the val column of the test_datatypes table:

SELECT
	id,
	val,
	typeof(val)
FROM
	test_datatypes
ORDER BY val;
Code language: SQL (Structured Query Language) (sql)
SQLite Data Types and ORDER BY clause
SQLite manifest typing & type affinity
Other important concepts related to SQLite data types are manifest typing and type affinity:

Manifest typing means that a data type is a property of a value stored in a column, not the property of the column in which the value is stored. SQLite uses manifest typing to store values of any type in a column.
Type affinity of a column is the recommended type for data stored in that column. Note that the data type is recommended, not required, therefore, a column can store any type of data.
In this tutorial, you have learned about SQLite data types and some important concepts including storage classes, manifest typing, and type affinity.
"""

"""
SQLite does not support built-in date and/or time storage class. Instead, it leverages some built-in date and time functions to use other storage classes such as TEXT, REAL, or INTEGER for storing the date and time values.

Using the TEXT storage class for storing SQLite date and time
If you use the TEXT storage class to store date and time value, you need to use the ISO8601 string format as follows:

YYYY-MM-DD HH:MM:SS.SSS
Code language: SQL (Structured Query Language) (sql)
For example, 2016-01-01 10:20:05.123

First, create a new table named datetime_text for demonstration.

CREATE TABLE datetime_text(
   d1 text,
   d2 text
);
Code language: SQL (Structured Query Language) (sql)
Try It

The table contains two column d1 and d2 with TEXT datatype.

To insert date and time values into the datetime_text table, you use the DATETIME function.

For example, to get the current UTC date and time value, you pass the now literal string to the function as follows:

SELECT datetime('now');
Code language: SQL (Structured Query Language) (sql)
Try It

To get the local time, you pass an additional argument  localtime.

SELECT datetime('now','localtime');
Code language: SQL (Structured Query Language) (sql)
Try It

Second, insert the date and time values into the datetime_text table as follows:

INSERT INTO datetime_text (d1, d2)
VALUES(datetime('now'),datetime('now', 'localtime'));
Code language: SQL (Structured Query Language) (sql)
Try It

Third, query the data from the datetime_text table.

SELECT
	d1,
	typeof(d1),
	d2,
	typeof(d2)
FROM
	datetime_text;
Code language: SQL (Structured Query Language) (sql)
Try It

SQLite Date Using TEXT data type
Using REAL storage class to store SQLite date and time values
You can use the REAL storage class to store the date and/ or time values as Julian day numbers, which is the number of days since noon in Greenwich on November 24, 4714 B.C. based on the proleptic Gregorian calendar.

Let’s take a look at an example of using the REAL storage class to store date and time values.

First, create a new table named datetime_real.

CREATE TABLE datetime_real(
   d1 real
);
Code language: SQL (Structured Query Language) (sql)
Try It

Second, insert the “current” date and time value into the datetime_real table.

INSERT INTO datetime_real (d1)
VALUES(julianday('now'));
Code language: SQL (Structured Query Language) (sql)
Try It

We used the  julianday() function to convert the current date and time to the Julian Day.

Third, query data from the datetime_real table.

SELECT d1 FROM datetime_real;
Code language: SQL (Structured Query Language) (sql)
Try It

SQLite Date Using REAL data type
The output is not human readable.

Fortunately, you can use the built-in date() and time() functions to format a date and time value as follows:

SELECT
	date(d1),
	time(d1)
FROM
	datetime_real;
Code language: SQL (Structured Query Language) (sql)
Try It

SQLite Date and Time functions
Using INTEGER to store SQLite date and time values
Besides  TEXT and REAL storage classes, you can use the INTEGER storage class to store date and time values.

We typically use the INTEGER to store UNIX time which is the number of seconds since 1970-01-01 00:00:00 UTC. See the following example:

First, create a table that has one column whose data type is INTEGER to store the date and time values.

CREATE TABLE datetime_int (d1 int);
Code language: SQL (Structured Query Language) (sql)
Try It

Second, insert the current date and time value into the datetime_int table.

INSERT INTO datetime_int (d1)
VALUES(strftime('%s','now'));
Code language: SQL (Structured Query Language) (sql)
Try It

Third, query data from the datetime_int table.

SELECT d1 FROM datetime_int;
Code language: SQL (Structured Query Language) (sql)
Try It

It’s an integer.

To format the result, you can use the built-in datetime() function as follows:

SELECT datetime(d1,'unixepoch')
FROM datetime_int;
Code language: SQL (Structured Query Language) (sql)
Try It

SQlite DATETIME function
Using SQLite, you can freely choose any data types to store date and time values and use the built-in dates and times function to convert between formats.

For the detailed information on SQLite dates and times functions, check it out the built-in dates and times functions.

In this tutorial, you have learned how to use the TEXT, REAL, and INTEGER storage classes to store date and time values. In addition, you learned how to use the built-in dates and times functions to convert the stored date and times values into readable formats.
"""

"""Introduction to SQLite CREATE TABLE statement
To create a new table in SQLite, you use CREATE TABLE statement using the following syntax:

CREATE TABLE [IF NOT EXISTS] [schema_name].table_name (
	column_1 data_type PRIMARY KEY,
   	column_2 data_type NOT NULL,
	column_3 data_type DEFAULT 0,
	table_constraints
) [WITHOUT ROWID];
Code language: SQL (Structured Query Language) (sql)
In this syntax:

First, specify the name of the table that you want to create after the CREATE TABLE keywords. The name of the table cannot start with sqlite_ because it is reserved for the internal use of SQLite.
Second, use IF NOT EXISTS option to create a new table if it does not exist. Attempting to create a table that already exists without using the IF NOT EXISTS option will result in an error.
Third, optionally specify the schema_name to which the new table belongs. The schema can be the main database, temp database or any attached database.
Fourth, specify the column list of the table. Each column has a name, data type, and the column constraint. SQLite supports PRIMARY KEY, UNIQUE, NOT NULL, and CHECK column constraints.
Fifth, specify the table constraints such as PRIMARY KEY, FOREIGN KEY, UNIQUE, and CHECK constraints.
Finally, optionally use the WITHOUT ROWID option. By default, a row in a table has an implicit column, which is referred to as the rowid, oid or _rowid_ column. The rowid column stores a 64-bit signed integer key that uniquely identifies the row inside the table. If you don’t want SQLite creates the rowid column, you specify the WITHOUT ROWID option. A table that contains the rowid column is known as a rowid table. Note that the WITHOUT ROWID option is only available in SQLite 3.8.2 or later.
Note that the primary key of a table is a column or a group of columns that uniquely identify each row in the table.

SQLite CREATE TABLE examples
Suppose you have to manage contacts using SQLite.

Each contact has the following information:

First name
Last name
Email
Phone
The requirement is that the email and phone must be unique. In addition, each contact belongs to one or many groups, and each group can have zero or many contacts.

Based on these requirements, we came up with three tables:

The contacts table that stores contact information.
The groups table that stores group information.
The contact_groups table that stores the relationship between contacts and groups.
The following database diagram illustrates tables:contacts groups, and contact_groups.

SQLite Create Table
The following statement creates the contacts table.

CREATE TABLE contacts (
	contact_id INTEGER PRIMARY KEY,
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	email TEXT NOT NULL UNIQUE,
	phone TEXT NOT NULL UNIQUE
);
Code language: SQL (Structured Query Language) (sql)
Try It

The contact_id is the primary key of the contacts table.

Because the primary key consists of one column, you can use the column constraint.

The first_name and last_name columns have TEXT storage class and these columns are NOT NULL. It means that you must provide values when you insert or update rows in the contacts table.

The email and phone are unique therefore we use the UNIQUE constraint for each column.

The following statement creates the groups table:

CREATE TABLE groups (
   group_id INTEGER PRIMARY KEY,
   name TEXT NOT NULL
);
Code language: SQL (Structured Query Language) (sql)
Try It

The groups table is quite simple with two columns: group_id and name. The group_id column is the primary key column.

The following statement creates contact_groups table:

CREATE TABLE contact_groups(
   contact_id INTEGER,
   group_id INTEGER,
   PRIMARY KEY (contact_id, group_id),
   FOREIGN KEY (contact_id)
      REFERENCES contacts (contact_id)
         ON DELETE CASCADE
         ON UPDATE NO ACTION,
   FOREIGN KEY (group_id)
      REFERENCES groups (group_id)
         ON DELETE CASCADE
         ON UPDATE NO ACTION
);
Code language: SQL (Structured Query Language) (sql)
Try It

The contact_groups table has a primary key that consists of two columns: contact_id and group_id.

To add the table primary key constraint, you use this syntax:

PRIMARY KEY (contact_id, group_id)
Code language: SQL (Structured Query Language) (sql)
In addition, the contact_id and group_id are the foreign keys. Therefore, you use FOREIGN KEY constraint to define a foreign key for each column.

FOREIGN KEY (contact_id)
   REFERENCES contacts (contact_id)
      ON DELETE CASCADE
      ON UPDATE NO ACTION
Code language: SQL (Structured Query Language) (sql)
FOREIGN KEY (group_id)
    REFERENCES groups (group_id)
      ON DELETE CASCADE
      ON UPDATE NO ACTION
Code language: SQL (Structured Query Language) (sql)
Note that we will discuss in the FOREIGN KEY constraint in detail in the subsequent tutorial.

In this tutorial, you have learned how to create a new table with various options using SQLite CREATE TABLE statement.
"""
"""
Summary: in this tutorial, you will learn how to use SQLite ALTER TABLE statement to change the structure of an existing table.

Unlike SQL-standard and other database systems, SQLite supports a very limited functionality of the ALTER TABLE statement.

By using an SQLite ALTER TABLE statement, you can perform two actions:

Rename a table.
Add a new column to a table.
Rename a column (added supported in version 3.20.0)
Using SQLite ALTER TABLE to rename a table
To rename a table, you use the following ALTER TABLE RENAME TO statement:

ALTER TABLE existing_table
RENAME TO new_table;
Code language: SQL (Structured Query Language) (sql)
These are important points you should know before you rename a table:

The ALTER TABLE only renames a table within a database. You cannot use it to move the table between the attached databases.
The database objects such as indexes and triggers associated with the table will be associated with the new table.
If a table is referenced by views or statements in triggers, you must manually change the definition of views and triggers.
Let’s take an example of renaming a table.

First, create a table named devices that has three columns: name, model, serial; and insert a new row into the devices table.

CREATE TABLE devices (
   name TEXT NOT NULL,
   model TEXT NOT NULL,
   Serial INTEGER NOT NULL UNIQUE
);

INSERT INTO devices (name, model, serial)
VALUES('HP ZBook 17 G3 Mobile Workstation','ZBook','SN-2015');
Code language: SQL (Structured Query Language) (sql)
Try It

Second, use the ALTER TABLE RENAME TO statement to change the devices table to equipment table as follows:

ALTER TABLE devices
RENAME TO equipment;
Code language: SQL (Structured Query Language) (sql)
Try It

Third, query data from the equipment table to verify the RENAME operation.

SELECT
	name,
	model,
	serial
FROM
	equipment;
Code language: SQL (Structured Query Language) (sql)
Try It

Using SQLite ALTER TABLE to add a new column to a table
You can use the SQLite ALTER TABLE statement to add a new column to an existing table. In this scenario, SQLite appends the new column at the end of the existing column list.

The following illustrates the syntax of ALTER TABLE ADD COLUMN statement:

ALTER TABLE table_name
ADD COLUMN column_definition;
Code language: SQL (Structured Query Language) (sql)
There are some restrictions on the new column:

The new column cannot have a UNIQUE or PRIMARY KEY constraint.
If the new column has a NOT NULL constraint, you must specify a default value for the column other than a NULL value.
The new column cannot have a default of CURRENT_TIMESTAMP, CURRENT_DATE, and CURRENT_TIME, or an expression.
If the new column is a foreign key and the foreign key constraint check is enabled, the new column must accept a default value NULL.
For example, you can add a new column named location to the equipment table:

ALTER TABLE equipment
ADD COLUMN location text;
Code language: SQL (Structured Query Language) (sql)
Try It

Using SQLite ALTER TABLE to rename a column
SQLite added the support for renaming a column using ALTER TABLE RENAME COLUMN statement in version 3.20.0

The following shows the syntax of the ALTER TABLE RENAME COLUMN statement:

ALTER TABLE table_name
RENAME COLUMN current_name TO new_name;
For more information on how to rename a column, check it out the renaming column tutorial.

Using SQLite ALTER TABLE for other actions
If you want to perform other actions e.g., drop a column, you use the following steps:

SQLite-ALTER-TABLE-Steps
The following script illustrates the steps above:

-- disable foreign key constraint check
PRAGMA foreign_keys=off;

-- start a transaction
BEGIN TRANSACTION;

-- Here you can drop column
CREATE TABLE IF NOT EXISTS new_table(
   column_definition,
   ...
);
-- copy data from the table to the new_table
INSERT INTO new_table(column_list)
SELECT column_list
FROM table;

-- drop the table
DROP TABLE table;

-- rename the new_table to the table
ALTER TABLE new_table RENAME TO table;

-- commit the transaction
COMMIT;

-- enable foreign key constraint check
PRAGMA foreign_keys=on;
Code language: SQL (Structured Query Language) (sql)
SQLite ALTER TABLE DROP COLUMN example
SQLite does not support ALTER TABLE DROP COLUMN statement. To drop a column, you need to use the steps above.

The following script creates two tables users and favorites, and insert data into these tables:

CREATE TABLE users(
	UserId INTEGER PRIMARY KEY,
	FirstName TEXT NOT NULL,
	LastName TEXT NOT NULL,
	Email TEXT NOT NULL,
	Phone TEXT NOT NULL
);

CREATE TABLE favorites(
	UserId INTEGER,
	PlaylistId INTEGER,
	FOREIGN KEY(UserId) REFERENCES users(UserId),
	FOREIGN KEY(PlaylistId) REFERENCES playlists(PlaylistId)
);

INSERT INTO users(FirstName, LastName, Email, Phone)
VALUES('John','Doe','john.doe@example.com','408-234-3456');

INSERT INTO favorites(UserId, PlaylistId)
VALUES(1,1);
Code language: SQL (Structured Query Language) (sql)
The following statement returns data from the users table:

SELECT * FROM users;
Code language: SQL (Structured Query Language) (sql)

And the following statement returns the data from the favorites table:

SELECT * FROM favorites;
Code language: SQL (Structured Query Language) (sql)

Suppose, you want to drop the column phone of the users table.

First, disable the foreign key constraint check:

PRAGMA foreign_keys=off;
Second, start a new transaction:

BEGIN TRANSACTION;
Code language: SQL (Structured Query Language) (sql)
Third, create a new table to hold data of the users table except for the phone column:

CREATE TABLE IF NOT EXISTS persons (
	UserId INTEGER PRIMARY KEY,
	FirstName TEXT NOT NULL,
	LastName TEXT NOT NULL,
	Email TEXT NOT NULL
);
Code language: SQL (Structured Query Language) (sql)
Fourth, copy data from the users to persons table:

INSERT INTO persons(UserId, FirstName, LastName, Email)
SELECT UserId, FirstName, LastName, Email
FROM users;
Code language: SQL (Structured Query Language) (sql)
Fifth, drop the users table:

DROP TABLE users;
Code language: SQL (Structured Query Language) (sql)
Sixth, rename the persons table to users table:

ALTER TABLE persons RENAME TO users;
Code language: SQL (Structured Query Language) (sql)
Seventh, commit the transaction:

COMMIT;
Code language: SQL (Structured Query Language) (sql)
Eighth, enable the foreign key constraint check:

PRAGMA foreign_keys=on;
Code language: SQL (Structured Query Language) (sql)
Here is the users table after dropping the phone column:

SELECT * FROM users;
Code language: SQL (Structured Query Language) (sql)

Summary
Use the ALTER TABLE statement to modify the structure of an existing table.
Use ALTER TABLE table_name RENAME TO new_name statement to rename a table.
Use ALTER TABLE table_name ADD COLUMN column_definition statement to add a column to a table.
Use ALTER TABLE table_name RENAME COLUMN current_name TO new_name to rename a column.
"""

"""
Introduction to SQLite ALTER TABLE RENAME COLUMN statement
SQLite added support for renaming column since version 3.25.0 using the ALTER TABLE statement with the following syntax:

ALTER TABLE table_name
RENAME COLUMN current_name TO new_name;
Code language: SQL (Structured Query Language) (sql)
In this syntax:

First, specify the name of the table after the ALTER TABLE keywords.
Second, specify the name of the column that you want to rename after the RENAME COLUMN keywords and the new name after the TO keyword.
SQLite ALTER TABLE RENAME COLUMN example
Let’s take an example of using the ALTER TABLE RENAME COLUMN statement.

First, create a new table called Locations:

CREATE TABLE Locations(
	LocationId INTEGER PRIMARY KEY,
	Address TEXT NOT NULL,
	City TEXT NOT NULL,
	State TEXT NOT NULL,
	Country TEXT NOT NULL
);
Code language: SQL (Structured Query Language) (sql)
Second, insert a new row into the Locations table by using the INSERT statement:

INSERT INTO Locations(Address,City,State,Country)
VALUES('3960 North 1st Street','San Jose','CA','USA');
Code language: SQL (Structured Query Language) (sql)
Third, rename the column Address to Street by using the ALTER TABLE RENAME COLUMN statement:

ALTER TABLE Locations
RENAME COLUMN Address TO Street;
Code language: SQL (Structured Query Language) (sql)
Fourth, query data from the Locations table:

SELECT * FROM Locations;
Code language: SQL (Structured Query Language) (sql)
Output:

LocationId  Street                 City        State       Country
----------  ---------------------  ----------  ----------  ----------
1           3960 North 1st Street  San Jose    CA          USA
Code language: Shell Session (shell)
Finally, show the schema of the Locations table:

.schema Locations
Code language: Shell Session (shell)
Output:

CREATE TABLE Locations(
        LocationId INTEGER PRIMARY KEY,
        Street TEXT NOT NULL,
        City TEXT NOT NULL,
        State TEXT NOT NULL,
        Country TEXT NOT NULL
);
Code language: SQL (Structured Query Language) (sql)
The old way to rename column
SQLite did not support the ALTER TABLE RENAME COLUMN syntax before version 3.25.0.

If you’re using the SQLite with the version lower than 3.25.0 and could not upgrade, then you should follow these steps to rename a column:

First, start a transaction.
Second, create a new table whose structure is the same as the original one except for the column that you want to rename.
Third, copy data from the original table to the new table.
Fourth, drop the original table.
Fifth, rename the new table to the original table.
Finally, commit the transaction.
Renaming column example
The following statement recreates the Locations table:

DROP TABLE IF EXISTS Locations;
CREATE TABLE Locations(
	LocationId INTEGER PRIMARY KEY,
	Address TEXT NOT NULL,
	State TEXT NOT NULL,
	City TEXT NOT NULL,
	Country TEXT NOT NULL
);
Code language: SQL (Structured Query Language) (sql)
And this INSERT statement inserts a new row into the Locations table:

INSERT INTO Locations(Address,City,State,Country)
VALUES('3960 North 1st Street','San Jose','CA','USA');
Code language: SQL (Structured Query Language) (sql)
Suppose that you want to the change the column Address to Street.

First, start a new transaction:

BEGIN TRANSACTION;
Code language: SQL (Structured Query Language) (sql)
Second, create a new table called LocationsTemp with the same structure as the Locations table except for the Address column:

CREATE TABLE LocationsTemp(
	LocationId INTEGER PRIMARY KEY,
	Street TEXT NOT NULL,
	City TEXT NOT NULL,
	State TEXT NOT NULL,
	Country TEXT NOT NULL
);
Code language: SQL (Structured Query Language) (sql)
Third, copy data from the table Locations to LocationsTemp:

INSERT INTO LocationsTemp(Street,City,State,Country)
SELECT Address,City,State,Country
FROM Locations;
Code language: SQL (Structured Query Language) (sql)
Fourth, drop the Locations table:

DROP TABLE Locations;
Code language: SQL (Structured Query Language) (sql)
Fifth, rename the table LocationsTemp to Locations:

ALTER TABLE LocationsTemp
RENAME TO Locations;
Code language: SQL (Structured Query Language) (sql)
Finally, commit the transaction:

COMMIT;
Code language: SQL (Structured Query Language) (sql)
If you query the Locations table, you will see that the column Address has been renamed to Street:

SELECT * FROM Locations;
Code language: SQL (Structured Query Language) (sql)
Here is the output:

sqlite rename column example
Summary
Use the ALTER TABLE RENAME COLUMN to rename a column in a table.
If you are using SQLite 3.25.0, you should upgrade it and use the new syntax. Otherwise, you need to follow the steps described above to rename a column.

"""

"""
Introduction to SQLite DROP TABLE statement
To remove a table in a database, you use SQLite DROP TABLE statement. The statement is simple as follows:

DROP TABLE [IF EXISTS] [schema_name.]table_name;
Code language: SQL (Structured Query Language) (sql)
In this syntax, you specify the name of the table which you want to remove after the DROP TABLE keywords.

SQLite allows you to drop only one table at a time. To remove multiple tables, you need to issue multiple DROP TABLE statements.

If you remove a non-existing table, SQLite issues an error. If you use IF EXISTS option, then SQLite removes the table only if the table exists, otherwise, it just ignores the statement and does nothing.

If you want to remove a table in a specific database, you use the [schema_name.] explicitly.

In case the table has dependent objects such as triggers and indexes, the DROP TABLE statement also removes all the dependent objects.

The DROP TABLE statement performs an implicit  DELETE statement before dropping the table. However, the DROP TABLE statement removes the triggers associated with the table before performing the implicit DELETE statement, therefore, the delete triggers will not fire.

If the foreign key constraints enabled and you perform the DROP TABLE statement, before SQLite performs the implicit DELETE statement, it carries the foreign key constraints check. If a foreign key constraint violation occurs, SQLite issues an error message and will not drop the table.

Notice that the DROP TABLE statement deletes the table from the database and the file on disk completely. You will not be able to undo or recover from this action. Therefore, you should perform the DROP TABLE statement with extra caution.

SQLite DROP TABLE statement examples
For the demonstration purpose, we will create two tables: people and addresses. Each person has one address. And one address can be shared by multiple people.

First, create the tables:

CREATE TABLE IF NOT EXISTS people (
   person_id INTEGER PRIMARY KEY,
   first_name TEXT,
   last_name TEXT,
   address_id INTEGER,
   FOREIGN KEY (address_id)
      REFERENCES addresses (address_id)
);

CREATE TABLE IF NOT EXISTS addresses (
   address_id INTEGER PRIMARY KEY,
   house_no TEXT,
   street TEXT,
   city TEXT,
   postal_code TEXT,
   country TEXT
);
Code language: SQL (Structured Query Language) (sql)
Try It

SQLite DROP TABLE example

Second, insert an address and a person into the addresses and people tables.

INSERT INTO addresses ( house_no, street, city, postal_code, country )
VALUES ( '3960', 'North 1st Street', 'San Jose ', '95134', 'USA ' );
INSERT INTO people ( first_name, last_name, address_id )
VALUES ('John', 'Doe', 1);
Code language: SQL (Structured Query Language) (sql)
Try It

Third, use the DROP TABLE statement to remove the addresses table.

DROP TABLE addresses;
Code language: SQL (Structured Query Language) (sql)
Try It

SQLite issued an error message:

constraint failed
Code language: SQL (Structured Query Language) (sql)
Try It

Because this action violates the foreign key constraint.

To remove the addresses table, you have to:

Disable foreign key constraints.
Drop the addresses table.
Update the address_id in the people table to NULL values.
Enable the foreign key constraints.
See the following statements:

PRAGMA foreign_keys = OFF;

DROP TABLE addresses;

UPDATE people
SET address_id = NULL;

PRAGMA foreign_keys = ON;
Code language: SQL (Structured Query Language) (sql)
Try It

The addresses table is removed and values of the address_id column are updated to NULL values.

In this tutorial, you have learned how to use SQLite DROP TABLE statement to remove the table completely from a database.
"""

"""
Why do you need SQLite VACUUM command
First, when you drop database objects such as tables, views, indexes, and triggers or delete data from tables, the database file size remains unchanged. Because SQLite just marks the deleted objects as free and reserves it for the future uses. As a result, the size of the database file always grows in size.

Second, when you insert or delete data from the tables, the indexes and tables become fragmented, especially for the database that has a high number of inserts, updates, and deletes.

Third, the insert, update and delete operations create unused data block within individual database pages. It decreases the number of rows that can be stored in a single page. Therefore, it increases the number of pages to hold a table. Because of this, it increases storage overhead for the table, takes more time to read/write, and decreases the cache performance.

SQLite VACUUM
SQLite provides the VACUUM command to address all three issues above.

SQLite first copies data within a database file to a temporary database. This operation defragments the database objects, ignores the free spaces, and repacks individual pages. Then, SQLite copies the content of the temporary database file back to the original database file. The original database file is overwritten.

Because the VACUUM command rebuilds the database, you can use it to change some database-specific configuration parameters such as page size, page format, and default encoding. To do this, you set new values using pragma and then vacuum the database.

The SQLite VACUUM command
The VACUUM command does not change the content of the database except the rowid values. If you use INTEGER PRIMARY KEY column, the VACUUM does not change the values of that column. However, if you use unaliased rowid, the VACUUM command will reset the rowid values. Besides changing the rowid values, the VACUUM command also builds the index from scratch.

It is a good practice to perform the VACUUM command periodically, especially when you delete large tables or indexes from a database.

It is important to note that the VACCUM command requires storage to hold the original file and also the copy. Also, the VACUUM command requires exclusive access to the database file. In other words, the VACUUM command will not run successfully if the database has a pending SQL statement or an open transaction.

Currently, as of version 3.9.2, you can run the VACUUM command on the main database, not the attached database file.

Even though SQLite enables the auto-vacuum mode that triggers the vacuum process automatically with some limitations. It is a good practice to run the VACUUM command manually.

How to run the SQLite VACUUM command
The following shows how to run the VACUUM command:

VACUUM;
Code language: SQL (Structured Query Language) (sql)
Make sure that there is no open transaction while you’re running the command.

The following statement enables full auto-vacuum mode:

PRAGMA auto_vacuum = FULL;
Code language: SQL (Structured Query Language) (sql)
To enable incremental vacuum, you use the following statement:

PRAGMA auto_vacuum = INCREMENTAL;
Code language: SQL (Structured Query Language) (sql)
The following statement disables auto-vacuum mode:

PRAGMA auto_vacuum = NONE;
Code language: SQL (Structured Query Language) (sql)
VACUUM with an INTO clause
Here is syntax of the VACUUM with INTO clause:

VACUUM schema-name INTO filename;
Code language: SQL (Structured Query Language) (sql)
The VACUUM statement with an INTO clause keeps the original database file unchanged and creates a new database with the file name specified. The new database will contain the same logical content as the original database, but fully vacuumed.

The filename in the INTO clause can be any SQL expression that evaluates to a string. It must be a path to a file that does not exist or to an empty file, or the VACUUM INTO command will result in an error.

The VACUUM command is very useful for generating backup copies of a live database. It is transactional safe, which the generated database is a consistent snapshot of the original database. However, if a unplanned shutdown or power lose interupts the command, the generated database might be corrupted.

The following statement uses the VACUUM INTO command to generate a new database with the file name chinook_backup.db whose data is copied from of the main schema of the chinook database:

VACUUM main INTO 'c:\sqlite\db\chinook_backup.db';
Code language: JavaScript (javascript)
In this tutorial, you have learned why you need to use the SQLite VACUUM command and how to run it to optimize the database.
"""
