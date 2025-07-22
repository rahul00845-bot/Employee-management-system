CREATE DATABASE IF NOT EXISTS employee_db;
USE employee_db;

-- Create the employee_data table
CREATE TABLE IF NOT EXISTS employee_data (
    emp_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(15),
    address TEXT,
    post VARCHAR(50),
    salary FLOAT
);
