"""What is a view
In database theory, a view is a result set of a stored query. A view is the way to pack a query into a named object stored in the database.

You can access the data of the underlying tables through a view. The tables that the query in the view definition refers to are called base tables.

A view is useful in some cases:

First, views provide an abstraction layer over tables. You can add and remove the columns in the view without touching the schema of the underlying tables.
Second, you can use views to encapsulate complex queries with joins to simplify the data access.
SQLite view is read only. It means you cannot use INSERT, DELETE, and  UPDATE statements to update data in the base tables through the view.

SQLite CREATE VIEW statement
To create a view, you use the CREATE VIEW statement as follows:

CREATE [TEMP] VIEW [IF NOT EXISTS] view_name[(column-name-list)]
AS
   select-statement;
Code language: SQL (Structured Query Language) (sql)
First, specify a name for the view. The IF NOT EXISTS option only creates a new view if it doesn’t exist. If the view already exists, it does nothing.

Second, use the the TEMP or TEMPORARY option if you want the view to be only visible in the current database connection. The view is called a temporary view and SQLite automatically removes the temporary view whenever the database connection is closed.

Third, specify a  SELECT statement for the view. By default, the columns of the view derive from the result set of the SELECT statement. However, you can assign the names of the view columns that are different from the column name of the table

SQLite CREATE VIEW examples
Let’s take some examples of creating a new view using the CREATE VIEW statement.

1) Creating a view to simplify a complex query
The following query gets data from the tracks, albums, media_types and genres tables in the sample database using the inner join clause.

SELECT
   trackid,
   tracks.name,
   albums.Title AS album,
   media_types.Name AS media,
   genres.Name AS genres
FROM
   tracks
INNER JOIN albums ON Albums.AlbumId = tracks.AlbumId
INNER JOIN media_types ON media_types.MediaTypeId = tracks.MediaTypeId
INNER JOIN genres ON genres.GenreId = tracks.GenreId;
Code language: SQL (Structured Query Language) (sql)
Try It

MySQL CREATE VIEW example
To create a view based on this query, you use the following statement:

CREATE VIEW v_tracks
AS
SELECT
	trackid,
	tracks.name,
	albums.Title AS album,
	media_types.Name AS media,
	genres.Name AS genres
FROM
	tracks
INNER JOIN albums ON Albums.AlbumId = tracks.AlbumId
INNER JOIN media_types ON media_types.MediaTypeId = tracks.MediaTypeId
INNER JOIN genres ON genres.GenreId = tracks.GenreId;
Code language: SQL (Structured Query Language) (sql)
Try It

From now on, you can use the following simple query instead of the complex one above.

SELECT * FROM v_tracks;
Code language: SQL (Structured Query Language) (sql)
Try It

2) Creating a view with custom column names
The following statement creates a view named v_albums that contains album title and the length of album in minutes:

CREATE VIEW v_albums (
    AlbumTitle,
    Minutes
)
AS
    SELECT albums.title,
           SUM(milliseconds) / 60000
      FROM tracks
           INNER JOIN
           albums USING (
               AlbumId
           )
     GROUP BY AlbumTitle;
Code language: SQL (Structured Query Language) (sql)
In this example, we specified new columns for the view AlbumTitle for the albums.title column and Minutes for the expression SUM(milliseconds) / 60000

This query returns data from the v_albums view:

SELECT * FROM v_albums;
"""

"""
Introduction to SQLite DROP VIEW statement
The DROP VIEW statement deletes a view from the database schema. Here is the basic syntax of the DROP VIEW statement:

DROP VIEW [IF EXISTS] [schema_name.]view_name;
Code language: SQL (Structured Query Language) (sql)
In this syntax:

First, specify the name of the view that you wants to remove after the DROP VIEW keywords.
Second, specify the schema of the view that you want to delete.
Third, use the IF EXISTS option to remove a view only if it exists. If the view does not exist, the DROP VIEW IF EXISTS statement does nothing. However, trying to drop a non-existing view without the IF EXISTS option will result in an error.
Note that the DROP VIEW statement only removes the view object from the database schema. It does not remove the data of the base tables.

SQLite DROP VIEW statement examples
This statement creates a view that summarizes data from the invoices and invoice_items in the sample database:

CREATE VIEW v_billings (
    invoiceid,
    invoicedate,
    total
)
AS
    SELECT invoiceid,
           invoicedate,
           sum(unit_price * quantity)
      FROM invoices
           INNER JOIN
           invoice_items USING (
               invoice_id
           );
Code language: SQL (Structured Query Language) (sql)
To delete the v_billings view, you use the following DROP VIEW statement:

DROP VIEW v_billings;
Code language: SQL (Structured Query Language) (sql)
This example uses the IF EXISTS option to delete a non-existing view:

DROP VIEW IF EXISTS v_xyz;
Code language: SQL (Structured Query Language) (sql)
It does not return any error. However, if you don’t use the IF EXISTS option like the following example, you will get an error:

DROP VIEW v_xyz;
Code language: SQL (Structured Query Language) (sql)
Here is the error message:

Error while executing SQL query on database 'chinook': no such view: v_xyz
In this tutorial, you have learned how to use the SQLite DROP VIEW statement to remove a view from its database schema.
"""
