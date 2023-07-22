"""What is an SQLite trigger
An SQLite trigger is a named database object that is executed automatically when an INSERT, UPDATE or DELETE statement is issued against the associated table.

When do we need SQLite triggers
You often use triggers to enable sophisticated auditing. For example, you want to log the changes in the sensitive data such as salary and address whenever it changes.

In addition, you use triggers to enforce complex business rules centrally at the database level and prevent invalid transactions.

SQLite CREATE TRIGGER statement
To create a new trigger in SQLite, you use the CREATE TRIGGER statement as follows:

CREATE TRIGGER [IF NOT EXISTS] trigger_name
   [BEFORE|AFTER|INSTEAD OF] [INSERT|UPDATE|DELETE]
   ON table_name
   [WHEN condition]
BEGIN
 statements;
END;
Code language: SQL (Structured Query Language) (sql)
In this syntax:

First,  specify the name of the trigger after the CREATE TRIGGER keywords.
Next, determine when the trigger is fired such as BEFORE, AFTER, or INSTEAD OF. You can create BEFORE and AFTER triggers on a table. However, you can only create an INSTEAD OF trigger on a view.
Then, specify the event that causes the trigger to be invoked such as INSERT, UPDATE, or DELETE.
After that, indicate the table to which the trigger belongs.
Finally, place the trigger logic in the BEGIN END block, which can be any valid SQL statements.
If you combine the time when the trigger is fired and the event that causes the trigger to be fired, you have a total of 9 possibilities:

BEFORE INSERT
AFTER INSERT
BEFORE UPDATE
AFTER UPDATE
BEFORE DELETE
AFTER DELETE
INSTEAD OF INSERT
INSTEAD OF DELETE
INSTEAD OF UPDATE
Suppose you use a UPDATE statement to update 10 rows in a table, the trigger that associated with the table is fired 10 times. This trigger is called FOR EACH ROW trigger. If the trigger associated with the table is fired one time, we call this trigger a FOR EACH STATEMENT trigger.

As of version 3.9.2, SQLite only supports FOR EACH ROW triggers. It has not yet supported the FOR EACH STATEMENT triggers.

If you use a condition in the WHEN clause, the trigger is only invoked when the condition is true. In case you omit the WHEN clause, the trigger is executed for all rows.

Notice that if you drop a table, all associated triggers are also deleted. However, if the trigger references other tables, the trigger is not removed or changed if other tables are removed or updated.

For example, a trigger references to a table named people, you drop the people table or rename it, you need to manually change the definition of the trigger.

You can access the data of the row being inserted, deleted, or updated using the OLD and NEW references in the form: OLD.column_name and NEW.column_name.

the OLD and NEW references are available depending on the event that causes the trigger to be fired.

The following table illustrates the rules.:

Action	Reference
INSERT	NEW is available
UPDATE	Both NEW and OLD are available
DELETE	OLD is available
SQLite triggers examples
Let’s create a new table called leads to store all business leads of the company.

CREATE TABLE leads (
	id integer PRIMARY KEY,
	first_name text NOT NULL,
	last_name text NOT NULL,
	phone text NOT NULL,
	email text NOT NULL,
	source text NOT NULL
);
Code language: SQL (Structured Query Language) (sql)
1) SQLite BEFORE INSERT trigger example
Suppose you want to validate the email address before inserting a new lead into the leads table. In this case, you can use a BEFORE INSERT trigger.

First, create a BEFORE INSERT trigger as follows:

CREATE TRIGGER validate_email_before_insert_leads
   BEFORE INSERT ON leads
BEGIN
   SELECT
      CASE
	WHEN NEW.email NOT LIKE '%_@__%.__%' THEN
   	  RAISE (ABORT,'Invalid email address')
       END;
END;
Code language: SQL (Structured Query Language) (sql)
We used the NEW reference to access the email column of the row that is being inserted.

To validate the email, we used the LIKE operator to determine whether the email is valid or not based on the email pattern. If the email is not valid, the RAISE function aborts the insert and issues an error message.

Second, insert a row with an invalid email into the leads table.

INSERT INTO leads (first_name,last_name,email,phone)
VALUES('John','Doe','jjj','4089009334');
Code language: SQL (Structured Query Language) (sql)
SQLite issued an error: “Invalid email address” and aborted the execution of the insert.

Third, insert a row with a valid email.

INSERT INTO leads (first_name, last_name, email, phone)
VALUES ('John', 'Doe', 'john.doe@sqlitetutorial.net', '4089009334');
Code language: SQL (Structured Query Language) (sql)
Because the email is valid, the insert statement executed successfully.

SELECT
	first_name,
	last_name,
	email,
	phone
FROM
	leads;
Code language: SQL (Structured Query Language) (sql)
SQLite TRIGGER Leads Table
2) SQLite AFTER UPDATE trigger example
The phones and emails of the leads are so important that you can’t afford to lose this information. For example, someone accidentally updates the email or phone to the wrong ones or even delete it.

To protect this valuable data, you use a trigger to log all changes which are made to the phone and email.

First, create a new table called lead_logs to store the historical data.

CREATE TABLE lead_logs (
	id INTEGER PRIMARY KEY,
	old_id int,
	new_id int,
	old_phone text,
	new_phone text,
	old_email text,
	new_email text,
	user_action text,
	created_at text
);
Code language: SQL (Structured Query Language) (sql)
Second, create an AFTER UPDATE trigger to log data to the lead_logs table whenever there is an update in the email or phone column.

CREATE TRIGGER log_contact_after_update
   AFTER UPDATE ON leads
   WHEN old.phone <> new.phone
        OR old.email <> new.email
BEGIN
	INSERT INTO lead_logs (
		old_id,
		new_id,
		old_phone,
		new_phone,
		old_email,
		new_email,
		user_action,
		created_at
	)
VALUES
	(
		old.id,
		new.id,
		old.phone,
		new.phone,
		old.email,
		new.email,
		'UPDATE',
		DATETIME('NOW')
	) ;
END;
Code language: SQL (Structured Query Language) (sql)
You notice that in the condition in the WHEN clause specifies that the trigger is invoked only when there is a change in either email or phone column.

Third, update the last name of John from Doe to Smith.

UPDATE leads
SET
   last_name = 'Smith'
WHERE
   id = 1;
Code language: SQL (Structured Query Language) (sql)
The trigger log_contact_after_update was not invoked because there was no change in email or phone.

Fourth, update both email and phone of John to the new ones.

UPDATE leads
SET
   phone = '4089998888',
   email = 'john.smith@sqlitetutorial.net'
WHERE
   id = 1;
Code language: SQL (Structured Query Language) (sql)
If you check the log table, you will see there is a new entry there.

SELECT
   old_phone,
   new_phone,
   old_email,
   new_email,
   user_action
FROM
   lead_logs;
Code language: SQL (Structured Query Language) (sql)
SQLite TRIGGER After Update Trigger Example
You can develop the AFTER INSERT and AFTER DELETE triggers to log the data in the lead_logs table as an excercise.

SQLite DROP TRIGGER statement
To drop an existing trigger, you use the DROP TRIGGER statement as follows:

DROP TRIGGER [IF EXISTS] trigger_name;
Code language: SQL (Structured Query Language) (sql)
In this syntax:

First, specify the name of the trigger that you want to drop after the DROP TRIGGER keywords.
Second, use the IF EXISTS option to delete the trigger only if it exists.
Note that if you drop a table, SQLite will automatically drop all triggers associated with the table.

For example, to remove the validate_email_before_insert_leads trigger, you use the following statement:

DROP TRIGGER validate_email_before_insert_leads;
Code language: SQL (Structured Query Language) (sql)
In this tutorial, we have introduced you to SQLite triggers and show you how to create and drop triggers from the database.
"""

