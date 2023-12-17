class DeleteMenu:
    def __init__(self, manager):
        self.manager = manager

    def run(self):
        print("\n--- Verwijderen ---")
        print("1. Verwijder een transactie")
        print("2. Verwijder een categorie")
        print("3. Verwijder alle transacties")
        print("4. Verwijder alle categorieën")
        sub_choice = input("\nMaak een keuze: ").lower()

        if sub_choice == "1" and self.manager.get_all_transactions():
            self.delete_transaction_menu()
        elif sub_choice == "2" and self.manager.get_all_categories():
            self.delete_category_menu()
        elif sub_choice == "3" and self.manager.get_all_transactions():
            self.delete_all_transactions_menu()
        elif sub_choice == "4" and self.manager.get_all_categories():
            self.delete_all_categories_menu()
        else:
            print("\nFout: Ongeldige keuze bij verwijderen.")

    def delete_transaction_menu(self):
        print("\n--- Beschikbare transacties ---")
        transactions = self.manager.get_all_transactions()
        for transaction in transactions:
            print(f"{transaction[0]}: {transaction[1]} - {transaction[2]} (Categorie: {transaction[3]})")

        transaction_id = int(input("\nVoer het ID van de transactie in die je wilt verwijderen: "))
        if transaction_id in [trans[0] for trans in transactions]:
            self.manager.delete_transaction(transaction_id)
            print("Transactie is succesvol verwijderd.")
        else:
            print("Fout: Ongeldige transactie ID.")

    def delete_category_menu(self):
        print("\n--- Beschikbare categorieën ---")
        categories = self.manager.get_all_categories()
        for category in categories:
            print(f"{category[0]}: {category[1]}")

        category_id = int(input("\nVoer het ID van de categorie in die je wilt verwijderen: "))
        if category_id in [cat[0] for cat in categories]:
            self.manager.delete_category(category_id)
            print("Categorie is succesvol verwijderd.")
        else:
            print("Fout: Ongeldig categorie ID.")

    def delete_all_transactions_menu(self):
        confirmation = input("Weet je zeker dat je ALLE transacties wilt verwijderen? (ja/nee): ").lower()
        if confirmation == 'ja':
            self.manager.delete_all_transactions()
            print("Alle transacties zijn succesvol verwijderd.")
        else:
            print("Verwijderen van alle transacties geannuleerd.")

    def delete_all_categories_menu(self):
        confirmation = input("Weet je zeker dat je ALLE categorieën wilt verwijderen? (ja/nee): ").lower()
        if confirmation == 'ja':
            self.manager.delete_all_categories()
            print("Alle categorieën zijn succesvol verwijderd.")
        else:
            print("Verwijderen van alle categorieën geannuleerd.")
