import sqlite3

DB_NAME = "shop.db"


def connect():
    return sqlite3.connect(DB_NAME)


def create_tables():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            product TEXT,
            price INTEGER,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    conn.commit()
    conn.close()


def add_user(name):
    conn = connect()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()
    print(f"User added: {name}")


def add_order(user_id, product, price):
    conn = connect()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO orders (user_id, product, price) VALUES (?, ?, ?)",
        (user_id, product, price)
    )
    conn.commit()
    conn.close()
    print(f"Order added: user_id={user_id}, {product}, {price}")


def show_users_with_orders():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        SELECT users.name, orders.product, orders.price
        FROM users
        LEFT JOIN orders ON users.id = orders.user_id
    """)
    rows = cur.fetchall()
    conn.close()

    print("\nUSERS WITH ORDERS")
    for row in rows:
        print(row)


def count_orders():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM orders")
    result = cur.fetchone()[0]
    conn.close()
    print("\nTOTAL ORDERS:", result)


def max_price():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT MAX(price) FROM orders")
    result = cur.fetchone()[0]
    conn.close()
    print("MAX PRICE:", result)


def avg_price():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT AVG(price) FROM orders")
    result = cur.fetchone()[0]
    conn.close()
    print("AVG PRICE:", result)


def orders_per_user():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        SELECT users.name, COUNT(orders.id)
        FROM users
        LEFT JOIN orders ON users.id = orders.user_id
        GROUP BY users.id
    """)
    rows = cur.fetchall()
    conn.close()

    print("\nORDERS PER USER")
    for row in rows:
        print(row)


def users_with_expensive_orders(min_price):
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        SELECT name FROM users
        WHERE id IN (
            SELECT user_id FROM orders WHERE price > ?
        )
    """, (min_price,))
    rows = cur.fetchall()
    conn.close()

    print(f"\nUSERS WITH ORDERS > {min_price}")
    for row in rows:
        print(row)


def create_view():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        CREATE VIEW IF NOT EXISTS user_orders AS
        SELECT users.name, orders.product, orders.price
        FROM users
        JOIN orders ON users.id = orders.user_id
    """)
    conn.commit()
    conn.close()
    print("\nVIEW CREATED")


def read_view():
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM user_orders")
    rows = cur.fetchall()
    conn.close()

    print("\nVIEW DATA")
    for row in rows:
        print(row)


create_tables()

add_user("Alice")
add_user("Bob")

add_order(1, "Laptop", 1200)
add_order(1, "Mouse", 50)
add_order(2, "Keyboard", 100)

show_users_with_orders()
count_orders()
max_price()
avg_price()
orders_per_user()
users_with_expensive_orders(500)

create_view()
read_view()