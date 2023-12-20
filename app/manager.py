import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from app.database import Database
from app.models import Transaction, Category
from datetime import datetime


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

    def get_transaction_amounts(self):
        self.db.execute_query("SELECT amount FROM transactions")
        amounts = [record[0] for record in self.db.fetch_all()]
        return np.array(amounts)

    def calculate_statistics(self):
        amounts = self.get_transaction_amounts()
        if len(amounts) > 0:
            mean_amount = np.mean(amounts)
            total_amount = np.sum(amounts)
            max_amount = np.max(amounts)
            min_amount = np.min(amounts)
            return mean_amount, total_amount, max_amount, min_amount
        else:
            return None
        
    def calculate_category_total(self, category_id):
        query = """
            SELECT SUM(amount) 
            FROM transactions 
            WHERE category_id=?
        """
        self.db.execute_query(query, (category_id,))
        total_amount = self.db.fetch_one()[0]
        return total_amount if total_amount is not None else 0.0

    def plot_transaction_distribution_per_category(self):
        transactions = self.get_all_transactions()

        if len(transactions) > 0:
            categories = set(transaction[3] for transaction in transactions)
            category_expenses = {category: 0 for category in categories}

            for transaction in transactions:
                category_expenses[transaction[3]] += transaction[2]

            total_expense = sum(category_expenses.values())

            plt.figure(figsize=(10, 8))
            pie_chart = plt.pie(category_expenses.values(), labels=category_expenses.keys(), startangle=140)

            legend_labels = [f"{category} - €{amount}" for category, amount in category_expenses.items()]
            legend_patches = plt.legend(legend_labels, loc="best", bbox_to_anchor=(1, 0.5), fontsize=10)

            plt.title(f'Uitgaven per Categorie\nTotale Uitgave: €{total_expense}')

            plt.subplots_adjust(left=0.0, bottom=0.1, right=0.65)
            plt.show()
        else:
            print("Geen transacties om te plotten.")

    def plot_transaction_distribution_percentages(self):
        transactions = self.get_all_transactions()

        if len(transactions) > 0:
            categories = set(transaction[3] for transaction in transactions)
            category_expenses = {category: 0 for category in categories}

            for transaction in transactions:
                category_expenses[transaction[3]] += transaction[2]

            total_expense = sum(category_expenses.values())

            percentages = [amount / total_expense * 100 for amount in category_expenses.values()]

            plt.figure(figsize=(10, 8))
            pie_chart = plt.pie(percentages, labels=category_expenses.keys(), startangle=140)

            legend_labels = [f"{category} - {percentage:.1f}%" for category, percentage in zip(category_expenses.keys(), percentages)]
            legend_patches = plt.legend(legend_labels, loc="best", bbox_to_anchor=(1, 0.5), fontsize=10)

            plt.title('Uitgaven per Categorie')

            plt.subplots_adjust(left=0.0, bottom=0.1, right=0.65)
            plt.show()
        else:
            print("Geen transacties om te plotten.")
                
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
        df = pd.DataFrame(transactions, columns=["ID", "Description", "Amount", "Category"])
        df.to_csv(filename + '.csv', index=False, sep=',')

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

    def close_current_month(self):
        confirmation = input("Wil je de huidige maand afsluiten? (ja/nee): ").lower()

        if confirmation == 'ja':
            today = datetime.now()
            first_day_of_month = today.replace(day=1)

            filename = f"afsluiting_{today.strftime('%Y-%m')}"
            self.export_transactions_to_csv(filename) 

            self.zero_out_current_month_transactions() 
            print(f"Huidige maand is afgesloten. Gegevens zijn geëxporteerd naar {filename}.csv.")
        else:
            print("Afsluiten geannuleerd.")

    def zero_out_current_month_transactions(self):
        query = '''
            DELETE FROM transactions
        '''
        self.db.execute_query(query)

    def delete_all_transactions(self):
        query = "DELETE FROM transactions"
        self.db.execute_query(query)

    def delete_all_categories(self):
        query = "DELETE FROM categories"
        self.db.execute_query(query)




        