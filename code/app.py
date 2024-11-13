import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create a User table if it doesn't already exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS User (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    active BOOLEAN NOT NULL
)
''')
conn.commit()

# Function to display the current state of the User table
def display_users():
    cursor.execute('SELECT * FROM User')
    users = cursor.fetchall()
    print("\nCurrent Users in Database:")
    if users:
        for user in users:
            print(user)
    else:
        print("No users found.")
    print("-" * 40)

# CRUD Functions
# 1. Create User
def create_user(username, password, active=True):
    try:
        cursor.execute('INSERT INTO User (username, password, active) VALUES (?, ?, ?)', (username, password, active))
        conn.commit()
        print(f"User '{username}' created successfully.")
    except sqlite3.IntegrityError:
        print("Error: Username already exists.")

# 2. Read User
def read_user(username):
    cursor.execute('SELECT * FROM User WHERE username = ?', (username,))
    user = cursor.fetchone()
    if user:
        print(f"User Found: {user}")
    else:
        print(f"User '{username}' not found.")

# 3. Update User
def update_user(username, new_password=None, new_active_status=None):
    if new_password:
        cursor.execute('UPDATE User SET password = ? WHERE username = ?', (new_password, username))
    if new_active_status is not None:
        cursor.execute('UPDATE User SET active = ? WHERE username = ?', (new_active_status, username))
    conn.commit()
    print(f"User '{username}' updated successfully.")

# 4. Delete User
def delete_user(username):
    cursor.execute('DELETE FROM User WHERE username = ?', (username,))
    conn.commit()
    print(f"User '{username}' deleted successfully.")

# Main Program Loop
while True:
    display_users()
    print("\nChoose an operation:")
    print("1. Create User")
    print("2. Read User")
    print("3. Update User")
    print("4. Delete User")
    print("5. Quit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        active = input("Is the user active? (yes/no): ").strip().lower() == "yes"
        create_user(username, password, active)
    
    elif choice == "2":
        username = input("Enter username to read: ")
        read_user(username)

    elif choice == "3":
        username = input("Enter username to update: ")
        new_password = input("Enter new password (leave blank to skip): ")
        new_active_status = input("Is the user active? (yes/no, leave blank to skip): ").strip().lower()
        active_status = None if new_active_status == "" else new_active_status == "yes"
        update_user(username, new_password if new_password else None, active_status)

    elif choice == "4":
        username = input("Enter username to delete: ")
        delete_user(username)

    elif choice == "5":
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please try again.")

# Closing the connection after operations are done
conn.close()
