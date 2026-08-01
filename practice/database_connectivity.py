import mysql.connector

conn = mysql.connector.connect(
    host='127.0.0.1',
    port='3306',
    user='root',
    password='root'
)

# Using buffered=True prevents unread result conflicts between queries
curr = conn.cursor(buffered=True)

#================================================================#

# 1. Show existing databases
curr.execute('SHOW DATABASES')
print("All databases before creation:")
for db in curr.fetchall():
    print(db[0])

print("=========================================================")

# 2. Create the new database
curr.execute('CREATE DATABASE IF NOT EXISTS python_practice')
print("Database 'python_practice' created successfully!")

print("=========================================================")

# 3. Show all databases again to confirm
curr.execute('SHOW DATABASES')
print("All databases after creation:")
for db in curr.fetchall():
    print(db[0])

#================================================================#

curr.execute('use python_practice')
#creating student table
curr.execute(
    'create table if not exists student_info (' \
    'sid int primary key auto_increment,' \
    'sname varchar (100) not null,' \
    'semail varchar (100) unique,' \
    'smobile varchar (15),' \
    'classid int'
    ')'
)

curr.execute('show tables')
data = curr.fetchall()
for table in data:
    print ("list of tables are : \n" , table[0])



curr.close()
conn.close()