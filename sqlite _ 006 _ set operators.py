"""
Introduction to SQLite UNION operator
Sometimes, you need to combine data from multiple tables into a complete result set. It may be for tables with similar data within the same database or maybe you need to combine similar data from multiple databases.

To combine rows from two or more queries into a single result set, you use SQLite UNION operator. The following illustrates the basic syntax of the UNION operator:

query_1
UNION [ALL]
query_2
UNION [ALL]
query_3
...;
Code language: SQL (Structured Query Language) (sql)
Both UNION and UNION ALL operators combine rows from result sets into a single result set. The UNION operator removes eliminate duplicate rows, whereas the UNION ALL operator does not.

Because the UNION ALL operator does not remove duplicate rows, it runs faster than the UNION operator.

The following are rules to union data:

The number of columns in all queries must be the same.
The corresponding columns must have compatible data types.
The column names of the first query determine the column names of the combined result set.
The GROUP BY and HAVING clauses are applied to each individual query, not the final result set.
The ORDER BY clause is applied to the combined result set, not within the individual result set.
Note that the difference between UNION and JOIN e.g., INNER JOIN or LEFT JOIN is that the JOIN clause combines columns from multiple related tables, while UNION combines rows from multiple similar tables.

Suppose we have two tables t1 and t2 with the following structures:

CREATE TABLE t1(
    v1 INT
);

INSERT INTO t1(v1)
VALUES(1),(2),(3);

CREATE TABLE t2(
    v2 INT
);
INSERT INTO t2(v2)
VALUES(2),(3),(4);
Code language: SQL (Structured Query Language) (sql)
The following statement combines the result sets of the t1 and t2 table using the UNION operator:

SELECT v1
  FROM t1
UNION
SELECT v2
  FROM t2;
Code language: SQL (Structured Query Language) (sql)
Here is the output:

SQLite UNION example
The following picture illustrates the UNION operation of t1 and t2 tables:

SQLite UNION
The following statement combines the result sets of t1 and t2 table using the  UNION ALL operator:

SELECT v1
  FROM t1
UNION ALL
SELECT v2
  FROM t2;
Code language: SQL (Structured Query Language) (sql)
The following picture shows the output:

SQLite UNION ALL example
The following picture illustrates the UNION ALL operation of the result sets of t1 and t2 tables:

SQLite UNION ALL
SQLite UNION examples
Let’s take some examples of using the UNION operator.

1) SQLite UNION example
This statement uses the UNION operator to combine names of employees and customers into a single list:

SELECT FirstName, LastName, 'Employee' AS Type
FROM employees
UNION
SELECT FirstName, LastName, 'Customer'
FROM customers;

Code language: SQL (Structured Query Language) (sql)
Here is the output:


2) SQLite UNION with ORDER BY example
This example uses the UNION operator to combine the names of the employees and customers into a single list. In addition, it uses the ORDER BY clause to sort the name list by first name and last name.

SELECT FirstName, LastName, 'Employee' AS Type
FROM employees
UNION
SELECT FirstName, LastName, 'Customer'
FROM customers
ORDER BY FirstName, LastName;
Code language: SQL (Structured Query Language) (sql)
Here is the output:

SQLITE UNION with ORDER BY example
In this tutorial, you have learned how to use SQLite UNION operator to combine rows from result sets into a single result set. You also learned the differences between UNION and UNION ALL operators.


"""

"""
Introduction to SQLite EXCEPT operator
SQLite EXCEPT operator compares the result sets of two queries and returns distinct rows from the left query that are not output by the right query.

The following shows the syntax of the EXCEPT operator:

SELECT select_list1
FROM table1
EXCEPT
SELECT select_list2
FROM table2
Code language: SQL (Structured Query Language) (sql)
This query must conform to the following rules:

First, the number of columns in the select lists of both queries must be the same.
Second, the order of the columns and their types must be comparable.
The following statements create two tables t1 and t2 and insert some data into both tables:

CREATE TABLE t1(
    v1 INT
);

INSERT INTO t1(v1)
VALUES(1),(2),(3);

CREATE TABLE t2(
    v2 INT
);
INSERT INTO t2(v2)
VALUES(2),(3),(4);
Code language: SQL (Structured Query Language) (sql)
The following statement illustrates how to use the EXCEPT operator to compare result sets of two queries:

SELECT v1
FROM t1
EXCEPT
SELECT v2
FROM t2;
Code language: SQL (Structured Query Language) (sql)
The output is 1.

The following picture illustrates the EXCEPT operation:

SQLite EXCEPT Operator Illustration
SQLite EXCEPT examples
We will use the artists and albums tables from the sample database for the demonstration.


The following statement finds artist ids of artists who do not have any album in the albums table:

SELECT ArtistId
FROM artists
EXCEPT
SELECT ArtistId
FROM albums;
Code language: SQL (Structured Query Language) (sql)
The output is as follows:

SQLite EXCEPT Example
In this tutorial, you have learned how to use the SQLite EXCEPT operator to compare two queries and return unique rows from the left query that are not output by the right query.


"""

"""Introduction to SQLite INTERSECT operator
SQLite INTERSECT operator compares the result sets of two queries and returns distinct rows that are output by both queries.

The following illustrates the syntax of the INTERSECT operator:

SELECT select_list1
FROM table1
INTERSECT
SELECT select_list2
FROM table2
Code language: SQL (Structured Query Language) (sql)
The basic rules for combining the result sets of two queries are as follows:

First, the number and the order of the columns in all queries must be the same.
Second, the data types must be comparable.
For the demonstration, we will create two tables t1 and t2 and insert some data into both:

CREATE TABLE t1(
    v1 INT
);

INSERT INTO t1(v1)
VALUES(1),(2),(3);

CREATE TABLE t2(
    v2 INT
);
INSERT INTO t2(v2)
VALUES(2),(3),(4);
Code language: SQL (Structured Query Language) (sql)
The following statement illustrates how to use the INTERSECT operator to compare result sets of two queries:

SELECT v1
FROM t1
INTERSECT
SELECT v2
FROM t2;
Code language: SQL (Structured Query Language) (sql)
Here is the output:

SQLite INTERSECT operator example
The following picture illustrates the INTERSECT operation:

SQLite INTERSECT
SQLite INTERSECT example
For the demonstration, we will use the customers and invoices tables from the sample database.


The following statement finds customers who have invoices:

SELECT CustomerId
FROM customers
INTERSECT
SELECT CustomerId
FROM invoices
ORDER BY CustomerId;
Code language: SQL (Structured Query Language) (sql)
The following picture shows the partial output:

SQLite INTERSECT example
In this tutorial, you have learned how to use the SQLite INTERSECT operator to compare two queries and return distinct rows that are output by both queries.


"""
