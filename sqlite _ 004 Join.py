# Join Tables
"""
SQLite Join

Summary: in this tutorial, you will learn about various kinds of SQLite joins to query data from two or more tables.

For the demonstration, we will use the artists and albums tables from the sample database.


An artist can have zero or many albums while an album belongs to one artist.

To query data from both artists and albums tables, you use can use an INNER JOIN, LEFT JOIN, or CROSS JOIN clause. Each join clause determines how SQLite uses data from one table to match with rows in another table.

Note that SQLite doesn’t directly support the RIGHT JOIN and FULL OUTER JOIN.

SQLite INNER JOIN
The following statement returns the album titles and their artist names:

SELECT
    Title,
    Name
FROM
    albums
INNER JOIN artists
    ON artists.ArtistId = albums.ArtistId;
Code language: SQL (Structured Query Language) (sql)
Here is the partial output:


In this example, the INNER JOIN clause matches each row from the albums table with every row from the artists table based on the join condition (artists.ArtistId = albums.ArtistId) specified after the ON keyword.

If the join condition evaluates to true (or 1), the columns of rows from both albums and artists tables are included in the result set.

This query uses table aliases (l for the albums table and r for artists table) to shorten the query:

SELECT
    l.Title,
    r.Name
FROM
    albums l
INNER JOIN artists r ON
    r.ArtistId = l.ArtistId;
Code language: SQL (Structured Query Language) (sql)
In case the column names of joined tables are the same e.g., ArtistId, you can use the USING syntax as follows:

SELECT
   Title,
   Name
FROM
   albums
INNER JOIN artists USING(ArtistId);
Code language: SQL (Structured Query Language) (sql)
The clause USING(ArtistId) is equipvalent to the clause ON artists.ArtistId = albums.ArtistId.

SQLite LEFT JOIN
This statement selects the artist names and album titles from the artists and albums tables using the LEFT JOIN clause:

SELECT
    Name,
    Title
FROM
    artists
LEFT JOIN albums ON
    artists.ArtistId = albums.ArtistId
ORDER BY Name;
Code language: SQL (Structured Query Language) (sql)
Here is the output:

sqlite join - left join example
The LEFT JOIN clause selects data starting from the left table (artists) and matching rows in the right table (albums) based on the join condition (artists.ArtistId = albums.ArtistId) .

The left join returns all rows from the artists table (or left table) and the matching rows from the albums table (or right table).

If a row from the left table doesn’t have a matching row in the right table, SQLite includes columns of the rows in the left table and NULL for the columns of the right table.

Similar to the INNER JOIN clause, you can use the USING syntax for the join condition as follows:

SELECT
   Name,
   Title
FROM
   artists
LEFT JOIN albums USING (ArtistId)
ORDER BY
   Name;
Code language: SQL (Structured Query Language) (sql)
If you want to find artists who don’t have any albums, you can add a WHERE clause as shown in the following query:

SELECT
    Name,
    Title
FROM
    artists
LEFT JOIN albums ON
    artists.ArtistId = albums.ArtistId
WHERE Title IS NULL
ORDER BY Name;
Code language: SQL (Structured Query Language) (sql)
This picture shows the partial output:

sqlite join - left join with a where clause example
Generally, this type of query allows you to find rows that are available in the left table but don’t have corresponding rows in the right table.

Note that LEFT JOIN and LEFT OUTER JOIN are synonyms.

SQLite CROSS JOIN
The CROSS JOIN clause creates a Cartesian product of rows from the joined tables.

Unlike the INNER JOIN and LEFT JOIN clauses, a CROSS JOIN doesn’t have a join condition. Here is the basic syntax of the CROSS JOIN clause:

SELECT
    select_list
FROM table1
CROSS JOIN table2;
Code language: SQL (Structured Query Language) (sql)
The CROSS JOIN combines every row from the first table (table1) with every row from the second table (table2) to form the result set.

If the first table has N rows, the second table has M rows, the final result will have NxM rows.

A practical example of the CROSS JOIN clause is to combine two sets of data for forming an initial data set for further processing. For example, you have a list of products and months, and you want to make a plan when you can sell which products.

The following script creates the products and calendars tables:

CREATE TABLE products(
    product text NOT null
);

INSERT INTO products(product)
VALUES('P1'),('P2'),('P3');



CREATE TABLE calendars(
    y int NOT NULL,
    m int NOT NULL
);

INSERT INTO calendars(y,m)
VALUES
    (2019,1),
    (2019,2),
    (2019,3),
    (2019,4),
    (2019,5),
    (2019,6),
    (2019,7),
    (2019,8),
    (2019,9),
    (2019,10),
    (2019,11),
    (2019,12);
Code language: SQL (Structured Query Language) (sql)
This query uses the CROSS JOIN clause to combine the products with the months:

SELECT *
FROM products
CROSS JOIN calendars;
Code language: SQL (Structured Query Language) (sql)
Here is the output:

In this tutorial, you have learned various kind of SQLite joins that allow you to query from multiple tables.
"""
# Inner Join
"""
SQLite Inner Join

Summary: this tutorial shows you how to use SQLite inner join clause to query data from multiple tables.

Introduction to SQLite inner join clause
In relational databases, data is often distributed in many related tables. A table is associated with another table using foreign keys.

To query data from multiple tables, you use INNER JOIN clause. The INNER JOIN clause combines columns from correlated tables.

Suppose you have two tables: A and B.

A has a1, a2, and f columns. B has b1, b2, and f column. The A table links to the B table using a foreign key column named f.

The following illustrates the syntax of the inner join clause:

SELECT a1, a2, b1, b2
FROM A
INNER JOIN B on B.f = A.f;
Code language: SQL (Structured Query Language) (sql)
For each row in the A table, the INNER JOIN clause compares the value of the f column with the value of the f column in the B table. If the value of the f column in the A table equals the value of the f column in the B table, it combines data from a1, a2, b1, b2, columns and includes this row in the result set.

In other words, the INNER JOIN clause returns rows from the A table that has the corresponding row in B table.

This logic is applied if you join more than 2 tables.

See the following example.

SQLite Inner Join Example
Only the rows in the A table: (a1,1), (a3,3) have the corresponding rows in the B table (b1,1), (b2,3) are included in the result set.

The following diagram illustrates the INNER JOIN clause:

SQLite inner join venn diagram
SQLite INNER JOIN examples
Let’s take a look at the tracks and albums tables in the sample database. The tracks table links to the albums table via AlbumId column.


In the tracks table, the AlbumId column is a foreign key. And in the albums table, the AlbumId is the primary key.

To query data from both tracks and albums tables, you use the following statement:

SELECT
	trackid,
	name,
	title
FROM
	tracks
INNER JOIN albums ON albums.albumid = tracks.albumid;
Code language: SQL (Structured Query Language) (sql)
Try It

SQLite Inner Join 2 Tables Example
For each row in the tracks table, SQLite uses the value in the albumid column of the tracks table to compare with the value in the albumid of the albums table. If SQLite finds a match, it combines data of rows in both tables in the result set.

You can include the AlbumId columns from both tables in the final result set to see the effect.

SELECT
    trackid,
    name,
    tracks.albumid AS album_id_tracks,
    albums.albumid AS album_id_albums,
    title
FROM
    tracks
    INNER JOIN albums ON albums.albumid = tracks.albumid;
Code language: SQL (Structured Query Language) (sql)
Try It

SQLite Inner Join Example
SQLite inner join – 3 tables example
See the following tables:tracks albums and artists


One track belongs to one album and one album have many tracks. The tracks table associated with the albums table via albumid column.

One album belongs to one artist and one artist has one or many albums. The albums table links to the artists table via artistid column.

To query data from these tables, you need to use two inner join clauses in the SELECT statement as follows:

SELECT
    trackid,
    tracks.name AS track,
    albums.title AS album,
    artists.name AS artist
FROM
    tracks
    INNER JOIN albums ON albums.albumid = tracks.albumid
    INNER JOIN artists ON artists.artistid = albums.artistid;
Code language: SQL (Structured Query Language) (sql)
Try It

SQLite Inner Join 3 tables
You can use a WHERE clause to get the tracks and albums of the artist with id 10 as the following statement:

SELECT
	trackid,
	tracks.name AS Track,
	albums.title AS Album,
	artists.name AS Artist
FROM
	tracks
INNER JOIN albums ON albums.albumid = tracks.albumid
INNER JOIN artists ON artists.artistid = albums.artistid
WHERE
	artists.artistid = 10;
Code language: SQL (Structured Query Language) (sql)
Try It

SQLite INNER JOIN with WHERE clause
In this tutorial, you have learned how to use SQLite INNER JOIN clause to query data from multiple tables.
"""
# Left Join
"""
SQLite Left Join
Summary: in this tutorial, you will learn how to use SQLite LEFT JOIN clause to query data from multiple tables.

Introduction to SQLite LEFT JOIN clause
Similar to the INNER JOIN clause, the LEFT JOIN clause is an optional clause of the SELECT statement. You use the LEFT JOIN clause to query data from multiple related tables.

Suppose we have two tables: A and B.

A has m and f columns.
B has n and f columns.
To perform join between A and B using LEFT JOIN clause, you use the following statement:

SELECT
	a,
	b
FROM
	A
LEFT JOIN B ON A.f = B.f
WHERE search_condition;
Code language: SQL (Structured Query Language) (sql)
The expression A.f = B.f is a conditional expression. Besides the equality (=) operator, you can use other comparison operators such as greater than (>), less than (<), etc.

The statement returns a result set that includes:

Rows in table A (left table) that have corresponding rows in table B.
Rows in the table A table and the rows in the table B filled with NULL values in case the row from table A does not have any corresponding rows in table B.
In other words, all rows in table A are included in the result set whether there are matching rows in table B or not.

In case you have a WHERE clause in the statement, the search_condition in the WHERE clause is applied after the matching of the LEFT JOIN clause completes.

See the following illustration of the LEFT JOIN clause between the A and B tables.

SQLite left join example
All rows in the table A are included in the result set.

Because the second row (a2,2) does not have a corresponding row in table B, the LEFT JOIN clause creates a fake row filled with NULL.

The following Venn Diagram illustrates the LEFT JOIN clause.

SQLite Left Join Venn Diagram
It is noted that LEFT OUTER JOIN is the same as LEFT JOIN.

SQLite LEFT JOIN examples
We will use the artists and albums tables in the sample database for demonstration.


One album belongs to one artist. However, one artist may have zero or more albums.

To find artists who do not have any albums by using the LEFT JOIN clause, we select artists and their corresponding albums. If an artist does not have any albums, the value of the AlbumId column is NULL.

To display the artists who do not have any albums first, we have two choices:

First, use ORDER BY clause to list the rows whose AlbumId is NULL values first.
Second, use WHERE clause and IS NULL operator to list only artists who do not have any albums.
The following statement uses the LEFT JOIN clause with the ORDER BY clause.

SELECT
   artists.ArtistId,
   AlbumId
FROM
   artists
LEFT JOIN albums ON
   albums.ArtistId = artists.ArtistId
ORDER BY
   AlbumId;
Code language: SQL (Structured Query Language) (sql)
Try It

The following statement uses the LEFT JOIN clause with the WHERE clause.

SELECT
   artists.ArtistId
   , AlbumId
FROM
   artists
LEFT JOIN albums ON
   albums.ArtistId = artists.ArtistId
WHERE
   AlbumId IS NULL;
Code language: SQL (Structured Query Language) (sql)
Try It

In this tutorial, you have learned how to use SQLite LEFT JOIN clause to query data from multiple tables.
"""

