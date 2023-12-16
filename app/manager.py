import csv

from app.database import Database
from app.models import Transaction, Category

class FinancialManager:
    def __init__(self, db_path):
        self.db = Database(db_path)
        self.create_tables()

    def create_tables(self):
        self.db.execute_query('''
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT
            )
        ''')
        self.db.execute_query('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT,
                amount REAL,
                category_id INTEGER,
                FOREIGN KEY(category_id) REFERENCES categories(id)
            )
        ''')

    def add_transaction(self, transaction):
        query = "INSERT INTO transactions (description, amount, category_id) VALUES (?, ?, ?)"
        self.db.execute_query(query, (transaction.description, transaction.amount, transaction.category_id))

    def get_all_transactions(self):
        self.db.execute_query("""
            SELECT transactions.id, transactions.description, transactions.amount, categories.name 
            FROM transactions 
            INNER JOIN categories ON transactions.category_id = categories.id
        """)
        return self.db.fetch_all()

    def add_category(self, category):
        query = "INSERT INTO categories (name) VALUES (?)"
        self.db.execute_query(query, (category.name,))

    def get_all_categories(self):
        self.db.execute_query("SELECT * FROM categories")
        return self.db.fetch_all()
    
    def export_transactions_to_csv(self, filename):
        transactions = self.get_all_transactions()
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Description", "Amount", "Category"])
            writer.writerows(transactions)