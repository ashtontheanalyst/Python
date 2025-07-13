# This is similar to tutorial.py but has cleaned up code and functions
import sqlite3
from employees import Employee

# Connect to the db and then cursor for conducting operations on it
conn = sqlite3.connect('employeeClean.db')
c = conn.cursor()


# Creates the table, only needs to be run once
'''
c.execute("""CREATE TABLE employees (
        first text,
        last text,
        pay integer
        )""")
'''


# Simplified from tutorial.py and put into different functions
def insertEmp(emp):
    # This will commit automatically for us and raise an exception or error if there is one
    with conn:
        c.execute("INSERT INTO employees VALUES (:first, :last, :pay)",
                {'first': emp.first, 'last': emp.last, 'pay': emp.pay})
        
def getEmpByName(lastname):
    # This doesn't need to be committed since it's a look up so we don't have to
    # put it inside the context manager like in insertEmp()
    c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
    return c.fetchall()

def updatePay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = :pay
                  WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last':emp.last, 'pay': pay})
        
def removeEmp(emp):
    with conn:
        c.execute("DELETE from employees WHERE first = :first AND last = :last",
                  {'first': emp.first, 'last': emp.last})
        

# Main body of the code
emp1 = Employee('Won', 'Dong', 34500)

# Making sure the db is cleared
removeEmp(emp1)

# Input emp1
insertEmp(emp1)
print(getEmpByName('Dong'))

# Change his pay, give this man a raise!
updatePay(emp1, 42000)
print(getEmpByName('Dong'))

# Delete emp1
removeEmp(emp1)
print(getEmpByName('Dong'))


# Iterating through a list of employees and putting them into the db
emp2 = Employee('Jack', 'Butcher', 26800)
emp3 = Employee('Max', 'Sterling', 68500)
emp4 = Employee('Ger', 'Man', 41300)

employeeList = [emp2, emp3, emp4]

for employee in employeeList:
    insertEmp(employee)
    updatePay(employee, 125000)
    print(getEmpByName(employee.last))

for employee in employeeList:
    removeEmp(employee)

# Once done, close the connection, good practice
conn.close()