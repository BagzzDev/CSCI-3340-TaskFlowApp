import mysql.connector

# Create data base connection with Django
data_base = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '!Coco1130991229!'
)

# Middleware
cursor_object = data_base.cursor()

cursor_object.execute("CREATE DATABASE taskflow_database")
print("Hello data base TaskFlow")