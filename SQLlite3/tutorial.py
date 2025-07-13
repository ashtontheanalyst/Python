# SQLite3 is a standard library in Python so no need to download or pip
import sqlite3

# Importing our employee class
from employees import Employee


# Create the db, if already created then connect to it
conn = sqlite3.connect('employee.db')

# A cursor allows us to perform operations on the db once connected
c = conn.cursor()


'''
There are 5 data types in SQLite3:
NULL - This is a null value
INTEGER - a signed integer value, stored in 1,2,3,4,5,6, or 8 bytes
REAL - A floating point value, stored in 8 bytes
TEXT - A text string, stored using db encoding UTF-8 16BE or 16LE
BLOB - A blob of data, stored exacly as it is in the input
'''

# Create the table, the 1st column titled "first" for name is in text data
# 2nd column labeled "last" for name is text, etc.
# This only needs to be done ONCE
'''
c.execute("""CREATE TABLE employees (
        first text,
        last text,
        pay integer
        )""")
'''


# This inserted a record into the DB following our table values
'''
c.execute("INSERT INTO employees VALUES ('John', 'Doe', 75000)")
c.execute("INSERT INTO employees VALUES ('Quilian', 'Doe', 49350)")
'''

# Checking to see if it did input the record
c.execute("SELECT * FROM employees WHERE last='Doe'")

# c.fetchone() fetches the first instance
# c.fetchmany(#) fetches a specific amount of records matching
# c.fetchall() fetches all matching records
print(c.fetchall())


# Notice how this will return none since we don't have a record with Smith yet
c.execute("SELECT * FROM employees WHERE last='Jane'")
print(c.fetchone())

# Adding another user
'''
c.execute("INSERT INTO employees VALUES ('Mary', 'Jane', 35000)")
'''


# Creating an employee based off our class
emp1 = Employee('Dawn', 'Farquad', 43521)
emp2 = Employee('Kate', 'Spaid', 132500)

# Accessing our class attributes
print(emp1.first)
print(emp1.last)
print(emp1.pay)
# Functions
print(emp1.email)
print(emp1.fullname)

'''
# Inserting an employee into the db using SQL correct formatting
c.execute("INSERT INTO employees VALUES (:first, :last, :pay)",
          {'first': emp1.first, 'last': emp1.last, 'pay': emp1.pay})

# This is another way of doing it too, not as verbose
c.execute("INSERT INTO employees VALUES (?, ?, ?)",
          (emp2.first, emp2.last, emp2.pay))
'''


# Specific querying using that formatting
c.execute("SELECT * FROM employees WHERE last=?", ('Doe',))
print(c.fetchall())

# The other way with the dictionary style
c.execute("SELECT * FROM employees WHERE last=:last", {'last': 'Doe'})
print(c.fetchall())


# Seeing all records in the table
c.execute("SELECT * FROM employees")
print(c.fetchall())


# Delete all records from the table
# c.execute("DELETE FROM employees")

# Commits the transaction to the db, like github
conn.commit()

# Once done, close the connection, good practice
conn.close()