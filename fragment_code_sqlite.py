import json
import os
import sqlite3


os.system("CLS")


def write(pathlike: str, data):
    with open(pathlike, "w", encoding="UTF-8") as fd:
        json.dump(data, fd, ensure_ascii=False, indent=4)
        fd.close()


def read(pathlike: str):
    data = None
    with open(pathlike, "rb") as fd:
        data = json.load(fd)
        fd.close()
    return data


def main():
    connection = sqlite3.connect("LEARN.sqlite3")
    cursor = connection.cursor()

    #    cursor.executescript("""DROP TABLE IF EXISTS CITIES; CREATE TABLE IF NOT EXISTS CITIES(ID INTEGER PRIMARY KEY, CITYNAME STRING);""")
    #    cursor.execute("DELETE FROM CITIES")
    #    cursor.executemany("""INSERT INTO CITIES(CITYNAME) VALUES (?)""", cities)
    #    connection.commit()

    """
    # Distinct
    # Distinct Values or with unique rows
    cursor.execute("Select CITYNAME from cities;")
    write("out_distinct.json", cursor.fetchall())
    cursor.execute("Select DISTINCT CITYNAME from cities;")
    write("out_distinct_2.json", cursor.fetchall())

    # ORDER BY
    cursor.execute("Select CITYNAME from cities ORDER BY LOWER(CITYNAME) ASC;")
    write("out_order_by_1.json", cursor.fetchall())
    cursor.execute("Select CITYNAME from cities ORDER BY LOWER(CITYNAME) DESC;")
    write("out_order_by_2.json", cursor.fetchall())
    cursor.execute("Select CITYNAME, ID from cities ORDER BY 1 ASC, 2 desc;")
    write("out_order_by_3.json", cursor.fetchall())
    cursor.execute("Select CITYNAME, ID from cities ORDER BY CITYNAME NULLS FIRST;")
    write("out_order_by_3.json", cursor.fetchall())
    cursor.execute("Select CITYNAME, ID from cities ORDER BY CITYNAME NULLS LAST;")
    write("out_order_by_3.json", cursor.fetchall())
    """
    """
    cjson = read("./countries_full.json")
    cursor.execute("DROP TABLE IF EXISTS COUNTRIES")
    cursor.execute("CREATE TABLE IF NOT EXISTS COUNTRIES(ID INTEGER, REGION STRING,COUNTRY STRING,  CAPITAL STRING, COORD_EW FLOAT, COORD_NS FLOAT, PRIMARY KEY(id))")
    cursor.executemany("INSERT INTO COUNTRIES(COUNTRY, REGION, CAPITAL, COORD_EW, COORD_NS) VALUES (?,?,?,?,?)", (cjson))
    # WHERE CLAUSE
    # select statements by conditions
    i = 0
    #
    i += 1
    cursor.execute("Select COUNTRY, REGION, CAPITAL from COUNTRIES;")
    write(f"where_{str(i).zfill(3)}.json", cursor.fetchall())
    i += 1
    cursor.execute("Select COUNTRY, REGION, CAPITAL from COUNTRIES WHERE ID = 50;")
    write(f"where_{str(i).zfill(3)}.json", cursor.fetchall())
    i += 1
    cursor.execute("Select COUNTRY, REGION, CAPITAL from COUNTRIES WHERE ID < 50;")
    write(f"where_{str(i).zfill(3)}.json", cursor.fetchall())
    i += 1
    cursor.execute("Select ID, COUNTRY, REGION, CAPITAL from COUNTRIES WHERE ID <> 50;")
    write(f"where_{str(i).zfill(3)}.json", cursor.fetchall())
    i += 1
    cursor.execute("Select COUNTRY, REGION, CAPITAL from COUNTRIES WHERE ID in (54, 63, 78);")
    write(f"where_{str(i).zfill(3)}.json", cursor.fetchall())
    i += 1
    cursor.execute("Select id, COUNTRY, REGION, CAPITAL from COUNTRIES WHERE ID BETWEEN 54 AND 67;")
    write(f"where_{str(i).zfill(3)}.json", cursor.fetchall())
    i += 1
    cursor.execute("Select id, COUNTRY, REGION, CAPITAL from COUNTRIES WHERE REGION LIKE 'As%';")
    write(f"where_{str(i).zfill(3)}.json", cursor.fetchall())
    i += 1
    cursor.execute("Select id, lower(CAPITAL) from COUNTRIES WHERE EXISTS ( SELECT LOWER(CITYNAME) from cities)")
    write(f"where_{str(i).zfill(3)}.json", cursor.fetchall())
    """

    """
    """
    # LIMIT CLAUSE
    #
    i = 0
    i += 1
    cursor.execute("Select id, lower(CAPITAL) from COUNTRIES limit 10 offset 0")
    write(f"limit_{str(i).zfill(3)}.json", cursor.fetchall())
    i += 1
    cursor.execute("Select id, lower(CAPITAL) from COUNTRIES limit 10 offset 10")
    write(f"limit_{str(i).zfill(3)}.json", cursor.fetchall())

    # like
    """
    Summary: in this tutorial, you will learn how to query data based on pattern matching using SQLite LIKE operator.

    Introduction to SQLite LIKE operator
    Sometimes, you don’t know exactly the complete keyword that you want to query. For example, you may know that your most favorite song contains the word,elevator but you don’t know exactly the name.

    To query data based on partial information, you use the LIKE operator in the WHERE clause of the SELECT statement as follows:

    SELECT
        column_list
    FROM
        table_name
    WHERE
        column_1 LIKE pattern;
    Code language: SQL (Structured Query Language) (sql)
    Note that you can also use the LIKE operator in the WHERE clause of other statements such as the DELETE and UPDATE.

    SQLite provides two wildcards for constructing patterns. They are percent sign % and underscore _ :

    The percent sign % wildcard matches any sequence of zero or more characters.
    The underscore _ wildcard matches any single character.
    The percent sign % wildcard examples
    The s% pattern that uses the percent sign wildcard ( %) matches any string that starts with s e.g.,son and so.

    The %er pattern matches any string that ends with er like peter, clever, etc.

    And the %per% pattern matches any string that contains per such as percent and peeper.

    The underscore _ wildcard examples
    The h_nt pattern matches hunt, hint, etc. The __pple pattern matches topple, supple, tipple, etc.
    Note that SQLite LIKE operator is case-insensitive. It means "A" LIKE "a" is true.

    However, for Unicode characters that are not in the ASCII ranges, the LIKE operator is case sensitive e.g., "Ä" LIKE "ä" is false.
    """

    # GLOB

    """
    Introduction to the SQLite GLOB operator
The GLOB operator is similar to the LIKE operator. The GLOB operator determines whether a string matches a specific pattern.

Unlike the LIKE operator, the GLOB operator is case sensitive and uses the UNIX wildcards. In addition, the GLOB patterns do not have escape characters.

The following shows the wildcards used with the GLOB  operator:

The asterisk (*) wildcard matches any number of characters.
The question mark (?) wildcard matches exactly one character.
On top of these wildcards, you can use the list wildcard [] to match one character from a list of characters. For example [xyz] match any single x, y, or z character.

The list wildcard also allows a range of characters e.g., [a-z] matches any single lowercase character from a to z. The [a-zA-Z0-9] pattern matches any single alphanumeric character, both lowercase, and uppercase.

Besides, you can use the character ^ at the beginning of the list to match any character except for any character in the list. For example, the [^0-9] pattern matches any single character except a numeric character.

SQLite GLOB examples
The following statement finds tracks whose names start with the string Man. The pattern Man* matches any string that starts with Man.

SELECT
	trackid,
	name
FROM
	tracks
WHERE
	name GLOB 'Man*';
Code language: SQL (Structured Query Language) (sql)
Try It

SQLite GLOB asterisk wildcard example
The following statement gets the tracks whose names end with Man. The pattern *Man matches any string that ends with Man.

SELECT
	trackid,
	name
FROM
	tracks
WHERE
	name GLOB '*Man';
Code language: SQL (Structured Query Language) (sql)
Try It

SQLite GLOB asterisk wildcard ending example
The following query finds the tracks whose names start with any single character (?), followed by the string ere and then any number of character (*).

SELECT
	trackid,
	name
FROM
	tracks
WHERE
	name GLOB '?ere*';
Code language: SQL (Structured Query Language) (sql)
Try It

SQLite GLOB asterisk wildcard containing example
To find the tracks whose names contain numbers, you can use the list wildcard [0-9] as follows:

SELECT
	trackid,
	name
FROM
	tracks
WHERE
	name GLOB '*[1-9]*';
Code language: SQL (Structured Query Language) (sql)
Try It

SQLite GLOB list wildcard example
Or to find the tracks whose name does not contain any number, you place the character ^ at the beginning of the list:

SELECT
	trackid,
	name
FROM
	tracks
WHERE
	name GLOB '*[^1-9]*';
Code language: SQL (Structured Query Language) (sql)
Try It

SQLite GLOB list wildcard characters example
The following statement finds the tracks whose names end with a number.

SELECT
	trackid,
	name
FROM
	tracks
WHERE
	name GLOB '*[1-9]';

    """
    # IS NULL

    """
    Introduction to the SQLite IS NULL operator
NULL is special. It indicates that a piece of information is unknown or not applicable.

For example, some songs may not have the songwriter information because we don’t know who wrote them.

To store these unknown songwriters along with the songs in a database table, we must use NULL.

NULL is not equal to anything even the number zero, an empty string, and so on.

Especially, NULL is not equal to itself. The following expression returns 0:

NULL = NULL
Code language: SQL (Structured Query Language) (sql)
This is because two unknown information cannot be comparable.

Let’s see the following tracks table from the sample database:


The following statement attempts to find tracks whose composers are NULL:

SELECT
    Name,
    Composer
FROM
    tracks
WHERE
    Composer = NULL;
Code language: SQL (Structured Query Language) (sql)
It returns an empty row without issuing any additional message.

This is because the following expression always evaluates to false:

Composer = NULL
Code language: SQL (Structured Query Language) (sql)
It’s not valid to use the NULL this way.

To check if a value is NULL or not, you use the IS NULL operator instead:

{ column | expression } IS NULL;
Code language: SQL (Structured Query Language) (sql)
The IS NULL operator returns 1 if the column or expression evaluates to NULL.

To find all tracks whose composers are unknown, you use the IS NULL operator as shown in the following query:

SELECT
    Name,
    Composer
FROM
    tracks
WHERE
    Composer IS NULL
ORDER BY
    Name;
Code language: SQL (Structured Query Language) (sql)
Here is the partial output:

SQLite IS NULL example
SQLite IS NOT NULL operator
The NOT operator negates the IS NULL operator as follows:

expression | column IS NOT NULL
Code language: SQL (Structured Query Language) (sql)
The IS NOT NULL operator returns 1 if the expression or column is not NULL, and 0 if the expression or column is NULL.

The following example finds tracks whose composers are not NULL:

SELECT
    Name,
    Composer
FROM
    tracks
WHERE
    Composer IS NOT NULL
ORDER BY
    Name;
Code language: SQL (Structured Query Language) (sql)
This picture illustrates the partial output:


In this tutorial, you have learned how to check if values in a column or an expression is NULL or not by using the IS NULL and IS NOT NULL operators.
    """

    i = 0
    i += 1
    cursor.execute("Select datetime('now')")
    write(
        f"datatype_{str(i).zfill(3)}.json",
        cursor.fetchall(),
    )
    i += 1
    cursor.execute("Select datetime('now', 'localtime')")
    write(
        f"datatype_{str(i).zfill(3)}.json",
        cursor.fetchall(),
    )

    cursor.executescript("VACUUM;")
    cursor.fetchall()
    cursor.fetchone()
    cursor.fetchmany(50)

    connection.commit()
    connection.close()


if __name__ == "__main__":
    main()
    """
    countries = read("./countries.json")
    cjson = []
    for x in countries:
        cjson.append((x["name"], x["region"], x["capital"], secrets.choice(range(100, 1000)) / 32,secrets.choice(range(100, 1000)) / 32))
    print(cjson[:5])
    write("./countries_full.json", cjson)
    """
