"""The SQLite CASE expression evaluates a list of conditions and returns an expression based on the result of the evaluation.

The CASE expression is similar to the IF-THEN-ELSE statement in other programming languages.

You can use the CASE expression in any clause or statement that accepts a valid expression. For example, you can use the CASE expression in clauses such as WHERE, ORDER BY, HAVING, SELECT and statements such as SELECT, UPDATE, and DELETE.

SQLite provides two forms of the CASE expression: simple CASE and searched CASE.

SQLite simple CASE expression
The simple CASE expression compares an expression to a list of expressions to return the result. The following illustrates the syntax of the simple CASE expression.

CASE case_expression
     WHEN when_expression_1 THEN result_1
     WHEN when_expression_2 THEN result_2
     ...
     [ ELSE result_else ]
END
Code language: SQL (Structured Query Language) (sql)
The simple CASE expression compares the case_expression to the expression appears in the first WHEN clause, when_expression_1, for equality.

If the case_expression equals when_expression_1, the simple CASE returns the expression in the corresponding THEN clause, which is the result_1.

Otherwise, the simple CASE expression compares the case_expression with the expression in the next WHEN clause.

In case no case_expression matches the when_expression, the CASE expression returns the result_else in the ELSE clause. If you omit the ELSE clause, the CASE expression returns NULL.

The simple CASE expression uses short-circuit evaluation. In other words, it returns the result and stop evaluating other conditions as soon as it finds a match.

Simple CASE example
Let’s take a look at the customers table in the sample database.

customers
Suppose, you have to make a report of the customer groups with the logic that if a customer locates in the USA, this customer belongs to the domestic group, otherwise the customer belongs to the foreign group.

To make this report, you use the simple CASE expression in the SELECT statement as follows:

SELECT customerid,
       firstname,
       lastname,
       CASE country
           WHEN 'USA'
               THEN 'Domestic'
           ELSE 'Foreign'
       END CustomerGroup
FROM
    customers
ORDER BY
    LastName,
    FirstName;
Code language: SQL (Structured Query Language) (sql)
Try It

SQLite searched CASE expression
The searched CASE expression evaluates a list of expressions to decide the result. Note that the simple CASE expression only compares for equality, while the searched CASE expression can use any forms of comparison.

The following illustrates the syntax of the searched CASE expression.

CASE
     WHEN bool_expression_1 THEN result_1
     WHEN bool_expression_2 THEN result_2
     [ ELSE result_else ]
END
Code language: SQL (Structured Query Language) (sql)
The searched CASE expression evaluates the Boolean expressions in the sequence specified and return the corresponding result if the expression evaluates to true.

In case no expression evaluates to true, the searched CASE expression returns the expression in the ELSE clause if specified. If you omit the ELSE clause, the searched CASE expression returns NULL.

Similar to the simple CASE expression, the searched CASE expression stops the evaluation when a condition is met.

Searched CASE example
We will use the tracks table for the demonstration.


Suppose you want to classify the tracks based on its length such as less a minute, the track is short; between 1 and 5 minutes, the track is medium; greater than 5 minutes, the track is long.

To achieve this, you use the searched CASE expression as follows:

SELECT
	trackid,
	name,
	CASE
		WHEN milliseconds < 60000 THEN
			'short'
		WHEN milliseconds > 60000 AND milliseconds < 300000 THEN 'medium'
		ELSE
			'long'
		END category
FROM
	tracks;
Code language: SQL (Structured Query Language) (sql)
Try It

SQLite Searched CASE example
In this tutorial, you have learned about SQLite CASE expression to form conditional logic inside a SQL query.

"""
