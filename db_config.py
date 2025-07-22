# Importing MySQL connector to interact with the database
import mysql.connector

# Function to create and return a database connection
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",             
        password="232774",
        database="employee"   
    )
