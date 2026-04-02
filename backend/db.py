import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="mysql.connector",
        user="root",
        password="root",
        database="cdr_db"
    )