# Cross Join

"""
SQLite CROSS JOIN with a Practical Example

Summary: in this tutorial, you will learn how to use SQLite CROSS JOIN to combine two or more result sets from multiple tables.

Introduction to SQLite CROSS JOIN clause
If you use a LEFT JOIN, INNER JOIN, or CROSS JOIN without the ON or USING clause, SQLite produces the Cartesian product of the involved tables. The number of rows in the Cartesian product is the product of the number of rows in each involved tables.

Suppose, we have two tables A and B. The following statements perform the cross join and produce a cartesian product of the rows from the A and B tables.

SELECT *
FROM A JOIN B;
Code language: SQL (Structured Query Language) (sql)
SELECT *
FROM A
INNER JOIN B;
Code language: SQL (Structured Query Language) (sql)
SELECT *
FROM A
CROSS JOIN B;
Code language: SQL (Structured Query Language) (sql)
SELECT *
FROM A, B;
Code language: SQL (Structured Query Language) (sql)
Suppose, the A table has N rows and B table has M rows, the CROSS JOIN of these two tables will produce a result set that contains NxM rows.

Imagine that if you have the third table C with K rows, the result of the CROSS JOIN clause of these three tables will contain NxMxK rows, which may be very huge. Therefore, you should be very careful when using the CROSS JOIN clause.

You use the INNER JOIN and LEFT JOIN clauses more often than the CROSS JOIN clause. However, you will find the CROSS JOIN clause very useful in some cases.

For example, when you want to have a matrix that has two dimensions filled with data completely like members and dates data in a membership database. You want to check the attendants of members for all relevant dates. In this case, you may use the CROSS JOIN clause as the following statement:

SELECT name,
       date
FROM members
CROSS JOIN dates;
Code language: SQL (Structured Query Language) (sql)
SQLite CROSS JOIN clause example
The following statements create the ranks and suits tables that store the ranks and suits for a deck of cards and insert the complete data into these two tables.

CREATE TABLE ranks (
    rank TEXT NOT NULL
);

CREATE TABLE suits (
    suit TEXT NOT NULL
);

INSERT INTO ranks(rank)
VALUES('2'),('3'),('4'),('5'),('6'),('7'),('8'),('9'),('10'),('J'),('Q'),('K'),('A');

INSERT INTO suits(suit)
VALUES('Clubs'),('Diamonds'),('Hearts'),('Spades');
Code language: SQL (Structured Query Language) (sql)
The following statement uses the CROSS JOIN clause to return a complete deck of cards data:

SELECT rank,
       suit
  FROM ranks
       CROSS JOIN
       suits
ORDER BY suit;
Code language: SQL (Structured Query Language) (sql)
rank	suit
2	Clubs
3	Clubs
4	Clubs
5	Clubs
6	Clubs
7	Clubs
8	Clubs
9	Clubs
10	Clubs
J	Clubs
Q	Clubs
K	Clubs
A	Clubs
2	Diamonds
3	Diamonds
4	Diamonds
5	Diamonds
6	Diamonds
7	Diamonds
8	Diamonds
9	Diamonds
10	Diamonds
J	Diamonds
Q	Diamonds
K	Diamonds
A	Diamonds
2	Hearts
3	Hearts
4	Hearts
5	Hearts
6	Hearts
7	Hearts
8	Hearts
9	Hearts
10	Hearts
J	Hearts
Q	Hearts
K	Hearts
A	Hearts
2	Spades
3	Spades
4	Spades
5	Spades
6	Spades
7	Spades
8	Spades
9	Spades
10	Spades
J	Spades
Q	Spades
K	Spades
A	Spades
In this tutorial, you have learned how to use the SQLite CROSS JOIN clause to produce a Cartesian product of multiple tables involved in the join.
"""
# FULL OUTER JOIN
"""
SQLite FULL OUTER JOIN Emulation

Summary: in this tutorial, you will learn how to emulate SQLite full outer join using the UNION and LEFT JOIN clauses.

Introduction to SQL FULL OUTER JOIN clause
In theory, the result of the FULL OUTER JOIN is a combination of  a LEFT JOIN and a RIGHT JOIN. The result set of the full outer join has NULL values for every column of the table that does not have a matching row in the other table. For the matching rows, the FULL OUTER JOIN produces a single row with values from columns of the rows in both tables.

The following picture illustrates the result of the FULL OUTER JOIN clause:

SQLite full outer join
See the following cats and dogs tables.

-- create and insert data into the dogs table
CREATE TABLE dogs (
    type       TEXT,
    color TEXT
);

INSERT INTO dogs(type, color)
VALUES('Hunting','Black'), ('Guard','Brown');

-- create and insert data into the cats table
CREATE TABLE cats (
    type       TEXT,
    color TEXT
);

INSERT INTO cats(type,color)
VALUES('Indoor','White'),
      ('Outdoor','Black');
Code language: SQL (Structured Query Language) (sql)
The following statement uses the FULL OUTER JOIN clause to query data from the dogs and cats tables.

SELECT *
FROM dogs
FULL OUTER JOIN cats
    ON dogs.color = cats.color;
Code language: SQL (Structured Query Language) (sql)
The following shows the result of the statement above:

Type	Color	Type	Color
Hunting	Black	Outdoor	Black
Guard	Brown	NULL	NULL
NULL	NULL	Indoor	White
Unfortunately, SQLite does not support the RIGHT JOIN clause and also the FULL OUTER JOIN clause. However, you can easily emulate the FULL OUTER JOIN by using the LEFT JOIN clause.

Emulating SQLite full outer join
The following statement emulates the FULL OUTER JOIN clause in SQLite:

SELECT d.type,
         d.color,
         c.type,
         c.color
FROM dogs d
LEFT JOIN cats c USING(color)
UNION ALL
SELECT d.type,
         d.color,
         c.type,
         c.color
FROM cats c
LEFT JOIN dogs d USING(color)
WHERE d.color IS NULL;
Code language: SQL (Structured Query Language) (sql)
How the query works.

Because SQLilte does not support the RIGHT JOIN clause, we use the LEFT JOIN clause in the second SELECT statement instead and switch the positions of the cats and dogs tables.
The UNION ALL clause retains the duplicate rows from the result sets of both queries.
The WHERE clause in the second SELECT statement removes rows that already included in the result set of the first SELECT statement.
In this tutorial, you have learned how to use the UNION ALL and LEFT JOIN clauses to emulate the SQLite FULL OUTER JOIN clause.
"""

