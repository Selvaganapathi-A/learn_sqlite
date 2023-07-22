"""
To insert data into a table, you use the INSERT statement. SQLite provides various forms of the INSERT statements that allow you to insert a single row, multiple rows, and default values into a table.

In addition, you can insert a row into a table using data provided by a  SELECT statement.

SQLite INSERT – inserting a single row into a table
To insert a single row into a table, you use the following form of the INSERT statement:

INSERT INTO table (column1,column2 ,..)
VALUES( value1,	value2 ,...);
Code language: SQL (Structured Query Language) (sql)
Let’s examine the INSERT statement in more detail:

First, specify the name of the table to which you want to insert data after the INSERT INTO keywords.
Second, add a comma-separated list of columns after the table name. The column list is optional. However, it is a good practice to include the column list after the table name.
Third, add a comma-separated list of values after the VALUES keyword. If you omit the column list, you have to specify values for all columns in the value list. The number of values in the value list must be the same as the number of columns in the column list.
We will use the artists table in the sample database for the demonstration.


The following statement insert a new row into the artists table:

INSERT INTO artists (name)
VALUES('Bud Powell');
Code language: SQL (Structured Query Language) (sql)
Try It

Because the ArtistId column is an auto-increment column, you can ignore it in the statement. SQLite automatically geneate a sequential integer number to insert into the ArtistId column.

You can verify the insert operation by using the following SELECT statement:

SELECT
	ArtistId,
	Name
FROM
	Artists
ORDER BY
	ArtistId DESC
LIMIT 1;
Code language: SQL (Structured Query Language) (sql)
Try It

SQLite Insert Example
As you see, we have a new row in the artists table.

SQLite INSERT – Inserting multiple rows into a table
To insert multiple rows into a table, you use the following form of the INSERT statement:

INSERT INTO table1 (column1,column2 ,..)
VALUES
   (value1,value2 ,...),
   (value1,value2 ,...),
    ...
   (value1,value2 ,...);
Code language: SQL (Structured Query Language) (sql)
Each value list following the VALUES clause is a row that will be inserted into the table.

The following example inserts three rows into the artists table:

INSERT INTO artists (name)
VALUES
	("Buddy Rich"),
	("Candido"),
	("Charlie Byrd");
Code language: SQL (Structured Query Language) (sql)
Try It

SQLite issued a message:

Row Affected: 3
You can verify the result using the following statement:

SELECT
	ArtistId,
	Name
FROM
	artists
ORDER BY
	ArtistId DESC
LIMIT 3;
Code language: SQL (Structured Query Language) (sql)
Try It

SQLite Insert Multiple Example
SQLite INSERT – Inserting default values
When you create a new table using the CREATE TABLE statement, you can specify default values for columns, or a NULL if a default value is not specified.

The third form of the INSERT statement is INSERT DEFAULT VALUES, which inserts a new row into a table using the default values specified in the column definition or NULL if the default value is not available and the column does not have a NOT NULL constraint.

For example, the following statement inserts a new row into the artists table using INSERT DEFAULT VALUES:

INSERT INTO artists DEFAULT VALUES;
Code language: SQL (Structured Query Language) (sql)
Try It

To verify the insert, you use the following statement:

SELECT
	ArtistId,
	Name
FROM
	artists
ORDER BY
	ArtistId DESC;
Code language: SQL (Structured Query Language) (sql)
Try It

SQLite Insert default values
The default value of the ArtistId column is the next sequential integer . However, the name column does not have any default value, therefore, the INSERT DEFAULT VALUES statement inserts NULL  into it.

SQLite INSERT – Inserting new rows with data provided by a SELECT statement
Suppose you want to backup the artists table, you can follow these steps:

First, create a new table named artists_backup as follows:

CREATE TABLE artists_backup(
   ArtistId INTEGER PRIMARY KEY AUTOINCREMENT,
   Name NVARCHAR
);
Code language: SQL (Structured Query Language) (sql)
Try It

To insert data into the artists_backup table with the data from the artists table, you use the INSERT INTO SELECT statement as follows:

INSERT INTO artists_backup
SELECT ArtistId, Name
FROM artists;
Code language: SQL (Structured Query Language) (sql)
Try It

If you query data from the artists_backup table, you will see all data in the artists table.

SELECT * FROM artists_backup;
Code language: SQL (Structured Query Language) (sql)
Try It

SQLite Insert Into Select
In this tutorial, you have learned how to use various forms of SQLite INSERT statement that insert new rows into a table.


"""
"""
Introduction to SQLite UPDATE statement
To update existing data in a table, you use SQLite UPDATE statement. The following illustrates the syntax of the UPDATE statement:

UPDATE table
SET column_1 = new_value_1,
    column_2 = new_value_2
WHERE
    search_condition
ORDER column_or_expression
LIMIT row_count OFFSET offset;
Code language: SQL (Structured Query Language) (sql)
In this syntax:

First, specify the table where you want to update after the UPDATE clause.
Second, set new value for each column of the table in the SET clause.
Third, specify rows to update using a condition in the WHERE clause. The WHERE clause is optional. If you skip it, the UPDATE statement will update data in all rows of the table.
Finally, use the ORDER BY and LIMIT clauses in the UPDATE statement to specify the number of rows to update.
Notice that if use a negative value in the LIMIT clause, SQLite assumes that there are no limit and updates all rows that meet the condition in the preceding WHERE clause.

The ORDER BY clause should always goes with the LIMIT clause to specify exactly which rows to be updated. Otherwise, you will never know which row will be actually updated; because without the ORDER BY clause, the order of rows in the table is unspecified.

SQLite UPDATE statement examples
We will use the employees table in the sample database to demonstrate the UPDATE statement.


The following SELECT statement gets partial data from the employees table:

SELECT
	employeeid,
	firstname,
	lastname,
	title,
	email
FROM
	employees;
Code language: SQL (Structured Query Language) (sql)
Try It

SQLite Update Table Example
1) Update one column example
Suppose, Jane got married and she wanted to change her last name to her husband’s last name i.e., Smith. In this case, you can update Jane’s last name using the following statement:

UPDATE employees
SET lastname = 'Smith'
WHERE employeeid = 3;
Code language: SQL (Structured Query Language) (sql)
Try It

The expression in the WHERE clause makes sure that we update Jane’s record only. We set the lastname column to a literal string 'Smith'.

To verify the UPDATE, you use the following statement:

SELECT
	employeeid,
	firstname,
	lastname,
	title,
	email
FROM
	employees
WHERE
	employeeid = 3;
Code language: SQL (Structured Query Language) (sql)
Try It

SQLite Update One Column Example
2) Update multiple columns example
Suppose Park Margaret locates in Toronto and you want to change his address, city, and state information. You can use the UPDATE statement to update multiple columns as follows:

UPDATE employees
SET city = 'Toronto',
    state = 'ON',
    postalcode = 'M5P 2N7'
WHERE
    employeeid = 4;
Code language: SQL (Structured Query Language) (sql)
Try It

To verify the UPDATE, you use the following statement:

SELECT
	employeeid,
	firstname,
	lastname,
	state,
	city,
	PostalCode
FROM
	employees
WHERE
	employeeid = 4;
Code language: SQL (Structured Query Language) (sql)
Try It

SQLite Update Multiple Columns Example
3) Update with ORDER BY and LIMIT clauses example
Notice that you need to build SQLite with SQLITE_ENABLE_UPDATE_DELETE_LIMIT option in order to perform UPDATE statement with optional ORDER BY and LIMIT clauses.

Let’s check the email addresses of employees in the employees table:

SELECT
	employeeid,
	firstname,
	lastname,
	email
FROM
	employees;
Code language: SQL (Structured Query Language) (sql)
Try It

SQLite Update Order By Limit
To update one row in the employees table, you use LIMIT 1 clause. To make sure that you update the first row of employees sorted by the first name, you add the ORDER BY firstname clause.

So the following statement updates email of Andrew Adams:

UPDATE employees
SET email = LOWER(
	firstname || "." || lastname || "@chinookcorp.com"
)
ORDER BY
	firstname
LIMIT 1;
Code language: SQL (Structured Query Language) (sql)
Try It

SQLite Update Order By Limit Example
The new email is the combination of the first name, dot (.), last name and the suffix @chinookcorp.com

The LOWER() function converts the email to lower case.

4) Update all rows example
To update all rows in the  employees table, you skip the WHERE clause. For example, the following UPDATE statement changes all email addresses of all employees to lowercase:

UPDATE employees
SET email = LOWER(
	firstname || "." || lastname || "@chinookcorp.com"
);
Code language: SQL (Structured Query Language) (sql)
Try It

SQLite Update all Rows Example
In this tutorial, you have learned how to use the SQLite UPDATE statement to update existing data in a table.
"""
"""
Introduction to SQLite DELETE statement
You have learned how to insert a new row into a table and update existing data of a table. Sometimes, you need to remove rows from a table. In this case, you use SQLite DELETE statement.

The SQLite DELETE statement allows you to delete one row, multiple rows, and all rows in a table. The syntax of the SQLite DELETE statement is as follows:

DELETE FROM table
WHERE search_condition;
Code language: SQL (Structured Query Language) (sql)
In this syntax:

First, specify the name of the table which you want to remove rows after the DELETE FROM keywords.
Second, add a search condition in the WHERE clause to identify the rows to remove. The WHERE clause is an optional part of the DELETE statement. If you omit the WHERE clause, the DELETE statement will delete all rows in the table.
SQLite also provides an extension to the DELETE statement by adding ORDER BY and LIMIT clauses. If you compile SQLite with the SQLITE_ENABLE_UPDATE_DELETE_LIMIT compile-time option, you can use the ORDER BY and LIMIT clause in the DELETE statement like the following form:

DELETE FROM table
WHERE search_condition
ORDER BY criteria
LIMIT row_count OFFSET offset;
Code language: SQL (Structured Query Language) (sql)
The ORDER BY clause sorts the rows filtered by the preceding search_condition in the WHERE clause and the LIMIT clause specifies the number of rows that to be deleted.

Notice that when you use the DELETE statement without a WHERE clause on a table that has no triggers. SQLite will delete all rows in one shot instead of visiting and deleting each individual row. This feature is known as truncate optimization.

SQLite DELETE statement examples
We will use the artists_backup table created in the how to insert rows into table tutorial.

If you did not follow that tutorial, you can create the artists_backup table and insert data into it using the following script:

-- create artists backup table
CREATE TABLE artists_backup(
   artistid INTEGER PRIMARY KEY AUTOINCREMENT,
   name NVARCHAR
);
-- populate data from the artists table
INSERT INTO artists_backup
SELECT artistid,name
FROM artists;
Code language: SQL (Structured Query Language) (sql)
The following statement returns all rows from the artists_backup table:

SELECT
	artistid,
	name
FROM
	artists_backup;
Code language: SQL (Structured Query Language) (sql)
Try It

SQLite Delete Table Example
We have 280 rows in the artists_backup table.

To remove an artist with id 1, you use the following statement:

DELETE FROM artists_backup
WHERE artistid = 1;
Code language: SQL (Structured Query Language) (sql)
Try It

Because we use artistid to identify the artist, the statement removed exactly 1 row.

Suppose you want to delete artists whose names contain the word Santana:

DELETE FROM artists_backup
WHERE name LIKE '%Santana%';
Code language: SQL (Structured Query Language) (sql)
Try It

There are 9 rows whose values in the name column contain the word Santana therefore, these 9 rows were deleted.

To remove all rows in the artists_backup table, you just need to omit the WHERE clause as the following statement:

DELETE FROM artists_backup;
Code language: SQL (Structured Query Language) (sql)
Try It

In this tutorial, you have learned how to use SQLite DELETE statement to remove rows in a table.
"""
"""
Introduction to the SQLite REPLACE statement
The idea of the REPLACE statement is that when a UNIQUE or PRIMARY KEY constraint violation occurs, it does the following:

First, delete the existing row that causes a constraint violation.
Second, insert a new row.
In the second step, if any constraint violation e.g., NOT NULL constraint occurs, the REPLACE statement will abort the action and roll back the transaction.

The following illustrates the syntax of the REPLACE statement.

INSERT OR REPLACE INTO table(column_list)
VALUES(value_list);
Code language: SQL (Structured Query Language) (sql)
Or in a short form:

REPLACE INTO table(column_list)
VALUES(value_list);
Code language: SQL (Structured Query Language) (sql)
Let’s take a look at some examples of using the SQLite REPLACE statement to understand how it works.

The SQLite REPLACE statement examples
First, create a new table named positions with the following structure.

CREATE TABLE IF NOT EXISTS positions (
	id INTEGER PRIMARY KEY,
	title TEXT NOT NULL,
	min_salary NUMERIC
);
Code language: SQL (Structured Query Language) (sql)
Try It

Second, insert some rows into the positions table.

INSERT INTO positions (title, min_salary)
VALUES ('DBA', 120000),
       ('Developer', 100000),
       ('Architect', 150000);
Code language: SQL (Structured Query Language) (sql)
Try It

Third, verify the insert using the following SELECT statement.

SELECT * FROM positions;
Code language: SQL (Structured Query Language) (sql)
Try It

SQLite REPLACE positions table
The following statement creates a unique index on the title column of the positions table to ensure that it doesn’t have any duplicate position title:

CREATE UNIQUE INDEX idx_positions_title
ON positions (title);
Code language: SQL (Structured Query Language) (sql)
Try It

Suppose, you want to add a position into the positions table if it does not exist, in case the position exists, update the current one.

The following REPLACE statement inserts a new row into the positions table because the position title Full Stack Developer is not in the positions table.

REPLACE INTO positions (title, min_salary)
VALUES('Full Stack Developer', 140000);
Code language: SQL (Structured Query Language) (sql)
Try It

SQLite REPLACE insert new row
You can verify the REPLACE operation using the SELECT statement.

SELECT
	id,title,min_salary
FROM
	positions;
Code language: SQL (Structured Query Language) (sql)
Try It

See the following statement.

REPLACE INTO positions (title, min_salary)
VALUES('DBA', 170000);
Code language: SQL (Structured Query Language) (sql)
Try It

SQLite REPLACE - replace the existing row
First, SQLite checked the UNIQUE constraint.

Second, because this statement violated the UNIQUE constraint by trying to add the DBA title that already exists, SQLite deleted the existing row.

Third, SQLite inserted a new row with the data provided by the REPLACE statement.

Notice that the REPLACE statement means INSERT or REPLACE, not INSERT or UPDATE.

See the following statement.

REPLACE INTO positions (id, min_salary)
VALUES(2, 110000);
Code language: SQL (Structured Query Language) (sql)
Try It

What the statement tried to do is to update the min_salary for the position with id 2, which is the developer.

First, the position with id 2 already exists, the REPLACE statement removes it.

Then, SQLite tried to insert a new row with two columns: ( id, min_salary). However, it violates the NOT NULL constraint of the title column. Therefore, SQLite rolls back the transaction.

If the title column does not have the NOT NULL constraint, the REPLACE statement will insert a new row whose the title column is NULL.

In this tutorial, we have shown you how to use the SQLite REPLACE statement to insert or replace a row in a table.
"""
