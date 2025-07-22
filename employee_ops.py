from db_config import get_connection

# Adds a new employee to the database
def add_employee(name, email, phone, address, post, salary):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO employee_data (name, email, phone, address, post, salary) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (name, email, phone, address, post, salary))
    conn.commit()
    conn.close()

# Returns a list of all employees
def get_all_employees():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employee_data")
    result = cursor.fetchall()
    conn.close()
    return result

# Updates the email, phone, and address of an employee
def update_employee(emp_id, email, phone, address):
    conn = get_connection()
    cursor = conn.cursor()
    query = "UPDATE employee_data SET email=%s, phone=%s, address=%s WHERE emp_id=%s"
    cursor.execute(query, (email, phone, address, emp_id))
    conn.commit()
    conn.close()

# Increases the salary of an employee
def promote_employee(emp_id, salary_increase):
    conn = get_connection()
    cursor = conn.cursor()
    query = "UPDATE employee_data SET salary = salary + %s WHERE emp_id = %s"
    cursor.execute(query, (salary_increase, emp_id))
    conn.commit()
    conn.close()

# Deletes an employee from the database
def delete_employee(emp_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM employee_data WHERE emp_id = %s", (emp_id,))
    conn.commit()
    conn.close()

# Searches for an employee by ID
def search_employee(emp_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employee_data WHERE emp_id = %s", (emp_id,))
    result = cursor.fetchone()
    conn.close()
    return result