"""
SQLite Self-Join

Summary: in this tutorial, you will learn about a special type of join called SQLite self-join that allows you to join table to itself.

Note that you should be familiar with  INNER JOIN and LEFT JOIN clauses before going forward with this tutorial.

Introduction to SQLite self-join
The self-join is a special kind of joins that allow you to join a table to itself using either LEFT JOIN or INNER JOIN clause. You use self-join to create a result set that joins the rows with the other rows within the same table.

Because you cannot refer to the same table more than one in a query, you need to use a table alias to assign the table a different name when you use self-join.

The self-join compares values of the same or different columns in the same table. Only one table is involved in the self-join.

You often use self-join to query parents/child relationship stored in a table or to obtain running totals.

SQLite self-join examples
We will use the employees table in the sample database for demonstration.


The employees table stores not only employee data but also organizational data. The ReportsTo column specifies the reporting relationship between employees.

If an employee reports to a manager, the value of the ReportsTo column of the employee’s row is equal to the value of the EmployeeId column of the manager’s row. In case an employee does not report to anyone, the ReportsTo column is NULL.

To get the information on who is the direct report of whom, you use the following statement:

SELECT m.firstname || ' ' || m.lastname AS 'Manager',
       e.firstname || ' ' || e.lastname AS 'Direct report'
FROM employees e
INNER JOIN employees m ON m.employeeid = e.reportsto
ORDER BY manager;
Code language: SQL (Structured Query Language) (sql)
Try It

SQLite self join example
The statement used the INNER JOIN clause to join the employees to itself. The employees table has two roles: employees and managers.

Because we used the INNER JOIN clause to join the employees table to itself, the result set does not have the row whose manager column contains a NULL value.

Note that the concatenation operator || concatenates multiple strings into a single string. In the example, we use the concatenation operator to from the full names of the employees by concatenating the first name, space, and last name.

In case you want to query the CEO who does not report to anyone, you need to change the INNER JOIN clause to LEFT JOIN clause in the query above.

SQLite self join with left join example
Andrew Adams is the CEO because he does not report anyone.

You can use the self-join technique to find the employees located in the same city as the following query:

SELECT DISTINCT
	e1.city,
	e1.firstName || ' ' || e1.lastname AS fullname
FROM
	employees e1
INNER JOIN employees e2 ON e2.city = e1.city
   AND (e1.firstname <> e2.firstname AND e1.lastname <> e2.lastname)
ORDER BY
	e1.city;
Code language: SQL (Structured Query Language) (sql)
Try It

SQLite self join - employees locate in the same city
The join condition has two expressions:

e1.city = e2.city to make sure that both employees located in the same city
e.firstname <> e2.firstname AND e1.lastname <> e2.lastname to ensure that e1 and e2 are not the same employee with the assumption that there aren’t employees who have the same first name and last name.
In this tutorial, we have shown you how to use the SQLite self-join technique to join a table to itself.
"""

