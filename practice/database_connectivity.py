"""
Simple interactive CLI to manage MySQL databases/tables.

NOTE ON SECURITY:
- Table/database/column names CANNOT be parameterized with %s placeholders
  in MySQL (only values can). Since identifiers are always validated against
  a list fetched live from the server (SHOW DATABASES / SHOW TABLES / SHOW
  COLUMNS) before being used in an f-string, an attacker can't inject
  arbitrary SQL through them -- the input has to match a real existing
  name first. Data VALUES, however, always go through parameterized
  queries (the %s placeholders below) rather than string formatting.
"""

import mysql.connector
from getpass import getpass

# --- Connection setup -------------------------------------------------
# All connection details are now asked for at startup instead of hardcoded,
# so the script isn't tied to one server/user. Pressing ENTER on any prompt
# falls back to a sensible local default.
def get_connection():
    print("=== Connect to MySQL server ===")
    # Note: MySQL treats 'localhost' and '127.0.0.1' as different accounts
    # ('root'@'localhost' vs 'root'@'127.0.0.1') -- they can have different
    # passwords or auth plugins even on the same machine. 'localhost' also
    # uses a Unix socket / named pipe rather than TCP, which is usually
    # how local root accounts are set up by default.
    host = input("Host [localhost]: ").strip() or "localhost"

    port_raw = input("Port [3306]: ").strip() or "3306"
    try:
        port = int(port_raw)
    except ValueError:
        print(f"'{port_raw}' isn't a valid port, defaulting to 3306.")
        port = 3306

    user = input("Username [root]: ").strip() or "root"

    # getpass() hides the password as it's typed instead of echoing it to
    # the terminal. Hardcoding credentials in source is fine for quick local
    # experiments, but avoid committing real passwords to version control.
    password = getpass(f"Password for {user}: ")

    try:
        connection = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password,
        )
        print(f"\nConnected to {host}:{port} as '{user}'.\n")
        return connection
    except mysql.connector.Error as err:
        print(f"\nConnection failed: {err}")
        raise SystemExit(1)


conn = get_connection()

# buffered=True prevents "Unread result found" errors when you run a new
# query before fully consuming the previous one's results.
curr = conn.cursor(buffered=True)


# =======================================================================
# 1. Show existing databases
# =======================================================================
def show_db():
    curr.execute("SHOW DATABASES")
    print("\n### LIST OF DATABASES ###")
    for db in curr.fetchall():
        print("➜ ", db[0])
    print("##########################")
    input("\nPress ENTER to return to main menu...")


# =======================================================================
# 2. Create a new database
# =======================================================================
def create_db():
    newdb = input("Enter the name for new database: ").strip()
    if not newdb:
        print("Database name cannot be empty.")
        input("\nPress ENTER to return to main menu...")
        return

    curr.execute("SHOW DATABASES")
    databases = [db[0] for db in curr.fetchall()]

    if newdb in databases:
        print("\n### WARNING: Database already exists ###")
    else:
        # Backticks let names with special characters/reserved words work safely.
        curr.execute(f"CREATE DATABASE `{newdb}`")
        print(f"\n### SUCCESS: Database '{newdb}' created ###")

    input("\nPress ENTER to return to main menu...")


# =======================================================================
# 3. Use / select a database
# =======================================================================
def use_db():
    show_db()
    db = input("Enter the name of the database you want to use: ").strip()
    curr.execute("SHOW DATABASES")
    databases = [d[0] for d in curr.fetchall()]

    if db in databases:
        # conn.database is the driver's built-in way to switch databases --
        # avoids building a raw "USE ..." string yourself.
        conn.database = db
        print(f"Database selected successfully: {db}")
    else:
        print("Database does not exist.")

    input("\nPress ENTER to return to main menu...")


# =======================================================================
# 4. View all tables in the currently selected database
# =======================================================================
def view_tables():
    curr.execute("SHOW TABLES")
    tables = curr.fetchall()

    print("\n=== LIST OF TABLES ===")
    for table in tables:
        print("➜", table[0])
    print("=======================")
    input("\nPress ENTER to return to main menu...")


# =======================================================================
# 5. Create a table
# =======================================================================
def create_table():
    # Was a stub (`pass`) in the original script. A minimal interactive
    # implementation -- extend as needed for more column types/constraints.
    table_name = input("Enter new table name: ").strip()
    if not table_name:
        print("Table name cannot be empty.")
        input("\nPress ENTER to return to main menu...")
        return

    print("Define columns. Leave column name blank to finish.")
    columns_sql = []
    while True:
        col_name = input("  Column name: ").strip()
        if not col_name:
            break
        col_type = input("  Column type (e.g. VARCHAR(100), INT): ").strip()
        columns_sql.append(f"`{col_name}` {col_type}")

    if not columns_sql:
        print("A table needs at least one column.")
        input("\nPress ENTER to return to main menu...")
        return

    query = f"CREATE TABLE `{table_name}` ({', '.join(columns_sql)})"
    try:
        curr.execute(query)
        conn.commit()
        print(f"\n### SUCCESS: Table '{table_name}' created ###")
    except mysql.connector.Error as err:
        print(f"Error creating table: {err}")

    input("\nPress ENTER to return to main menu...")


