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

        print(f"Created new db: {DB_NAME}...")
    else:
        print(f"Connected to {DB_NAME}!")

    conn.commit()
    conn.close()


# Convert the CSV into a df and add the week ID to each record, earliest date in statement
def buildDF(filepath):
    weekdf = pd.read_csv(filepath)

    # Declare weekID and then append a new column with it on each record
    weekID = weekdf.loc[1, "Date"]
    weekdf['weekID'] = weekID

    # DF is now built out so pass it to the DB
    importDFtoDB(weekdf)
    

# DF into the DB
def importDFtoDB(weekdf):
    conn = db.connect(DB_NAME)

    # Find the weekID, if it already exists then delete and replace
    weekID = weekdf["weekID"].loc[0]
    conn.execute("DELETE FROM statements WHERE weekID=:weekID", {'weekID': weekID})

    # Will add the table to the db only if it doesn't already exist
    weekdf.to_sql("statements", conn, if_exists="append", index=False)

    conn.commit()
    conn.close()


# Clear the db
def clearDB():
    conn = db.connect(DB_NAME)
    c = conn.cursor()

    c.execute("DATA FROM statements")

    conn.commit()
    conn.close()


# MAINLY FOR TESTING, See what's going on inside the db
def dbInfo():
    # Connect to the db
    conn = db.connect(DB_NAME)

    # Prints out the full data base, all records and columns
    print("DATABASE INFORMATION:")
    df = pd.read_sql_query("SELECT * FROM statements;", conn)
    print(df)

    conn.close()



# MAIN BODY

DATA_PATH = './data'
DB_NAME = 'test.db'

# Check to see if the db is there, if not then back it and the table
checkDB()

# This takes each file in the data folder, creates a full path, then runs it through the build
files = os.listdir(DATA_PATH)
for file in files:
    path = DATA_PATH + "/" + file
    buildDF(path)

# FOR TESTING, SEE ABOVE
dbInfo()