"""
SQLite FULL OUTER JOIN Emulation

Summary: in this tutorial, you will learn how to emulate SQLite full outer join using the UNION and LEFT JOIN clauses.

Introduction to SQL FULL OUTER JOIN clause
In theory, the result of the FULL OUTER JOIN is a combination of  a LEFT JOIN and a RIGHT JOIN. The result set of the full outer join has NULL values for every column of the table that does not have a matching row in the other table. For the matching rows, the FULL OUTER JOIN produces a single row with values from columns of the rows in both tables.

The following picture illustrates the result of the FULL OUTER JOIN clause:

SQLite full outer join
See the following cats and dogs tables.

-- create and insert data into the dogs table
CREATE TABLE dogs (
    type       TEXT,
    color TEXT
);

INSERT INTO dogs(type, color)
VALUES('Hunting','Black'), ('Guard','Brown');

-- create and insert data into the cats table
CREATE TABLE cats (
    type       TEXT,
    color TEXT
);

INSERT INTO cats(type,color)
VALUES('Indoor','White'),
      ('Outdoor','Black');
Code language: SQL (Structured Query Language) (sql)
The following statement uses the FULL OUTER JOIN clause to query data from the dogs and cats tables.

SELECT *
FROM dogs
FULL OUTER JOIN cats
    ON dogs.color = cats.color;
Code language: SQL (Structured Query Language) (sql)
The following shows the result of the statement above:

Type	Color	Type	Color
Hunting	Black	Outdoor	Black
Guard	Brown	NULL	NULL
NULL	NULL	Indoor	White
Unfortunately, SQLite does not support the RIGHT JOIN clause and also the FULL OUTER JOIN clause. However, you can easily emulate the FULL OUTER JOIN by using the LEFT JOIN clause.

Emulating SQLite full outer join
The following statement emulates the FULL OUTER JOIN clause in SQLite:

SELECT d.type,
         d.color,
         c.type,
         c.color
FROM dogs d
LEFT JOIN cats c USING(color)
UNION ALL
SELECT d.type,
         d.color,
         c.type,
         c.color
FROM cats c
LEFT JOIN dogs d USING(color)
WHERE d.color IS NULL;
Code language: SQL (Structured Query Language) (sql)
How the query works.

Because SQLilte does not support the RIGHT JOIN clause, we use the LEFT JOIN clause in the second SELECT statement instead and switch the positions of the cats and dogs tables.
The UNION ALL clause retains the duplicate rows from the result sets of both queries.
The WHERE clause in the second SELECT statement removes rows that already included in the result set of the first SELECT statement.
In this tutorial, you have learned how to use the UNION ALL and LEFT JOIN clauses to emulate the SQLite FULL OUTER JOIN clause.

"""