"""What are INSTEAD OF triggers in SQLite
In SQLite, an INSTEAD OF trigger can be only created based on a view, not a table.

Views are read-only in SQLite. And if you issue a DML statement such as INSERT, UPDATE, or DELETE against a view, you will receive an error.

When a view has an INSTEAD OF trigger, the trigger will fire when you issue a corresponding DML statement. This allows you to inject your own logic in the processing flow.

For example, if a view has an INSTEAD OF INSERT trigger, when you issue an INSERT statement, the trigger will fire automatically. Inside the trigger, you can perform insert, update, or delete data in the base tables.

In other words, the INSTEAD OF triggers allow views to become modifiable.

The following illustrates the syntax of creating an INSTEAD OF trigger in SQLite:

CREATE TRIGGER [IF NOT EXISTS] schema_ame.trigger_name
    INSTEAD OF [DELETE | INSERT | UPDATE OF column_name]
    ON table_name
BEGIN
    -- insert code here
END;
Code language: SQL (Structured Query Language) (sql)
In this syntax:

First, specify the name of the trigger after the CREATE TRIGGER keywords. Use IF NOT EXISTS if you want to create the trigger if it exists only.
Second, use the INSTEAD OF keywords followed by a triggering event such as INSERT, UPDATE, or DELETE.
Third, specify the name of the view to which the trigger belongs.
Finally, specify the code that executes the logic.
SQLite INSTEAD OF trigger example
For the demonstration, we will use the Artists and Albums tables from the sample database.


First, create a view named AlbumArtists based on data from the Artists and Albums tables:

CREATE VIEW AlbumArtists(
    AlbumTitle,
    ArtistName
) AS
SELECT
    Title,
    Name
FROM
    Albums
INNER JOIN Artists USING (ArtistId);
Code language: SQL (Structured Query Language) (sql)
Second, use this query to verify data from the view:

SELECT * FROM AlbumArtists;
Code language: SQL (Structured Query Language) (sql)
Third, insert a new row into the AlbumArtists view:

INSERT INTO AlbumArtists(AlbumTitle,ArtistName)
VALUES('Who Do You Trust?','Papa Roach');
Code language: SQL (Structured Query Language) (sql)
SQLite issued the following error:

[SQLITE_ERROR] SQL error or missing database (cannot modify AlbumArtists because it is a view)
Code language: SQL (Structured Query Language) (sql)
Fourth, create an INSTEAD OF trigger that fires when a new row is inserted into the AlbumArtists table:

CREATE TRIGGER insert_artist_album_trg
    INSTEAD OF INSERT ON AlbumArtists
BEGIN
    -- insert the new artist first
    INSERT INTO Artists(Name)
    VALUES(NEW.ArtistName);

    -- use the artist id to insert a new album
    INSERT INTO Albums(Title, ArtistId)
    VALUES(NEW.AlbumTitle, last_insert_rowid());
END;
Code language: SQL (Structured Query Language) (sql)
In this trigger:

First, insert a new row into the Artists table. SQLite automatically generates an integer for the ArtistId column.
Second, use the last_insert_rowid() to get the generated value from the ArtistId column and insert a new row into the Albums table.
Finally, verify insert from the Artists and Albums tables:

SELECT
  *
FROM
    Artists
ORDER BY
    ArtistId DESC;

SELECT
*
FROM
    Albums
ORDER BY
    AlbumId DESC;
Code language: SQL (Structured Query Language) (sql)
SQLite INSTEAD OF Trigger - Artists Table

As you can see the output, a new row has been inserted into the Artists and Albums tables.

In this tutorial, you have learned about the SQLite INSTEAD OF triggers and how to create an INSTEAD OF INSERT trigger to insert data into base tables through a view.
"""
