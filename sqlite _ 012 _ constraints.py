"""Introduction to SQLite primary key
A primary key is a column or group of columns used to identify the uniqueness of rows in a table. Each table has one and only one primary key.

SQLite allows you to define primary key in two ways:

First, if the primary key has only one column, you use the PRIMARY KEY column constraint to define the primary key as follows:

CREATE TABLE table_name(
   column_1 INTEGER NOT NULL PRIMARY KEY,
   ...
);
Code language: PHP (php)
Second, in case primary key consists of two or more columns, you use the PRIMARY KEY table constraint to define the primary as shown in the following statement.

CREATE TABLE table_name(
   column_1 INTEGER NOT NULL,
   column_2 INTEGER NOT NULL,
   ...
   PRIMARY KEY(column_1,column_2,...)
);
Code language: SQL (Structured Query Language) (sql)
In SQL standard, the primary key column must not contain NULL values. It means that the primary key column has an implicit NOT NULL constraint.

However, to make the current version of SQLite compatible with the earlier version, SQLite allows the primary key column to contain NULL values.

SQLite primary key and rowid table
When you create a table without specifying the WITHOUT ROWID option, SQLite adds an implicit column called rowid that stores 64-bit signed integer. The rowid column is a key that uniquely identifies the rows in the table. Tables that have rowid columns are called rowid tables.

If a table has the primary key that consists of one column, and that column is defined as INTEGER then this primary key column becomes an alias for the rowid column.

Notice that if you assign another integer type such as BIGINT and UNSIGNED INT to the primary key column, this column will not be an alias for the rowid column.

Because the rowid table organizes its data as a B-tree, querying and sorting data of a rowid table are very fast. It is faster than using a primary key which is not an alias of the rowid.

Another important note is that if you declare a column with the INTEGER type and PRIMARY KEY DESC clause, this column will not become an alias for the rowid column:

CREATE TABLE table(
   pk INTEGER PRIMARY KEY DESC,
   ...
);
Code language: SQL (Structured Query Language) (sql)
Creating SQLite primary key examples
The following statement creates a table named countries which has country_id column as the primary key.

CREATE TABLE countries (
   country_id INTEGER PRIMARY KEY,
   name TEXT NOT NULL
);
Code language: SQL (Structured Query Language) (sql)
Try It

Because the primary key of the countries table has only one column, we defined the primary key using PRIMARY KEY column constraint.

It is possible to use the PRIMARY KEY table constraint to define the primary key that consists of one column as shown in the following statement:

CREATE TABLE languages (
   language_id INTEGER,
   name TEXT NOT NULL,
   PRIMARY KEY (language_id)
);
Code language: SQL (Structured Query Language) (sql)
Try It

However, for tables that the primary keys consist of more than one column, you must use PRIMARY KEY table constraint to define primary keys.

The following statement creates the country_languages table whose primary key consists of two columns.

CREATE TABLE country_languages (
	country_id INTEGER NOT NULL,
	language_id INTEGER NOT NULL,
	PRIMARY KEY (country_id, language_id),
	FOREIGN KEY (country_id) REFERENCES countries (country_id)
            ON DELETE CASCADE ON UPDATE NO ACTION,
	FOREIGN KEY (language_id) REFERENCES languages (language_id)
            ON DELETE CASCADE ON UPDATE NO ACTION
);
Code language: PHP (php)
Try It

Adding SQLite primary key example
Unlike other database systems e.g., MySQL and PostgreSQL, you cannot use the ALTER TABLE statement to add a primary key to an existing table.

You need to follow these steps to work around the limitation:

First, set the foreign key constarint check off.
Next, rename the table to another table name (old_table)
Then, create a new table (table) with exact structure of the table that you have been renamed.
After that, copy data from the old_table to the table.
Finally, turn on the foreign key constraint check on
See the following statements:

PRAGMA foreign_keys=off;

BEGIN TRANSACTION;

ALTER TABLE table RENAME TO old_table;

-- define the primary key constraint here
CREATE TABLE table ( ... );

INSERT INTO table SELECT * FROM old_table;

COMMIT;

PRAGMA foreign_keys=on;
Code language: SQL (Structured Query Language) (sql)
Try It

The BEGIN TRANSACTION starts a new transaction. It ensures that all subsequent statements execute successfully or nothing executes at all.

The COMMIT statement commits all the statements.

Let’s create a table name cities without a primary key.

CREATE TABLE cities (
   id INTEGER NOT NULL,
   name text NOT NULL
);

INSERT INTO cities (id, name)
VALUES(1, 'San Jose');
Code language: SQL (Structured Query Language) (sql)
Try It

In order to add the primary key to the cities table, you perform the following steps:

PRAGMA foreign_keys=off;

BEGIN TRANSACTION;

ALTER TABLE cities RENAME TO old_cities;

CREATE TABLE cities (
   id INTEGER NOT NULL PRIMARY KEY,
   name TEXT NOT NULL
);

INSERT INTO cities
SELECT * FROM old_cities;

DROP TABLE old_cities;

COMMIT;

PRAGMA foreign_keys=on;
Code language: SQL (Structured Query Language) (sql)
Try It

If you use SQLite GUI tool, you can use the following statement to show the table’s information.

PRAGMA table_info([cities]);
Code language: SQL (Structured Query Language) (sql)
Try It

SQLite Primary Key Example
In this tutorial, you have learned use the SQLite PRIMARY KEY constraint to define the primary key for a table.
"""

