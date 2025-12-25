import sqlite3

conn = sqlite3.connect("products.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    name TEXT,
    price INTEGER,
    quantity INTEGER
)
""")
conn.commit()


def create_product(name, price, quantity):
    cursor.execute(
        "INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)",
        (name, price, quantity)
    )
    conn.commit()


def get_all_products():
    cursor.execute("SELECT rowid, * FROM products")
    return cursor.fetchall()


def get_product_by_rowid(row_id):
    cursor.execute("SELECT rowid, * FROM products WHERE rowid = ?", (row_id,))
    return cursor.fetchone()


def update_product(row_id, name, price, quantity):
    cursor.execute(
        "UPDATE products SET name = ?, price = ?, quantity = ? WHERE rowid = ?",
        (name, price, quantity, row_id)
    )
    conn.commit()


def delete_product(row_id):
    cursor.execute("DELETE FROM products WHERE rowid = ?", (row_id,))
    conn.commit()


create_product("Apple", 100, 10)
create_product("Banana", 50, 20)

print(get_all_products())

print(get_product_by_rowid(1))

update_product(1, "Green Apple", 120, 15)
print(get_all_products())

delete_product(2)
print(get_all_products())

conn.close()