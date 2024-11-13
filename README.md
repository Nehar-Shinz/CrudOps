# User CRUD Service

A simple Python CRUD service using SQLite to manage user data. This service supports creating, reading, updating, and deleting user records in a local SQLite database.

## User Model

The `User` model has the following fields:
- `username` (string): Unique identifier for the user
- `password` (string): User password
- `active` (boolean): User status (active or inactive)

## Requirements

- Python 3.x
- SQLite3 (built-in with Python)

## Setup

1. Clone the repository or copy the code into a Python file.
2. Run the script to create the `users.db` SQLite database and the `User` table automatically.

## Usage/Functionality

### Create User
```python
create_user("username", "password", active=True)
```

### Read User
```python
read_user("username")
```

### Update User
```python
update_user("username", new_password="new_password", new_active_status=False)
```

### Delete User
```python
delete_user("username")
```

## Closing the Database

Database connection is closed when done:
```python
conn.close()
```

## License Disclaimer
This project is a demo and is open-source and available for personal and educational use.
