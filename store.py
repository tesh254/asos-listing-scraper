import sqlite3


class Store:
    def __init__(self):
        self.conn = sqlite3.connect("data.db")

    def initialize_database(self):
        curr = self.conn.cursor()

        curr.execute(
            "CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, title TEXT, price TEXT, description TEXT, images TEXT)"
        )

        self.conn.commit()

    def save_to_db(self, product_data):
        curr = self.conn.cursor()

        images_str = ""

        for image in product_data["images"]:
            images_str += image + ","
        
        product_data["images"] = images_str

        curr.execute(
            "INSERT INTO products (title, price, description, images) VALUES (?, ?, ?, ?)",
            (product_data["title"], product_data["price"], product_data["description"], product_data["images"])
        )

        self.conn.commit()

        self.conn.close()

    def read_data_from_db(self):
        curr = self.conn.cursor()

        curr.execute("SELECT * FROM products")

        rows = curr.fetchall()

        products = []

        for row in rows:
            print(row)

        self.conn.close()
