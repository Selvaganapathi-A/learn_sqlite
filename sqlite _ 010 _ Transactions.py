"""SQLite & ACID
SQLite is a transactional database that all changes and queries are atomic, consistent, isolated, and durable (ACID).

SQLite guarantees all the transactions are ACID compliant even if the transaction is interrupted by a program crash, operation system dump, or power failure to the computer.

Atomic: a transaction should be atomic. It means that a change cannot be broken down into smaller ones. When you commit a transaction, either the entire transaction is applied or not.
Consistent: a transaction must ensure to change the database from one valid state to another. When a transaction starts and executes a statement to modify data, the database becomes inconsistent. However, when the transaction is committed or rolled back, it is important that the transaction must keep the database consistent.
Isolation: a pending transaction performed by a session must be isolated from other sessions. When a session starts a transaction and executes the INSERT or UPDATE statement to change the data, these changes are only visible to the current session, not others. On the other hand, the changes committed by other sessions after the transaction started should not be visible to the current session.
Durable: if a transaction is successfully committed, the changes must be permanent in the database regardless of the condition such as power failure or program crash. On the contrary, if the program crashes before the transaction is committed, the change should not persist.
SQLite transaction statements
By default, SQLite operates in auto-commit mode. It means that for each command, SQLite starts, processes, and commits the transaction automatically.

To start a transaction explicitly, you use the following steps:

First, open a transaction by issuing the BEGIN TRANSACTION command.

BEGIN TRANSACTION;
Code language: SQL (Structured Query Language) (sql)
After executing the statement BEGIN TRANSACTION, the transaction is open until it is explicitly committed or rolled back.

Second, issue SQL statements to select or update data in the database. Note that the change is only visible to the current session (or client).

Third, commit the changes to the database by using the COMMIT or COMMIT TRANSACTION statement.

COMMIT;
Code language: SQL (Structured Query Language) (sql)
If you do not want to save the changes, you can roll back using the ROLLBACK or ROLLBACK TRANSACTION statement:

ROLLBACK;
Code language: SQL (Structured Query Language) (sql)
SQLite transaction example
We will create two new tables: accounts and account_changes for the demonstration.

The accounts table stores data about the account numbers and their balances. The account_changes table stores the changes of the accounts.

First, create the accounts and account_changes tables by using the following CREATE TABLE statements:

CREATE TABLE accounts (
	account_no INTEGER NOT NULL,
	balance DECIMAL NOT NULL DEFAULT 0,
	PRIMARY KEY(account_no),
        CHECK(balance >= 0)
);

CREATE TABLE account_changes (
	change_no INT NOT NULL PRIMARY KEY,
	account_no INTEGER NOT NULL,
	flag TEXT NOT NULL,
	amount DECIMAL NOT NULL,
	changed_at TEXT NOT NULL
);
Code language: SQL (Structured Query Language) (sql)
Second, insert some sample data into the accounts table.

INSERT INTO accounts (account_no,balance)
VALUES (100,20100);

INSERT INTO accounts (account_no,balance)
VALUES (200,10100);
Code language: SQL (Structured Query Language) (sql)
Third, query data from the accounts table:

SELECT * FROM accounts;
Code language: SQL (Structured Query Language) (sql)

Fourth, transfer 1000 from account 100 to 200, and log the changes to the table account_changes in a single transaction.

BEGIN TRANSACTION;

UPDATE accounts
   SET balance = balance - 1000
 WHERE account_no = 100;

UPDATE accounts
   SET balance = balance + 1000
 WHERE account_no = 200;

INSERT INTO account_changes(account_no,flag,amount,changed_at)
VALUES(100,'-',1000,datetime('now'));

INSERT INTO account_changes(account_no,flag,amount,changed_at)
VALUES(200,'+',1000,datetime('now'));

COMMIT;
Code language: SQL (Structured Query Language) (sql)
Fifth, query data from the accounts table:

SELECT * FROM accounts;
Code language: SQL (Structured Query Language) (sql)

As you can see, balances have been updated successfully.

Sixth, query the contents of the account_changes table:

SELECT * FROM account_changes;
Code language: SQL (Structured Query Language) (sql)

Let’s take another example of rolling back a transaction.

First, attempt to deduct 20,000 from account 100:

BEGIN TRANSACTION;

UPDATE accounts
   SET balance = balance - 20000
 WHERE account_no = 100;

INSERT INTO account_changes(account_no,flag,amount,changed_at)
VALUES(100,'-',20000,datetime('now'));
Code language: SQL (Structured Query Language) (sql)
SQLite issued an error due to not enough balance:

[SQLITE_CONSTRAINT]  Abort due to constraint violation (CHECK constraint failed: accounts)
Code language: CSS (css)
However, the log has been saved to the account_changes table:

SELECT * FROM account_changes;
Code language: SQL (Structured Query Language) (sql)

Second, roll back the transaction by using the ROLLBACK statement:

ROLLBACK;
Code language: SQL (Structured Query Language) (sql)
Finally, query data from the account_changes table, you will see that the change no #3 is not there anymore:

SELECT * FROM account_changes;
Code language: SQL (Structured Query Language) (sql)

In this tutorial, you have learned how to deal with SQLite transactions by using the BEGIN TRANSACTION, COMMIT, and ROLLBACK statements to control the transactions in the SQLite database.
"""
