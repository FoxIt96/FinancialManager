class EditMenu:
    def __init__(self, manager):
        self.manager = manager

    def run(self):
        print("\n--- Bewerken ---")
        print("1. Bewerk een transactie")
        print("2. Bewerk een categorie")
        sub_choice = input("\nMaak een keuze: ").lower()

        if sub_choice == "1" and self.manager.get_all_transactions():
            self.edit_transaction_menu()
        elif sub_choice == "2" and (self.manager.get_all_transactions() or self.manager.get_all_categories()):
            self.edit_category_menu()
        else:
            print("\nFout: Ongeldige keuze bij bewerken.")

    def edit_transaction_menu(self):
        print("\n--- Beschikbare transacties ---")
        transactions = self.manager.get_all_transactions()
        for transaction in transactions:
            print(f"{transaction[0]}: {transaction[1]} - {transaction[2]} (Categorie: {transaction[3]})")

        transaction_id = int(input("\nVoer het ID van de transactie in die je wilt bewerken: "))
        if transaction_id in [trans[0] for trans in transactions]:
            transaction_info = self.manager.get_transaction_by_id(transaction_id)
            print(f"\nVolledige informatie van transactie {transaction_info[0]}:")
            print(f"Beschrijving: {transaction_info[1]}")
            print(f"Bedrag: {transaction_info[2]}")
            print(f"Categorie: {transaction_info[3]}")

            new_description = input("Voer de nieuwe beschrijving in: ")
            new_amount = float(input("Voer het nieuwe bedrag in: "))
            print("\n--- Kies een nieuwe categorie ---")
            categories = self.manager.get_all_categories()
            for category in categories:
                print(f"{category[0]}: {category[1]}")
            new_category_id = int(input("\nVoer een categorie ID in: "))

            if any(category[0] == new_category_id for category in categories):
                self.manager.edit_transaction(transaction_id, new_description, new_amount, new_category_id)
                print("Transactie is succesvol bewerkt.")
            else:
                print("Fout: Ongeldig categorie ID.")
        else:
            print("Fout: Ongeldige transactie ID.")

    def edit_category_menu(self):
        print("\n--- Beschikbare categorieën ---")
        categories = self.manager.get_all_categories()
        for category in categories:
            print(f"{category[0]}: {category[1]}")

        category_id = int(input("\nVoer het ID van de categorie in die je wilt bewerken: "))
        if category_id in [cat[0] for cat in categories]:
            category_info = self.manager.get_category_by_id(category_id)
            print(f"\nVolledige informatie van categorie {category_info[0]}:")
            print(f"Naam: {category_info[1]}")

            new_name = input("Voer de nieuwe naam in: ")
            self.manager.edit_category(category_id, new_name)
            print("Categorie is succesvol bewerkt.")
        else:
            print("Fout: Ongeldig categorie ID.")
