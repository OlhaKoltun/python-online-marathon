import sqlite3
from sqlite3 import Error


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connected to SQLite")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
    except Error as e:
        print(f"The error '{e}' occurred")

    return result


def close_connection(connection):
    try:
        connection.close()
        print("The SQLite connection is closed")
    except Error as e:
        print(f"The error '{e}' occurred")


connection = create_connection('q1.db')

select_users = "SELECT * FROM customers WHERE grade > 200 ORDER BY id"
users = execute_read_query(connection, select_users)

print(f'Total rows are:   {len(users)}')
print('Printing each row')

for user in users:
    print(f'Id:  {user[0]}')
    print(f'Name:  {user[1]}')
    print(f'City:  {user[2]}')
    print(f'Grade:  {user[3]}')
    print(f'Seller:  {user[4]}')
    print('\n')

close_connection(connection)
