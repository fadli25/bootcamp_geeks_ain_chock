import psycopg2
import bcrypt

connection = psycopg2.connect(
    dbname="auth_db",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
)
connection.autocommit = True

with connection.cursor() as cur:
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

def signup(username, password):
    with connection.cursor() as cur:
        cur.execute("SELECT * FROM users WHERE username = %s", (username,))
        if cur.fetchone():
            return False
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed.decode()))
        return True

def login(username, password):
    with connection.cursor() as cur:
        cur.execute("SELECT password FROM users WHERE username = %s", (username,))
        row = cur.fetchone()
        if row and bcrypt.checkpw(password.encode(), row[0].encode()):
            return True
        return False

def cli():
    logged_in = None
    while True:
        action = input("Enter login / signup / exit: ").lower()
        if action == "exit":
            break
        elif action == "login":
            username = input("Username: ")
            password = input("Password: ")
            if login(username, password):
                logged_in = username
                print("You are now logged in")
            else:
                print("Invalid username or password")
        elif action == "signup":
            while True:
                username = input("Choose a username: ")
                with connection.cursor() as cur:
                    cur.execute("SELECT * FROM users WHERE username = %s", (username,))
                    if cur.fetchone():
                        print("Username already exists, try again")
                    else:
                        break
            password = input("Choose a password: ")
            if signup(username, password):
                print("Signup successful, you can now login")
            else:
                print("Error signing up")
        else:
            print("Unknown command")

if __name__ == "__main__":
    cli()