"""Introduction to SQLite NOT NULL constraint
When you create a table, you can specify whether a column acceptsNULL values or not. By default, all columns in a table accept NULL values except you explicitly use NOT NULL constraints.

To define a NOT NULL constraint for a column, you use the following syntax:

CREATE TABLE table_name (
    ...,
    column_name type_name NOT NULL,
    ...
);
Code language: SQL (Structured Query Language) (sql)
Unlike other constraints such as PRIMARY KEY and CHECK, you can only define NOT NULL constraints at the column level, not the table level.

Based on the SQL standard, PRIMARY KEY should always imply NOT NULL. However, SQLite allows NULL values in the PRIMARY KEY column except that a column is INTEGER PRIMARY KEY column or the table is a WITHOUT ROWID table or the column is defined as a NOT NULL column.

This is due to a bug in some early versions. If this bug is fixed to conform with the SQL standard, then it might break the legacy systems. Therefore, it has been decided to allow NULL values in the  PRIMARY KEY column.

Once a NOT NULL constraint is attached to a column, any attempt to set the column value to NULL such as inserting or updating will cause a constraint violation.

SQLite NOT NULL constraint example
The following example creates a new table named suppliers:

CREATE TABLE suppliers(
    supplier_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);
Code language: SQL (Structured Query Language) (sql)
In this example, the supplier_id is the PRIMARY KEY column of the suppliers table. Because this column is declared as INTEGER PRIMARY KEY, it will not accept NULL values.

The name column is also declared with a NOT NULL constraint, so it will accept only non-NULL values.

The following statement attempt to insert a NULL into the name column of the suppliers table:

INSERT INTO suppliers(name)
VALUES(NULL);
Code language: SQL (Structured Query Language) (sql)
The statement fails due to the NOT NULL constraint violation. Here is the error message:

SQL Error [19]: [SQLITE_CONSTRAINT]  Abort due to constraint violation (NOT NULL constraint failed: suppliers.name)
Code language: CSS (css)
In this tutorial, you have learned how to use SQLite NOT NULL constraint to ensure values in a column are not NULL.
"""

