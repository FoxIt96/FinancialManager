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

    def edit_transaction(self, transaction_id, new_description, new_amount, new_category_id):
        query = '''
            UPDATE transactions
            SET description=?, amount=?, category_id=?
            WHERE id=?
        '''
        self.db.execute_query(query, (new_description, new_amount, new_category_id, transaction_id))

    def edit_category(self, category_id, new_name):
        query = "UPDATE categories SET name=? WHERE id=?"
        self.db.execute_query(query, (new_name, category_id))

    def delete_transaction(self, transaction_id):
        query = "DELETE FROM transactions WHERE id=?"
        self.db.execute_query(query, (transaction_id,))

    def delete_category(self, category_id):
        query = "DELETE FROM categories WHERE id=?"
        self.db.execute_query(query, (category_id,))

    def get_transaction_by_id(self, transaction_id):
        query = """
            SELECT transactions.id, transactions.description, transactions.amount, categories.name 
            FROM transactions 
            INNER JOIN categories ON transactions.category_id = categories.id
            WHERE transactions.id=?
        """
        self.db.execute_query(query, (transaction_id,))
        return self.db.fetch_one()

    def get_category_by_id(self, category_id):
        query = "SELECT * FROM categories WHERE id=?"
        self.db.execute_query(query, (category_id,))
        return self.db.fetch_one()
