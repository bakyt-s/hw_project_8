import sqlite3


def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
    except sqlite3.Error as err:
        print(err)
    return connection


def create_table(est_conn, sql):
    try:
        cursor = est_conn.cursor()
        cursor.execute(sql)
    except sqlite3.Error as err:
        print(err)


def insert_product(est_conn, product):
    try:
        sql = '''INSERT INTO products 
        (product_title, price, quantity) 
        VALUES (?, ?, ?)'''
        cursor = est_conn.cursor()
        cursor.execute(sql, product)
        est_conn.commit()
    except sqlite3.Error as err:
        print(err)


def update_product_by_quantity(est_conn, product):
    try:
        sql = '''UPDATE products SET quantity = ?
        WHERE id = ?'''
        cursor = est_conn.cursor()
        cursor.execute(sql, product)
        est_conn.commit()
    except sqlite3.Error as err:
        print(err)


def update_product_by_price(est_conn, product):
    try:
        sql = '''UPDATE products SET price = ?
        WHERE id = ?'''
        cursor = est_conn.cursor()
        cursor.execute(sql, product)
        est_conn.commit()
    except sqlite3.Error as err:
        print(err)


def delete_product(est_conn, id):
    try:
        sql = '''DELETE FROM products WHERE id = ?'''
        cursor = est_conn.cursor()
        cursor.execute(sql, (id,))
        est_conn.commit()
    except sqlite3.Error as err:
        print(err)


def select_all_products(est_conn):
    try:
        sql = '''SELECT * FROM products'''
        cursor = est_conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except sqlite3.Error as err:
        print(err)


def select_products_by_criteria(est_conn, criteria):
    try:
        sql = '''SELECT * FROM products WHERE price < ? AND quantity > ?'''
        cursor = est_conn.cursor()
        cursor.execute(sql, criteria)
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except sqlite3.Error as err:
        print(err)


def select_products_by_title(est_conn, title):
    try:
        sql = '''SELECT * FROM products
        WHERE product_title LIKE ?'''
        cursor = est_conn.cursor()
        cursor.execute(sql, ('%' + title + '%',))
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except sqlite3.Error as err:
        print(err)


cr_products_table = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR(200) NOT NULL,
price DOUBLE(10, 2) NOT NULL DEFAULT 0.0,
quantity INTEGER(5) NOT NULL DEFAULT 0
)
'''


est_conn = create_connection('hw.db')
if est_conn is not None:
    print('Successfully connected to the database')
    create_table(est_conn, cr_products_table)
    insert_product(est_conn, ('PlayStation 3', 179.99, 12))
    insert_product(est_conn, ('PlayStation 4 Slim', 311.98, 17))
    insert_product(est_conn,('PlayStation 5 PRO', 559.00, 28))
    insert_product(est_conn, ('PlayStation 3 Games', 35.99, 3))
    insert_product(est_conn, ('PlayStation 4 Games', 64.15, 26))
    insert_product(est_conn, ('PlayStation 5 Games', 89.69, 45))
    insert_product(est_conn, ('Samsung TV 75 inch', 956.34, 20))
    insert_product(est_conn, ('LG TV 60 inch', 727.99, 30))
    insert_product(est_conn, ('MacBook Pro 16 inch', 3499.00, 29))
    insert_product(est_conn, ('MacBook Air 14 inch', 1499.00, 54))
    insert_product(est_conn, ('iMac 24 inch', 1699.00, 41))
    insert_product(est_conn, ('Mac Mini', 1299.00, 12))
    insert_product(est_conn, ('Mac Pro', 6499.00, 3))
    insert_product(est_conn, ('Mac Studio', 3999.00, 19))
    insert_product(est_conn, ('Pro Display XDR', 5999.99, 6))
    update_product_by_quantity(est_conn, (4, 4))
    update_product_by_price(est_conn, (9, 3499.99))
    delete_product(est_conn, 1)
    select_all_products(est_conn)
    select_products_by_criteria(est_conn, (100, 5))
    title = input('\nProduct search. Enter a word: ')
    select_products_by_title(est_conn, title)
    est_conn.close()
    print('DONE!')
