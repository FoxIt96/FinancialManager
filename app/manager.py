from app.database import Database
from app.models import Transaction, Category

class FinancialManager:
    def __init__(self, db_path):
        self.db = Database(db_path)
        self.create_tables()

    def create_tables(self):
        self.db.execute_query('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT,
                amount REAL
            )
        ''')

    def add_transaction(self, transaction):
        query = "INSERT INTO transactions (description, amount) VALUES (?, ?)"
        self.db.execute_query(query, (transaction.description, transaction.amount))

    def get_all_transactions(self):
        self.db.execute_query("SELECT * FROM transactions")
        return self.db.fetch_all()
