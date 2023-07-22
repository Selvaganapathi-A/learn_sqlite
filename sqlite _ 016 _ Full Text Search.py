"""Introduction to SQLite full-text search
A virtual table is a custom extension to SQLite. A virtual table is like a normal table. The difference between a virtual table and a normal table is where the data come from i.e., when you process a normal table, SQLite accesses the database file to retrieve data. However, when you access a virtual table, SQLite calls the custom code to get the data. The custom code can have specified logic to handle certain tasks such as getting data from multiple data sources.

To use full-text search in SQLite, you use FTS5 virtual table module.

The following CREATE VIRTUAL TABLE statement creates an FTS5 table with two columns:

CREATE VIRTUAL TABLE table_name
USING FTS5(column1,column2...);
Code language: SQL (Structured Query Language) (sql)
Notice that you cannot add types, constraints, or PRIMARY KEY declaration in the CREATE VIRTUAL TABLE statement for creating an FTS5 table. If you do so, SQLite will issue an error.

Like creating a normal table without specifying the primary key column, SQLite adds an implicit rowid column to the FTS5 table.

The following example creates an FTS5 table named posts with two columns title and body.

CREATE VIRTUAL TABLE posts
USING FTS5(title, body);
Code language: SQL (Structured Query Language) (sql)
Similar to a normal table, you can insert data into the posts table as follows:

INSERT INTO posts(title,body)
VALUES('Learn SQlite FTS5','This tutorial teaches you how to perform full-text search in SQLite using FTS5'),
('Advanced SQlite Full-text Search','Show you some advanced techniques in SQLite full-text searching'),
('SQLite Tutorial','Help you learn SQLite quickly and effectively');
Code language: SQL (Structured Query Language) (sql)
And query data against it:

SELECT * FROM posts;
Code language: SQL (Structured Query Language) (sql)
SQLite full-text search - table data
Querying data using full-text search
You can execute a full-text query against an FTS5 table using one of these three ways.

First, use a MATCH operator in the WHERE clause of the SELECT statement. For example, to get all rows that have the term fts5, you use the following query:

SELECT *
FROM posts
WHERE posts MATCH 'fts5';
Code language: SQL (Structured Query Language) (sql)
SQLite full-text search - MATCH operator
Second, use an equal (=) operator in the WHERE clause of the SELECT statement. The following statement returns the same result as the statement above:

SELECT *
FROM posts
WHERE posts = 'fts5';
Code language: SQL (Structured Query Language) (sql)
Third, use a tabled-value function syntax. In this way, you use the search term as the first table argument:

SELECT *
FROM posts('fts5');
Code language: SQL (Structured Query Language) (sql)
By default, FTS5 is case-independent. It treats the terms fts5FTS5 and Fts5 the same.

To sort the search results from the most to least relevant, you use the ORDER BY clause as follows:

SELECT *
FROM posts
WHERE posts MATCH 'text'
ORDER BY rank;
Code language: SQL (Structured Query Language) (sql)
SQLite full-text search - Sorting
Using full-text query syntax
A full-text search query is made up of phrases, where each phrase is an ordered list of one or more tokens. You can use the “+” operator to concatenate two phrases as the following example:

"learn SQLite"
"learn + SQLite"
Code language: SQL (Structured Query Language) (sql)
FTS5 determines whether a document matches a phrase if the document contains at least one subsequence of tokens that match the sequence of tokens used to construct the phrase.

The following query returns all documents that match the search term Learn SQLite:

SELECT *
FROM posts
WHERE posts MATCH 'learn SQLite';
Code language: SQL (Structured Query Language) (sql)
SQLite full-text search - query syntax
Prefix searches
You can use the asterisk (*) as a prefix token. When a phrase contains the asterisk (*), it will match any document that contains the token that begins with the phrase. For example, search* matches with search, searching, searches, etc. See the following example:

SELECT *
FROM posts
WHERE posts = 'search*';
Code language: SQL (Structured Query Language) (sql)
SQLite full-text search - prefix searches
Boolean operators
You can use the Boolean operator e.g., NOT, OR, or AND to combine queries.

q1 AND q2: matches if both q1 and q2 queries match.
q1 OR q2: matches if either query q1 or q2 matches.
q1 NOT q2: matches if query q1 matches and q2 doesn’t match.
For example, to get the documents that match the learn phrase but doesn’t match the FTS5 phrase, you use the NOT operator as follows:

SELECT *
FROM posts
WHERE posts MATCH 'learn NOT text';
Code language: SQL (Structured Query Language) (sql)
SQLite full-text search - NOT operator
To search for documents that match either phrase learn or text, you use the OR operator as the following example:

SELECT *
FROM posts
WHERE posts MATCH 'learn OR text';
Code language: SQL (Structured Query Language) (sql)
SQLite full-text search - OR operator
To find the documents that match both SQLite and searching, you use the AND operator as shown below:

SELECT *
FROM posts
WHERE posts MATCH 'sqlite AND searching';
Code language: SQL (Structured Query Language) (sql)
SQLite full-text search - AND operator
To change the operator precedence, you use parenthesis to group expressions. For example:

SELECT *
FROM posts
WHERE posts MATCH 'search AND sqlite OR help';
Code language: SQL (Structured Query Language) (sql)
SQLite full-text search - Combine Logical Operators
The statement returns documents that match search and sqlite or help. To find the documents that match search and either sqlite or help, you use parenthesis as follows:

SELECT *
FROM posts
WHERE posts MATCH 'search AND (sqlite OR help)';
Code language: SQL (Structured Query Language) (sql)
SQLite full-text search - Operators precedence
Built-in auxiliary functions
SQLite provides three built-in auxiliary functions that can be used within full-text queries on the FTS5 table.

The bm25() returns a value that represents the accuracy of the current match, the lower value means a better match.
The highlight() auxiliary function returns a copy of the text with search terms surrounded by a specified markup e.g.,<b>search term </b>
The snippet() selects a short fragment of text in order to maximize the number of search terms it contains.
For example, the following query uses the highlight() function to decorate the search terms using the <b>tag</b>:

SELECT highlight(posts,0, '<b>', '</b>') title,
       highlight(posts,1, '<b>', '</b>') body
FROM posts
WHERE posts MATCH 'SQLite'
ORDER BY rank;
Code language: SQL (Structured Query Language) (sql)
SQLite full-text search - highlight function
In this tutorial, you have learned how to use SQLite full-text search features via FTS5 virtual table module.
"""