"""Introduction to SQLite UNIQUE constraint
A UNIQUE constraint ensures all values in a column or a group of columns are distinct from one another or unique.

To define a UNIQUE constraint, you use the UNIQUE keyword followed by one or more columns.

You can define a UNIQUE constraint at the column or the table level. Only at the table level, you can define a UNIQUE constraint across multiple columns.

The following shows how to define a UNIQUE constraint for a column at the column level:

CREATE TABLE table_name(
    ...,
    column_name type UNIQUE,
    ...
);
Code language: SQL (Structured Query Language) (sql)
Or at the table level:

CREATE TABLE table_name(
    ...,
    UNIQUE(column_name)
);
Code language: SQL (Structured Query Language) (sql)
The following illustrates how to define a UNIQUE constraint for multiple columns:

CREATE TABLE table_name(
    ...,
    UNIQUE(column_name1,column_name2,...)
);
Code language: SQL (Structured Query Language) (sql)
Once a UNIQUE constraint is defined, if you attempt to insert or update a value that already exists in the column, SQLite will issue an error and abort the operation.

SQLite UNIQUE constraint examples
Let’s take some examples of using the UNIQUE constraint.

Defining a UNIQUE constraint for one column example
The following statement creates a new table named contacts with a UNIQUE constraint defined for the email column:

CREATE TABLE contacts(
    contact_id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    email TEXT NOT NULL UNIQUE
);
Code language: SQL (Structured Query Language) (sql)
The following example inserts a new row into the contacts table:

INSERT INTO contacts(first_name,last_name,email)
VALUES ('John','Doe','john.doe@gmail.com');
Code language: SQL (Structured Query Language) (sql)
If you attempt to insert a new contact with the same email, you will get an error message:

INSERT INTO contacts(first_name,last_name,email)
VALUES ('Johnny','Doe','john.doe@gmail.com');
Code language: SQL (Structured Query Language) (sql)
Here is the error message:

Error while executing SQL query on database 'chinook': UNIQUE constraint failed: contacts.email
Code language: SQL (Structured Query Language) (sql)
Defining a UNIQUE constraint for multiple columns example
The following statement creates the shapes table with a UNIQUE constraint defined for the background_color and foreground_color columns:

CREATE TABLE shapes(
    shape_id INTEGER PRIMARY KEY,
    background_color TEXT,
    foreground_color TEXT,
    UNIQUE(background_color,foreground_color)
);
Code language: SQL (Structured Query Language) (sql)
The following statement inserts a new row into the shapes table:

INSERT INTO shapes(background_color,foreground_color)
VALUES('red','green');
Code language: SQL (Structured Query Language) (sql)
The following statement works because of no duplication violation in both background_color and foreground_color columns:

INSERT INTO shapes(background_color,foreground_color)
VALUES('red','blue');
Code language: SQL (Structured Query Language) (sql)
However, the following statement causes an error due to the duplicates in both background_color and foreground_color columns:

INSERT INTO shapes(background_color,foreground_color)
VALUES('red','green');
Code language: SQL (Structured Query Language) (sql)
Here is the error:

Error while executing SQL query on database 'chinook': `UNIQUE` constraint failed: shapes.background_color, shapes.foreground_color
Code language: SQL (Structured Query Language) (sql)
SQLite UNIQUE constraint and NULL
SQLite treats all NULL values are different, therefore, a column with a UNIQUE constraint can have multiple NULL values.

The following statement creates a new table named lists whose email column has a UNIQUE constraint:

CREATE TABLE lists(
    list_id INTEGER PRIMARY KEY,
    email TEXT UNIQUE
);
Code language: SQL (Structured Query Language) (sql)
The following statement inserts multiple NULL values into the email column of the lists table:

INSERT INTO lists(email)
VALUES(NULL),(NULL);
Code language: SQL (Structured Query Language) (sql)
Let’s query data from the lists table:

SELECT * FROM lists;
Code language: SQL (Structured Query Language) (sql)
Here is the output:

SQLite UNIQUE Constraint Example
As you can see, even though the email column has a UNIQUE constraint, it can accept multiple NULL values.

In this tutorial, you have learned how to use the SQLite UNIQUE constraint to ensure all values in a column or a group of columns are unique.
"""
"""
Introduction to SQLite CHECK constraints
SQLite CHECK constraints allow you to define expressions to test values whenever they are inserted into or updated within a column.

If the values do not meet the criteria defined by the expression, SQLite will issue a constraint violation and abort the statement.

The CHECK constraints allow you to define additional data integrity checks beyond UNIQUE or NOT NULL to suit your specific application.

SQLite allows you to define a CHECK constraint at the column level or the table level.

The following statement shows how to define a CHECK constraint at the column level:

CREATE TABLE table_name(
    ...,
    column_name data_type CHECK(expression),
    ...
);
Code language: SQL (Structured Query Language) (sql)
and the following statement illustrates how to define a CHECK constraint at the table level:

CREATE TABLE table_name(
    ...,
    CHECK(expression)
);
Code language: SQL (Structured Query Language) (sql)
In this syntax, whenever a row is inserted into a table or an existing row is updated, the expression associated with each CHECK constraint is evaluated and returned a numeric value 0 or 1.

If the result is zero, then a constraint violation occurred. If the result is a non-zero value or NULL, it means no constraint violation occurred.

Note that the expression of a CHECK constraint cannot contain a subquery.

SQLite CHECK constraint examples
Let’s take some examples of using the CHECK constraints.

1) Using SQLite CHECK constraint at the column level example
The following statement creates a new table named contacts:

CREATE TABLE contacts (
    contact_id INTEGER PRIMARY KEY,
    first_name TEXT    NOT NULL,
    last_name  TEXT    NOT NULL,
    email      TEXT,
    phone      TEXT    NOT NULL
                    CHECK (length(phone) >= 10)
);
Code language: SQL (Structured Query Language) (sql)
In the contacts table, the phone column has a CHECK constraint:

CHECK (length(phone) >= 10)
Code language: SQL (Structured Query Language) (sql)
This CHECK constraint ensures that the values in the phone column must be at least 10 characters.

If you attempt to execute the following statement, you will get a constraint violation error:

INSERT INTO contacts(first_name, last_name, phone)
VALUES('John','Doe','408123456');
Code language: SQL (Structured Query Language) (sql)
Here is the error message:

Result: CHECK constraint failed: contacts
Code language: SQL (Structured Query Language) (sql)
The reason was that the phone number that you attempted to insert just has 9 characters while it requires at least 10 characters.

The following statement should work because the value in the phone column has 13 characters, which satisfies the expression in the CHECK constraint:

INSERT INTO contacts(first_name, last_name, phone)
VALUES('John','Doe','(408)-123-456');
Code language: SQL (Structured Query Language) (sql)
2) Using SQLite CHECK constraints at the table level example
The following statement creates a new table named products:

CREATE TABLE products (
    product_id   INTEGER         PRIMARY KEY,
    product_name TEXT            NOT NULL,
    list_price   DECIMAL (10, 2) NOT NULL,
    discount     DECIMAL (10, 2) NOT NULL
                                DEFAULT 0,
    CHECK (list_price >= discount AND
        discount >= 0 AND
        list_price >= 0)
);
Code language: SQL (Structured Query Language) (sql)
In this example, the CHECK constraint is defined at the table level:

CHECK (list_price >= discount AND
            discount >= 0 AND
            list_price >= 0)
Code language: SQL (Structured Query Language) (sql)
The CHECK constraint ensures that list price is always greater or equal to discount and both discount and list price are greater or equal to zero.

The following statement violates the CHECK constraint because the discount is higher than the list price.

INSERT INTO products(product_name, list_price, discount)
VALUES('New Product',900,1000);
Code language: SQL (Structured Query Language) (sql)
The following statement also violates the CHECK constraint because the discount is negative:

INSERT INTO products(product_name, list_price, discount)
VALUES('New XFactor',1000,-10);
Code language: SQL (Structured Query Language) (sql)
Adding CHECK constraints to an existing table
As of version 3.25.2, SQLite does not support adding a CHECK constraint to an existing table.

However, you can follow these steps:

First, create a new table whose structure is the same as the table that you want to add a CHECK constraint. The new table should also include the CHECK constraint:

CREATE TABLE new_table (
    [...],
    CHECK ([...])
);
Code language: SQL (Structured Query Language) (sql)
To get the structure of the old table, you can use the .schema command. Check out the SQLite DESCRIBE table tutorial for more information.

Second, copy data from the old table to the new table.

INSERT INTO new_table SELECT * FROM old_table;
Code language: SQL (Structured Query Language) (sql)
Third, drop the old table:

DROP TABLE old_table;
Code language: SQL (Structured Query Language) (sql)
Fourth, rename the new table to the old one:

ALTER TABLE new_table RENAME TO old_table;
Code language: SQL (Structured Query Language) (sql)
To make all statements above transaction-safe, you should execute all of them within a transaction like this:

BEGIN;
-- create a new table
CREATE TABLE new_table (
    [...],
    CHECK ([...])
);
-- copy data from old table to the new one
INSERT INTO new_table SELECT * FROM old_table;

-- drop the old table
DROP TABLE old_table;

-- rename new table to the old one
ALTER TABLE new_table RENAME TO old_table;

-- commit changes
COMMIT;
Code language: SQL (Structured Query Language) (sql)
In this tutorial, you have learned how to use the SQLite CHECK constraint to ensure values in a column or a group of columns satisfies a condition defined by an expression.
"""
"""Introduction to SQLite ROWID table
Whenever you create a table without specifying the WITHOUT ROWID option, you get an implicit auto-increment column called rowid. The rowid column store 64-bit signed integer that uniquely identifies a row in the table.

Let’s see the following example.

First, create a new table named people that has two columns: first_name,  and last_name:

CREATE TABLE people (
   first_name TEXT NOT NULL,
   last_name TEXT NOT NULL
);
Code language: SQL (Structured Query Language) (sql)
Try It

Second, insert a row into the people table using the following INSERT statement:

INSERT INTO people (first_name, last_name)
VALUES('John', 'Doe');
Code language: SQL (Structured Query Language) (sql)
Try It

Third, query data from the people table using the following SELECT statement:

SELECT
   rowid,
   first_name,
   last_name
FROM
   people;
Code language: SQL (Structured Query Language) (sql)
Try It

SQLite AUTOINCREMENT
As you can see clearly from the output, SQLite implicitly  creates a column named rowid and automatically assigns an integer value whenever you insert a new row into the table.

Note that you can also refer to the rowid column using its aliases: _rowid_ and oid.

When you create a table that has an INTEGER PRIMARY KEY column, this column is the alias of the rowid column.

The following statement drops table people and recreates it. This time, however, we add another column named person_id whose data type is INTEGER and column constraint is PRIMARY KEY:

DROP TABLE people;

CREATE TABLE people (
   person_id INTEGER PRIMARY KEY,
   first_name TEXT NOT NULL,
   last_name TEXT NOT NULL
);
Code language: SQL (Structured Query Language) (sql)
Try It

In this case, the person_id column is actually the rowid column.

How does SQLite assign an integer value to the rowid column?

If you don’t specify the rowid value or you use a NULL value when you insert a new row, SQLite automatically assigns the next sequential integer, which is one larger than the largest rowid in the table. The rowid value starts at 1.

The maximum value of  therowid column is 9,223,372,036,854,775,807, which is very big. If your data reaches this maximum value and you attempt to insert a new row, SQLite will find an unused integer and uses it. If SQLite cannot find any unused integer, it will issue an SQLITE_FULL error. On top of that, if you delete some rows and insert a new row, SQLite will try to reuse the rowid values from the deleted rows.

Let’s take a test on it.

First, insert a row with the maximum value into the people table.

INSERT INTO people (person_id,first_name,last_name)
VALUES(	9223372036854775807,'Johnathan','Smith');
Code language: SQL (Structured Query Language) (sql)
Try It

SQLite maximum rowid value
Second, insert another row without specifying a value for the person_id column:

INSERT INTO people (first_name,last_name)
VALUES('William','Gate');
Code language: SQL (Structured Query Language) (sql)
Try It

SQLite INSERT row without rowid
As clearly shown in the output, the new row received an unused integer.

Consider another example.

First, create a new table named t1 that has one column:

CREATE TABLE t1(c text);
Code language: SQL (Structured Query Language) (sql)
Second, insert some rows into the t1 table:

INSERT INTO t1(c) VALUES('A');
INSERT INTO t1(c) values('B');
INSERT INTO t1(c) values('C');
INSERT INTO t1(c) values('D');
Code language: SQL (Structured Query Language) (sql)
Third, query data from the t1 table:

SELECT rowid, c FROM t1;
Code language: SQL (Structured Query Language) (sql)

Fourth, delete all rows of the t1 table:

DELETE FROM t1;
Code language: SQL (Structured Query Language) (sql)
Fifth, insert some rows into the t1 table:

INSERT INTO t1(c) values('E');
INSERT INTO t1(c) values('F');
INSERT INTO t1(c) values('G');
Code language: SQL (Structured Query Language) (sql)
Finally, query data from the t1 table:

SELECT rowid, c FROM t1;
Code language: SQL (Structured Query Language) (sql)

As you can see, the rowid 1, 2 and 3 have been reused for the new rows.

SQLite AUTOINCREMENT column attribute
SQLite recommends that you should not use AUTOINCREMENT attribute because:

The AUTOINCREMENT keyword imposes extra CPU, memory, disk space, and disk I/O overhead and should be avoided if not strictly needed. It is usually not needed.

In addition, the way SQLite assigns a value for the AUTOINCREMENT column slightly different from the way it does for the rowid column.

Consider the following example.

First, drop and recreate the people table. This time, we use AUTOINCREMENT attribute column:

DROP TABLE people;

CREATE TABLE people (
   person_id INTEGER PRIMARY KEY AUTOINCREMENT,
   first_name text NOT NULL,
   last_name text NOT NULL
);
Code language: SQL (Structured Query Language) (sql)
Try It

Second, insert a row with the maximum rowid value into the people table.

INSERT INTO people (person_id,first_name,last_name)
VALUES(9223372036854775807,'Johnathan','Smith');
Code language: SQL (Structured Query Language) (sql)
Try It

Third, insert another row into the people table.

INSERT INTO people (first_name,last_name)
VALUES('John','Smith');
Code language: SQL (Structured Query Language) (sql)
Try It

This time, SQLite issued an error message because the person_id column did not reuse the number like a rowid column.

[Err] 13 - database or disk is full
Code language: SQL (Structured Query Language) (sql)
When should you use the AUTOINCREMENT column attribute?

The main purpose of using attribute AUTOINCREMENT is to prevent SQLite to reuse a value that has not been used or a value from the previously deleted row.

If you don’t have any requirement like this, you should not use the AUTOINCREMENT attribute in the primary key.

In this tutorial, you have learned how SQLite AUTOINCREMENT attribute works and how it influences the way SQLite assigns values to the primary key column.
"""
