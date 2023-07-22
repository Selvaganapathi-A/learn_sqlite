"""
Introduction to SQLite subquery
A subquery is a SELECT statement nested in another statement. See the following statement.

SELECT column_1
FROM table_1
WHERE column_1 = (
   SELECT column_1
   FROM table_2
);
Code language: SQL (Structured Query Language) (sql)
The following query is the outer query:

SELECT column_1
  FROM table_1
 WHERE colum_1 =
Code language: SQL (Structured Query Language) (sql)
And the following query is the subquery.

(SELECT column_1
  FROM table_2)
Code language: SQL (Structured Query Language) (sql)
You must use a pair of parentheses to enclose a subquery. Note that you can nest a subquery inside another subquery with a certain depth.

Typically, a subquery returns a single row as an atomic value, though it may return multiple rows for comparing values with the IN operator.

You can use a subquery in the SELECT, FROM, WHERE, and JOIN clauses.

SQLite subquery examples
We will use the tracks and albums tables from the sample database for the demonstration.


1) SQLite subquery in the WHERE clause example
You can use a simple subquery as a search condition. For example, the following statement returns all the tracks in the album with the title  Let There Be Rock

SELECT trackid,
       name,
       albumid
FROM tracks
WHERE albumid = (
   SELECT albumid
   FROM albums
   WHERE title = 'Let There Be Rock'
);
Code language: SQL (Structured Query Language) (sql)
SQLite Subquery example
The subquery returns the id of the album with the title 'Let There Be Rock'. The query uses the equal operator (=) to compare albumid returned by the subquery with the  albumid in the tracks table.

If the subquery returns multiple values, you can use the IN operator to check for the existence of a single value against a set of value.

See the following employees and customers table in the sample database:


For example, the following query returns the customers whose sales representatives are in Canada.

SELECT customerid,
       firstname,
       lastname
  FROM customers
 WHERE supportrepid IN (
           SELECT employeeid
             FROM employees
            WHERE country = 'Canada'
       );
Code language: SQL (Structured Query Language) (sql)
SQLite Subquery with IN operator example
The subquery returns a list of ids of the employees who locate in Canada. The outer query uses the IN operator to find the customers who have the sales representative id in the list.

2) SQLite subquery in the FROM clause example
Sometimes you want to apply aggregate functions to a column multiple times. For example, first, you want to sum the size of an album and then calculate the average size of all albums. You may come up with the following query.

SELECT AVG(SUM(bytes)
FROM tracks
GROUP BY albumid;
Code language: SQL (Structured Query Language) (sql)
This query is not valid.

To fix it, you can use a subquery in the FROM clause as follows:

SELECT
	AVG(album.size)
FROM
	(
		SELECT
			SUM(bytes) SIZE
		FROM
			tracks
		GROUP BY
			albumid
	) AS album;
Code language: SQL (Structured Query Language) (sql)
AVG(album.size)
---------------
  338288920.317
In this case, SQLite first executes the subquery in the FROM clause and returns a result set. Then, SQLite uses this result set as a derived table in the outer query.

SQLite correlated subquery
All the subqueries you have seen so far can be executed independently. In other words, it does not depend on the outer query.

The correlated subquery is a subquery that uses the values from the outer query. Unlike an ordinal subquery, a correlated subquery cannot be executed independently.

The correlated subquery is not efficient because it is evaluated for each row processed by the outer query.

The following query uses a correlated subquery to return the albums whose size is less than 10MB.

SELECT albumid,
       title
  FROM albums
 WHERE 10000000 > (
                      SELECT sum(bytes)
                        FROM tracks
                       WHERE tracks.AlbumId = albums.AlbumId
                  )
 ORDER BY title;
Code language: SQL (Structured Query Language) (sql)
SQLite Correlated Subquery Example
How the query works.

For each row processed in the outer query, the correlated subquery calculates the size of the albums from the tracks that belong the current album using the SUM function.
The predicate in the WHERE clause filters the albums that have the size greater than or equal 10MB (10000000 bytes).
SQLite correlated subquery in the SELECT clause example
The following query uses a correlated subquery in the SELECT clause to return the number of tracks in an album.

SELECT albumid,
       title,
       (
           SELECT count(trackid)
             FROM tracks
            WHERE tracks.AlbumId = albums.AlbumId
       )
       tracks_count
  FROM albums
 ORDER BY tracks_count DESC;
Code language: SQL (Structured Query Language) (sql)
SQLite Subquery in SELECT clause example
In this tutorial, we have introduced you to the subquery and shown various ways to use a subquery in a query to select data from tables.


"""

""" Introduction to the SQLite REPLACE statement
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

In this tutorial, we have shown you how to use the SQLite REPLACE statement to insert or replace a row in a table. """
