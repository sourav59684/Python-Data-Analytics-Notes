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

choice = input("Press Y to enter data into tables : ")
if choice.lower() == 'y':
    curr.execute('show tables')
    data = curr.fetchall()
    for table in data:
        print ("list of tables are : \n" , table[0])

    table_name = input ("enter the name of table to insert data : ")
    tables = [table[0] for table in data]
    if table_name in tables :
        print("table found \n enter the details below : ")
        while True :
            sname = input("enter student name : ")
            semail = input("enter student email : ")
            smobile = input("enter sutdent mobile : ")
            classid = int(input(" enter class id : "))

            curr.execute (f"insert into {table_name} (sname, semail, smobile, classid) values (%s,%s,%s,%s)",
                        (sname, semail, smobile, classid))
            conn.commit()
            choice = input ("press Y to insert more data : ")
            if choice.lower() != 'y':
                break
    else :
        print("table dosen't exist")

conn.commit()

#view data from tables
def view_tables() :
    curr.execute('show tables')
    data = curr.fetchall()
    for table in data:
        print ("list of tables are : \n" , table[0])
    choice = input ("enter the name of table you want to view :")
    tables = [table[0] for table in data]
    if choice in tables :
        print("table found \n Here is the table details : ")
        curr.execute(f'select * from {choice}')
        data = curr.fetchall()
#viewing columns
        curr.execute(f"SHOW COLUMNS FROM {choice}")
        columns = curr.fetchall()
        print()
        for col in columns:
            print(col[0], end=" ")
        print() #to move to next line

        for row in data:
            
            #print (row[0],"\t",row[1],"\t",row[2],"\t",row[3],"\t",row[4])
            print (col[0]," : ",row[0],
                   col[1]," : ",row[1],
                   col[2]," : ",row[2],
                   col[3]," : ",row[3],
                   col[4]," : ",row[4])
    else :
        print ("table not found")

view_tables()






curr.close()
conn.close()