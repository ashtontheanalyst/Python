import sqlite3 as db
import pandas as pd
import os

'''
Information on data from csv's in this use case:
    - The have been stripped of the description data and starting bal line
    - The data types are already cleaned to be correct
    - Similar to what comes out of a cleaned db in my financeApp

Then we are going to append another column with a week ID so it can be referenced later:
weekID will be equal to the earliest date in the statement
'''


# FUNCTIONS

# Connect/Making DB
def checkDB():
    # Checks to see if db exists
    dbExists = os.path.exists(DB_NAME)

    conn = db.connect(DB_NAME)
    c = conn.cursor()

    if not dbExists:
        c.execute("""CREATE TABLE statements (
        Date BLOB,
        Description TEXT,
        Amount REAL,
        Balance REAL,
        weekID INTEGER
        )""")

        c.execute("""CREATE TABLE weekIDs (
        weekID TEXT,
        filename TEXT
        )""")

        print(f"Created new db: {DB_NAME}...\n")
    else:
        print(f"Connection to {DB_NAME} successful.\n")

    conn.commit()
    conn.close()


# Convert the CSV into a df and add the week ID to each record, earliest date in statement
def buildStatementsDF(filepath):
    weekdf = pd.read_csv(filepath)

    # Declare weekID and then append a new column with it on each record
    weekID = weekdf.loc[1, "Date"]
    weekdf['weekID'] = weekID

    # DF is now built out so pass it to the DB
    impStateDFtoDB(weekdf, filepath)
    

# Statements DF to the DB
def impStateDFtoDB(weekdf, filepath):
    conn = db.connect(DB_NAME)

    # Find the weekID, if it already exists then delete and replace
    weekID = weekdf["weekID"].loc[0]
    conn.execute("DELETE FROM statements WHERE weekID=:weekID", {'weekID': weekID})

    # Will add the table to the db only if it doesn't already exist
    weekdf.to_sql("statements", conn, if_exists="append", index=False)

    conn.commit()
    conn.close()

    # Gets the file name from the path and pushes info to weekID table function
    filename = os.path.basename(filepath)
    buildWeekIDTable(weekID, filename)


# WeekID and filename to weekID table
def buildWeekIDTable(weekID, filename):
    conn = db.connect(DB_NAME)
    c = conn.cursor()

    # Delete any prior record of filename so we can replace it
    c.execute("DELETE FROM weekIDs WHERE filename =:filename", {'filename': filename})

    # Insert/Replace the entry
    c.execute("INSERT INTO weekIDs VALUES (:weekID, :filename)", 
              {'weekID': weekID, 'filename': filename})

    conn.commit()
    conn.close()


# Clear the db
def clearDB():
    conn = db.connect(DB_NAME)
    c = conn.cursor()

    c.execute("DELETE FROM statements")

    conn.commit()
    conn.close()



# OUTPUTS FOR CLI

# Output the FULL DB to the terminal
def outputFullDB():
    conn = db.connect(DB_NAME)

    # Prints out all tables in the DB
    print("[--- 1. See Full DB ---]")
    for table in TABLES:
        df = pd.read_sql_query(f"SELECT * FROM {table};", conn)
        print(df)

    conn.close()

# Inpect the columns, data types, amounts, etc.
def columnInfo():
    conn = db.connect(DB_NAME)
    c = conn.cursor()

    c.execute("PRAGMA table_info(statements)")
    rows = c.fetchall()

    print("[--------------------- 2. Inspect Columns and Specifics ---------------------]")
    for row in rows:
        print(f"Column ID:                      {row[0]}")
        print(f"Column Name:                    {row[1]}")
        print(f"Data Type:                      {row[2]}")
        print(f"NOT NULL applied (1), else (0): {row[3]}")
        print(f"Default Value if Any:           {row[0]}")
        print(f"Primary Key (1), else (0):      {row[0]}\n")

    conn.close()



# MAIN BODY

DATA_PATH = './data'
DB_NAME = 'test.db'
TABLES = ["statements", "weekIDs"]

# Check to see if the db is there, if not then make it and the tables
checkDB()

# This takes each file in the data folder, creates a full path, then runs it through the build
files = os.listdir(DATA_PATH)
for file in files:
    path = DATA_PATH + "/" + file
    buildStatementsDF(path)


# CURRENTLY WORKING ON OPTIONS 2 AND 3, OPTION ONE WORKS

# CLI Tool
print("[------------------------ Welcome to the Test DB App ------------------------]\n"
      "OPTIONS:\n" \
      "1. See Full DB\n" \
      "2. See a Specific Table\n" \
      "3. See a Specific Tables Structure/Columns" \
      )

number = int(input("CHOICE: "))


if number == 1:
    outputFullDB()
else:
    print("ERROR: That value is not one of the above options.")
