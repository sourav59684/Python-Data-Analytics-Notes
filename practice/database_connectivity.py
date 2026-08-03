#essential for mysql connectivity
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
def show_db():
    curr.execute("SHOW DATABASES")
    print("""
            ###################################################
            ###             LIST OF DATABASES              ####
            ###################################################
            """)
    for db in curr.fetchall():
        print("➜ ", db[0])
    print("###################################################")

# 2. Create a new database
def create_db():
    newdb = input("Enter the name for new database: ").strip()
    curr.execute("SHOW DATABASES")
    databases = [db[0] for db in curr.fetchall()]
    if newdb in databases:
        print("""
                ###################################################
                ###                   WARNING                  ####
                ###        Database already exists             ####
                ###################################################
                """)
    else:
        curr.execute(f"CREATE DATABASE {newdb}")
        print(f"""
                ###################################################
                ###                   SUCCESS                  ####
                ###      Database created successfully         ####
                ###################################################
                ###      Database Name : {newdb}                ###
                ###################################################
                """)

#3. use database
def use_db():
    show_db()
    db = input("enter the name of database you want to use : ")
    curr.execute("SHOW DATABASES")
    databases = [db[0] for db in curr.fetchall()]
    if db in databases:
        curr.execute(f"use {db}")
        print(f"database selected sucessfully. selected database name : {db}")
    else:
        print("database dosent exist")

# 4. View all tables
def view_tables():
    curr.execute("SHOW TABLES")
    tables = curr.fetchall()

    print("\n===================================================")
    print("                LIST OF TABLES")
    print("===================================================")

    for table in tables:
        print("➜", table[0])

    print("===================================================")

#5. create a table
def create_table():
    pass



#6. insert data into tables
# Insert data into any table
def insert_data():

    # Show tables
    curr.execute("SHOW TABLES")
    tables = [table[0] for table in curr.fetchall()]

    print("\nAvailable Tables:")
    for table in tables:
        print("➜", table)

    table_name = input("\nEnter table name: ").strip()

    if table_name not in tables:
        print("Table does not exist")
        return


    # Get columns of selected table
    curr.execute(f"SHOW COLUMNS FROM {table_name}")
    columns = [col[0] for col in curr.fetchall()]


    print("\nAvailable Columns:")
    for col in columns:
        print("➜", col)


    # User selects columns
    selected_columns = input(
        "\nEnter columns to insert (comma separated): "
    ).strip().split(",")


    # Remove extra spaces
    selected_columns = [col.strip() for col in selected_columns]


    # Validate columns
    for col in selected_columns:
        if col not in columns:
            print(f"{col} column does not exist")
            return


    # Take values
    values = []

    for col in selected_columns:
        value = input(f"Enter value for {col}: ").strip()
        values.append(value)


    # Create placeholders
    placeholders = ",".join(["%s"] * len(values))


    # Create SQL query
    query = f"""
    INSERT INTO {table_name}
    ({','.join(selected_columns)})
    VALUES ({placeholders})
    """


    curr.execute(query, values)

    conn.commit()

    print("""
###################################################
###                   SUCCESS                  ####
###             Data inserted successfully     ####
###################################################
""")

#dashboard
print("===============  welcome to automate sql script using python by sourav singh  ===================")
while True:
    print("""
        1. SHOW DATABASES (view all available databases)
        2. CREATE DATABASE (create a new database if it dosen't exists)
        3. USE DATABASE (IMPORTANT :- use the selected database)
        4. VIEW TABLES (view all tables inside the selected database)
        5. CREATE TABLE (create new tables in a database)
        6. INSERT INTO TABLE (insert data into tables)
        7. 
        8. 
        9. 
        0. Exit
        """)
    choice = int(input("choose the option below for query : "))
    print()

    if choice == 0:
            print("\t\t Thank you! For using my script")
            break
    elif choice == 1 :
        print("===============  ====================================================  ===================")
        show_db()
        input("Press ENTER to continue...")
    elif choice == 2 :
        print("===============  ====================================================  ===================")
        create_db()
        input("Press ENTER to continue...")
    elif choice == 3:
        use_db()
        input("Press ENTER to continue...")
    elif choice == 4:
        view_tables()
    elif choice == 5:
        create_table()
    elif choice == 6:
        insert_data()
    else:
        print("Invalid choice, try again.")
#================================================================#

# #creating student table
# curr.execute(
#     'create table if not exists student_info (' \
#     'sid int primary key auto_increment,' \
#     'sname varchar (100) not null,' \
#     'semail varchar (100) unique,' \
#     'smobile varchar (15),' \
#     'classid int'
#     ')'
# )

# curr.execute('show tables')
# data = curr.fetchall()
# for table in data:
#     print ("list of tables are : \n" , table[0])

# choice = input("Press Y to enter data into tables : ")
# if choice.lower() == 'y':
#     curr.execute('show tables')
#     data = curr.fetchall()
#     for table in data:
#         print ("list of tables are : \n" , table[0])

#     table_name = input ("enter the name of table to insert data : ")
#     tables = [table[0] for table in data]
#     if table_name in tables :
#         print("table found \n enter the details below : ")
#         while True :
#             sname = input("enter student name : ")
#             semail = input("enter student email : ")
#             smobile = input("enter sutdent mobile : ")
#             classid = int(input(" enter class id : "))

#             curr.execute (f"insert into {table_name} (sname, semail, smobile, classid) values (%s,%s,%s,%s)",
#                         (sname, semail, smobile, classid))
#             conn.commit()
#             choice = input ("press Y to insert more data : ")
#             if choice.lower() != 'y':
#                 break
#     else :
#         print("table dosen't exist")

# conn.commit()

# #view data from tables
# def view_tables() :
#     curr.execute('show tables')
#     data = curr.fetchall()
#     for table in data:
#         print ("list of tables are : \n" , table[0])
#     choice = input ("enter the name of table you want to view :")
#     tables = [table[0] for table in data]
#     if choice in tables :
#         print("table found \n Here is the table details : ")
#         curr.execute(f'select * from {choice}')
#         data = curr.fetchall()
# #viewing columns
#         curr.execute(f"SHOW COLUMNS FROM {choice}")
#         columns = curr.fetchall()
#         print()
#         for col in columns:
#             print(col[0], end=" ")
#         print() #to move to next line

#         for row in data:
            
#             #print (row[0],"\t",row[1],"\t",row[2],"\t",row[3],"\t",row[4])
#             print (col[0]," : ",row[0],
#                    col[1]," : ",row[1],
#                    col[2]," : ",row[2],
#                    col[3]," : ",row[3],
#                    col[4]," : ",row[4])
#     else :
#         print ("table not found")

# view_tables()






curr.close()
conn.close()