import tkinter as tk
from tkinter import messagebox, simpledialog
from employee_ops import *

# Add Employee UI
def add_employee_ui():
    def submit():
        add_employee(
            name_entry.get(), email_entry.get(), phone_entry.get(),
            address_entry.get(), post_entry.get(), float(salary_entry.get())
        )
        messagebox.showinfo("Success", "Employee added successfully")
        top.destroy()

    top = tk.Toplevel()
    top.title("Add Employee")

    # Create entry fields and labels
    tk.Label(top, text="Name").grid(row=0, column=0)
    name_entry = tk.Entry(top)
    name_entry.grid(row=0, column=1)

    tk.Label(top, text="Email").grid(row=1, column=0)
    email_entry = tk.Entry(top)
    email_entry.grid(row=1, column=1)

    tk.Label(top, text="Phone").grid(row=2, column=0)
    phone_entry = tk.Entry(top)
    phone_entry.grid(row=2, column=1)

    tk.Label(top, text="Address").grid(row=3, column=0)
    address_entry = tk.Entry(top)
    address_entry.grid(row=3, column=1)

    tk.Label(top, text="Post").grid(row=4, column=0)
    post_entry = tk.Entry(top)
    post_entry.grid(row=4, column=1)

    tk.Label(top, text="Salary").grid(row=5, column=0)
    salary_entry = tk.Entry(top)
    salary_entry.grid(row=5, column=1)

    tk.Button(top, text="Submit", command=submit).grid(row=6, columnspan=2)

# View all employees in a popup
def view_employees_ui():
    employees = get_all_employees()
    top = tk.Toplevel()
    top.title("All Employees")

    for idx, emp in enumerate(employees):
        tk.Label(top, text=str(emp)).grid(row=idx, column=0)

# Update existing employee details
def update_employee_ui():
    emp_id = simpledialog.askinteger("Input", "Enter Employee ID")
    email = simpledialog.askstring("Input", "Enter New Email")
    phone = simpledialog.askstring("Input", "Enter New Phone")
    address = simpledialog.askstring("Input", "Enter New Address")
    update_employee(emp_id, email, phone, address)
    messagebox.showinfo("Success", "Employee updated successfully")

# Promote an employee by increasing salary
def promote_employee_ui():
    emp_id = simpledialog.askinteger("Input", "Enter Employee ID")
    increment = simpledialog.askfloat("Input", "Enter Salary Increase")
    promote_employee(emp_id, increment)
    messagebox.showinfo("Success", "Employee promoted successfully")

# Delete employee by ID
def delete_employee_ui():
    emp_id = simpledialog.askinteger("Input", "Enter Employee ID")
    delete_employee(emp_id)
    messagebox.showinfo("Success", "Employee deleted successfully")

# Search employee by ID
def search_employee_ui():
    emp_id = simpledialog.askinteger("Input", "Enter Employee ID")
    emp = search_employee(emp_id)
    if emp:
        messagebox.showinfo("Employee Found", str(emp))
    else:
        messagebox.showwarning("Not Found", "Employee not found")

# Main root window and buttons
root = tk.Tk()
root.title("Employee Management System")
root.geometry("400x400")
root.configure(bg="#f0f0f0") 

# Buttons for each operation
btns = [
    ("Add Employee", add_employee_ui),
    ("View All Employees", view_employees_ui),
    ("Update Employee", update_employee_ui),
    ("Promote Employee", promote_employee_ui),
    ("Delete Employee", delete_employee_ui),
    ("Search Employee", search_employee_ui),
    ("Exit", root.quit)
]

# Create and place buttons on the screen
for i, (label, cmd) in enumerate(btns):
    tk.Button(root, text=label, command=cmd, width=30, bg="#004c99", fg="white", font=("Arial", 12)).pack(pady=6)

root.mainloop()
