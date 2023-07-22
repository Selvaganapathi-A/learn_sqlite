"""Getting the structure of a table via the SQLite command-line shell program
To find out the structure of a table via the SQLite command-line shell program, you follow these steps:

First, connect to a database via the SQLite command-line shell program:

sqlite3 c:\sqlite\db\chinook.db
Code language: SQL (Structured Query Language) (sql)
Then, issue the following command:

.schema table_name
Code language: SQL (Structured Query Language) (sql)
For example, the following command shows the statement that created the albums table:

.schema albums
Code language: SQL (Structured Query Language) (sql)
Notice that there is no semicolon (;) after the table name. If you add a semicolon (;), the .schema will consider the albums; as the table name and returns nothing because the table albums; does not exist.

Here is the output:

CREATE TABLE IF NOT EXISTS "albums"
(
    [AlbumId] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    [Title] NVARCHAR(160)  NOT NULL,
    [ArtistId] INTEGER  NOT NULL,
    FOREIGN KEY ([ArtistId]) REFERENCES "artists" ([ArtistId])
                ON DELETE NO ACTION ON UPDATE NO ACTION
);
CREATE INDEX [IFK_AlbumArtistId] ON "albums" ([ArtistId]);
Code language: SQL (Structured Query Language) (sql)
Another way to show the structure of a table is to use the PRAGMA command. To do it, you use the following command to format the output:

.header on
.mode column
Code language: SQL (Structured Query Language) (sql)
And use the PRAGMA command as follows:

pragma table_info('albums');
Code language: JavaScript (javascript)
The following picture shows the output:

cid  name      type           notnull  dflt_value  pk
---  --------  -------------  -------  ----------  --
0    AlbumId   INTEGER        1                    1
1    Title     NVARCHAR(160)  1                    0
2    ArtistId  INTEGER        1                    0
Getting the structure of a table using the SQL statement
You can find the structure of a table by querying it from the sqlite_schema table as follows:

SELECT sql
FROM sqlite_schema
WHERE name = 'albums';
Code language: SQL (Structured Query Language) (sql)
Here is the output:

sql
------------
CREATE TABLE "albums"
(
    [AlbumId] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    [Title] NVARCHAR(160)  NOT NULL,
    [ArtistId] INTEGER  NOT NULL,
    FOREIGN KEY ([ArtistId]) REFERENCES "artists" ([ArtistId])
                ON DELETE NO ACTION ON UPDATE NO ACTION
)
Code language: SQL (Structured Query Language) (sql)
In this tutorial, you have learned how to show the structure of a table in SQLite via a command-line shell program or SQL statement.

"""
