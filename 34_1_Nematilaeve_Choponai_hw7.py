import sqlite3
from pprint import pprint


def create_connection(db_name):
    conn = None
    try:
        conn = sqlite3.connect(db_name)
    except sqlite3.Error as e:
        print(e)
    return conn


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)


def insert_products(conn, products):
    sql = '''INSERT INTO products 
    (product_title,price,quantity)
    VALUES (?, ?, ?)
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, products)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def update_products(conn, product):
    sql = '''UPDATE products SET quantity = ?  WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, product)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def choose_products(conn):
    sql = '''SELECT * FROM products WHERE  price < 100 and quantity > 5 
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        pprint(cursor.fetchall())
    except sqlite3.Error as e:
        print(e)


def search_products(conn, products):
    sql = ''' SELECT  * FROM PRODUCTS WHERE product_title LIKE ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, ("%"+products+"%",))
        pprint(cursor.fetchall())
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def update_products(conn, products):
    sql = '''UPDATE products SET price = ? WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, products)
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def delete_products(conn, id):
    sql = '''DELETE FROM products WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (id,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def select_all_products(conn):
    sql = '''SELECT * FROM products'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql)

        rows_list = cursor.fetchall()
        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)


def select_product_by_price(conn, price):
    sql = '''SELECT * FROM products WHERE price >= ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (price,))

        rows_list = cursor.fetchall()
        for row in rows_list:
            print(row)
    except sqlite3.Error as e:
        print(e)


connection = create_connection('hw.db')
sql_create_products_table = '''
    CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title  VARCHAR(200) NOT NULL,
    price FLOAT(10,2) NOT NULL DEFAULT 0.0,
    quantity INTEGER NOT NULL DEFAULT 0
);'''
# create_table(connection, sql_create_products_table)

if connection is not None:
    print('Successfully connected!')
    # insert_products(connection, ('Bubble Tea', 270.0, 10))
    # insert_products(connection, ('OREO', 120.0, 17))
    # insert_products(connection, ('KITKAT', 70.0, 27))
    # insert_products(connection, ('LAYS CHIPS', 155.0, 9))
    # insert_products(connection, ('FANTA', 72.0, 19))
    # insert_products(connection, ('KURUT', 10.0, 29))
    # insert_products(connection, ('NITRO', 65.0, 8))
    # insert_products(connection, ('SOOP', 120.0, 5))
    # insert_products(connection, ('BACKET', 42.0, 13))
    # insert_products(connection, ('MARSHMELOU', 98.0, 43))
    # insert_products(connection, ('MAXI TEA', 78.0, 21))
    # insert_products(connection, ('MACARON', 120.0, 30))
    # insert_products(connection, ('TOY', 740.0, 3))
    # insert_products(connection, ('TEA', 126.0, 41))
    # insert_products(connection, ('SNIKCERS', 70.0, 10))


    # update_products(connection, (100.0, 3))
    # choose_products(connection)
    # delete_products(connection,2)
    # select_all_products(connection)
    search_products(connection, 'KIT')
    connection.close()
