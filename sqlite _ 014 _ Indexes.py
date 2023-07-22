"""What is an index?
In relational databases, a table is a list of rows. In the same time, each row has the same column structure that consists of cells. Each row also has a consecutive rowid sequence number used to identify the row. Therefore, you can consider a table as a list of pairs: (rowid, row).

Unlike a table, an index has an opposite relationship: (row, rowid). An index is an additional data structure that helps improve the performance of a query.

SQLite Index
SQLite uses B-tree for organizing indexes. Note that B stands for balanced, B-tree is a balanced tree, not a binary tree.

The B-tree keeps the amount of data at both sides of the tree balanced so that the number of levels that must be traversed to locate a row is always in the same approximate number. In addition, querying using equality (=) and ranges (>, >=, <,<=) on the B-tree indexes are very efficient.

How does an index work
Each index must be associated with a specific table. An index consists of one or more columns, but all columns of an index must be in the same table. A table may have multiple indexes.

Whenever you create an index, SQLite creates a B-tree structure to hold the index data.

The index contains data from the columns that you specify in the index and the corresponding rowid value. This helps SQLite quickly locate the row based on the values of the indexed columns.

Imagine an index in the database like an index of a book. By looking at the index, you can quickly identify page numbers based on the keywords.

SQLite CREATE INDEX statement
To create an index, you use the CREATE INDEX statement with the following syntax:

CREATE [UNIQUE] INDEX index_name
ON table_name(column_list);
Code language: SQL (Structured Query Language) (sql)
To create an index, you specify three important information:

The name of the index after the CREATE INDEX keywords.
The name of the table to the index belongs.
A list of columns of the index.
In case you want to make sure that values in one or more columns are unique like email and phone, you use the UNIQUE option in the CREATE INDEX statement. The CREATE UNIQUE INDEX creates a new unique index.

SQLite UNIQUE index example
Let’s create a new table named contacts for demonstration.

CREATE TABLE contacts (
	first_name text NOT NULL,
	last_name text NOT NULL,
	email text NOT NULL
);
Code language: SQL (Structured Query Language) (sql)
Try It

Suppose, you want to enforce that the email is unique, you create a unique index as follows:

CREATE UNIQUE INDEX idx_contacts_email
ON contacts (email);
Code language: SQL (Structured Query Language) (sql)
Try It

To test this.

First,  insert a row into the contacts table.

INSERT INTO contacts (first_name, last_name, email)
VALUES('John','Doe','john.doe@sqlitetutorial.net');
Code language: SQL (Structured Query Language) (sql)
Try It

Second, insert another row with a duplicate email.

INSERT INTO contacts (first_name, last_name, email)
VALUES('Johny','Doe','john.doe@sqlitetutorial.net');
Code language: SQL (Structured Query Language) (sql)
Try It

SQLite issued an error message indicating that the unique index has been violated. Because when you inserted the second row, SQLite checked and made sure that the email is unique across of rows in email of the contacts table.

Let’s insert two more rows into the contacts table.

INSERT INTO contacts (first_name, last_name, email)
VALUES('David','Brown','david.brown@sqlitetutorial.net'),
      ('Lisa','Smith','lisa.smith@sqlitetutorial.net');
Code language: SQL (Structured Query Language) (sql)
Try It

If you query data from the contacts table based on a specific email, SQLite will use the index to locate the data. See the following statement:

SELECT
	first_name,
	last_name,
	email
FROM
	contacts
WHERE
	email = 'lisa.smith@sqlitetutorial.net';
Code language: SQL (Structured Query Language) (sql)
Try It

SQLite index example
To check if SQLite uses the index or not, you use the EXPLAIN QUERY PLAN statement as follows:

EXPLAIN QUERY PLAN
SELECT
	first_name,
	last_name,
	email
FROM
	contacts
WHERE
	email = 'lisa.smith@sqlitetutorial.net';
Code language: SQL (Structured Query Language) (sql)
Try It

SQLite Index Explain example
SQLite multicolumn index example
If you create an index that consists of one column, SQLite uses that column as the sort key. In case you create an index that has multiple columns, SQLite uses the additional columns as the second, third, … as the sort keys.

SQLite sorts the data on the multicolumn index by the first column specified in the CREATE INDEX statement. Then, it sorts the duplicate values by the second column, and so on.

Therefore, the column order is very important when you create a multicolumn index.

To utilize a multicolumn index, the query must contain the condition that has the same column order as defined in the index.

The following statement creates a multicolumn index on the first_name and last_name columns of the contacts table:

CREATE INDEX idx_contacts_name
ON contacts (first_name, last_name);
Code language: SQL (Structured Query Language) (sql)
Try It

If you query the contacts table with one of the following conditions in the WHERE clause, SQLite will utilize the multicolumn index to search for data.

1) filter data by the first_name column.

WHERE
	first_name = 'John';
Code language: SQL (Structured Query Language) (sql)
2)filter data by both first_name and last_name columns:

WHERE
	first_name = 'John' AND last_name = 'Doe';
Code language: SQL (Structured Query Language) (sql)
However, SQLite will not use the multicolumn index if you use one of the following conditions.

1)filter by the last_name column only.

WHERE
	last_name = 'Doe';
Code language: SQL (Structured Query Language) (sql)
2) filter by first_name OR last_name columns.

last_name = 'Doe' OR first_name = 'John';
Code language: SQL (Structured Query Language) (sql)
SQLite Show Indexes
To find all indexes associated with a table, you use the following command:

PRAGMA index_list('table_name');
Code language: SQL (Structured Query Language) (sql)
For example, this statement shows all the indexes of the contacts table:

PRAGMA index_list('playlist_track');
Code language: SQL (Structured Query Language) (sql)
Here is the output:

SQLite index - show indexes
To get the information about the columns in an index, you use the following command:

PRAGMA index_info('idx_contacts_name');
Code language: SQL (Structured Query Language) (sql)
This example returns the column list of the index idx_contacts_name:


Another way to get all indexes from a database is to query from the sqlite_master table:

SELECT
   type,
   name,
   tbl_name,
   sql
FROM
   sqlite_master
WHERE
   type= 'index';
Code language: SQL (Structured Query Language) (sql)
SQLite DROP INDEX statement
To remove an index from a database, you use the DROP INDEX statement as follows:

DROP INDEX [IF EXISTS] index_name;
Code language: SQL (Structured Query Language) (sql)
In this syntax, you specify the name of the index that you want to drop after the DROP INDEX keywords. The IF EXISTS option removes an index only if it exists.

For example, you use the following statement to remove the idx_contacts_name index:

DROP INDEX idx_contacts_name;
Code language: SQL (Structured Query Language) (sql)
Try It

The idx_contacts_name index is removed completely from the database.

In this tutorial, you have learned about SQLite index and how to utilize indexes for improving the performance of query or enforcing unique constraints.
"""


