# import mysql.connector

# conn = mysql.connector.connect(
#     host='127.0.0.1',
#     port='3306',
#     user='root',
#     password='root'
# )

# # Using buffered=True prevents unread result conflicts between queries
# curr = conn.cursor(buffered=True)

# #================================================================#

# # 1. Show existing databases
# curr.execute('SHOW DATABASES')
# print("All databases before creation:")
# for db in curr.fetchall():
#     print(db[0])

# print("=========================================================")

# # 2. Create the new database
# curr.execute('CREATE DATABASE IF NOT EXISTS python_practice')
# print("Database 'python_practice' created successfully!")

# print("=========================================================")

# # 3. Show all databases again to confirm
# curr.execute('SHOW DATABASES')
# print("All databases after creation:")
# for db in curr.fetchall():
#     print(db[0])

# #================================================================#

# curr.execute('use python_practice')
# curr.execute('show tables')
# curr.close()
# conn.close()

x = [1, 2, 3]
x += [4]
print(x)