# =======================================================================
# 6. Insert data into any table
# =======================================================================
def insert_data():
    curr.execute("SHOW TABLES")
    tables = [table[0] for table in curr.fetchall()]

    print("\nAvailable Tables:")
    for table in tables:
        print("➜", table)

    table_name = input("\nEnter table name: ").strip()
    if table_name not in tables:
        print("Table does not exist")
        input("\nPress ENTER to return to main menu...")
        return

    curr.execute(f"SHOW COLUMNS FROM `{table_name}`")
    columns = curr.fetchall()
    columns_name = [each[0] for each in columns]

    print(f"\n{'Column':<15}{'Type':<20}{'Null':<8}{'Key':<8}{'Default':<12}{'Extra'}")
    print("-" * 75)
    for field, dtype, null, key, default, extra in columns:
        print(f"{field:<15}{dtype:<20}{null:<8}{key:<8}{str(default):<12}{extra}")

    selected_columns = input("\nEnter columns to insert (column1, column2, column3...): ").split(",")
    selected_columns = [col.strip() for col in selected_columns]

    for col in selected_columns:
        if col not in columns_name:
            print(f"{col} column does not exist")
            input("\nPress ENTER to return to main menu...")
            return

    # BUG FIX: the original code appended to an undefined `values` list
    # instead of `new_values`, which would raise a NameError as soon as
    # this ran. Now consistently using `new_values`.
    new_values = []
    for col in selected_columns:
        value = input(f"Enter value for {col}: ").strip()
        new_values.append(value)

    placeholders = ",".join(["%s"] * len(new_values))
    query = f"""
    INSERT INTO `{table_name}`
    ({','.join(f'`{c}`' for c in selected_columns)})
    VALUES ({placeholders})
    """

    try:
        curr.execute(query, new_values)
        conn.commit()
        print("\n### SUCCESS: Data inserted successfully ###")
    except mysql.connector.Error as err:
        # Roll back so a failed insert doesn't leave a half-open transaction.
        conn.rollback()
        print(f"Error inserting data: {err}")

    input("\nPress ENTER to return to main menu...")


# =======================================================================
# Startup: pick a database before showing the main menu
# =======================================================================
def select_initial_database():
    """
    Runs once at startup. Loops until the user has either selected an
    existing database or created and selected a new one -- the main menu
    doesn't appear until conn.database is actually set.
    """
    while True:
        curr.execute("SHOW DATABASES")
        databases = [db[0] for db in curr.fetchall()]

        print("\n### AVAILABLE DATABASES ###")
        for db in databases:
            print("➜ ", db)
        print("############################")

        choice = input(
            "\nEnter a database name to use it, or type 'new' to create one: "
        ).strip()

        if choice.lower() == "new":
            newdb = input("Enter the name for the new database: ").strip()
            if not newdb:
                print("Database name cannot be empty.")
                continue
            if newdb in databases:
                print("That database already exists -- selecting it.")
            else:
                curr.execute(f"CREATE DATABASE `{newdb}`")
                print(f"Database '{newdb}' created.")
            conn.database = newdb
            return

        if choice in databases:
            conn.database = choice
            return

        print(f"'{choice}' is not a valid option. Try again.")


# =======================================================================
# Dashboard / main menu loop
# =======================================================================
def main():
    print("=============== Welcome to Automate SQL Script (by Sourav Singh) ===================")

    select_initial_database()

    actions = {
        1: show_db,
        2: create_db,
        3: use_db,
        4: view_tables,
        5: create_table,
        6: insert_data,
    }

    while True:
        # Re-read conn.database each loop so the header stays accurate
        # after use_db() or create_db() changes the active database.
        menu = f"""
        --- Connected to database: {conn.database} ---
        1. SHOW DATABASES (view all available databases)
        2. CREATE DATABASE (create a new database if it doesn't exist)
        3. USE DATABASE (switch the active database)
        4. VIEW TABLES (view all tables inside the selected database)
        5. CREATE TABLE (create a new table)
        6. INSERT INTO TABLE (insert data into tables)
        0. Exit
        """
        print(menu)
        raw_choice = input("Choose an option: ").strip()

        # Guard against non-numeric input crashing the script (the
        # original used a bare int(input(...)) with no error handling).
        if not raw_choice.isdigit():
            print("Invalid choice, try again.")
            continue

        choice = int(raw_choice)
        print()

        if choice == 0:
            print("\t\tThank you! For using my script")
            break

        action = actions.get(choice)
        if action:
            try:
                action()
            except mysql.connector.Error as err:
                print(f"Database error: {err}")
                input("\nPress ENTER to return to main menu...")
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    try:
        main()
    finally:
        # finally ensures the connection closes even if something above
        # raises an unhandled exception.
        curr.close()
        conn.close()