"""Introduction to the SQLite expression-based index
When you create an index, you often use one or more columns in a table. Besides the normal indexes, SQLite allows you to form an index based on expressions involved table columns. This kind of index is called an expression based index.

The following query selects the customers whose the length of the company is greater than 10 characters.

SELECT customerid,
       company
  FROM customers
 WHERE length(company) > 10
 ORDER BY length(company) DESC;
Code language: SQL (Structured Query Language) (sql)
If you use the EXPLAIN QUERY PLAN statement, you will find that SQLite query planner had to scan the whole customers table to return the result set.

EXPLAIN QUERY PLAN
SELECT customerid,
       company
  FROM customers
 WHERE length(company) > 10
 ORDER BY length(company) DESC;
Code language: SQL (Structured Query Language) (sql)
The SQLite query planner is a software component that determines the best algorithm or query plan to execute an SQL statement. As of SQLite version 3.8.0, the query planner component was rewritten to run faster and generate better query plans. The rewrite is known as the next generation query planner or NGQP.

To create an index based on the expression LENGTH(company), you use the following statement.

CREATE INDEX customers_length_company
ON customers(LENGTH(company));
Code language: SQL (Structured Query Language) (sql)
Now if you execute the query above again, SQLite will use the expression index to search to select the data, which is faster.

How the SQLite expression-based index work
The SQLite query planner uses the expression-based index only when the expression, which you specified in the CREATE INDEX statement, appears the same as in the WHERE clause or ORDER BY clause.

For example, in the sample database, we have the invoice_items table.

The following statement creates an index using the unit price and quantity columns.

CREATE INDEX invoice_line_amount
ON invoice_items(unitprice*quantity);
Code language: SQL (Structured Query Language) (sql)
However, when you run the following query:

EXPLAIN QUERY PLAN
SELECT invoicelineid,
       invoiceid,
       unitprice*quantity
FROM invoice_items
WHERE quantity*unitprice > 10;
Code language: SQL (Structured Query Language) (sql)
The SQLite query planner did not use the index because the expression in the CREATE INDEX ( unitprice*quantity) is not the same as the one in the WHERE clause (quantity*unitprice)

SQLite expression based index restriction
The following lists all the restrictions on the expression that appears in the CREATE INDEX statement.

The expression must refer to the columns of the table that is being indexed only. It cannot refer to the columns of other tables.
The expression can only use the deterministic function call.
The expression cannot use a subquery.
In this tutorial, you have learned how to use the SQLite expression based index to improve the query performance.
"""
