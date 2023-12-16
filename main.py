from app.manager import FinancialManager
from app.models import Transaction, Category

class App:
    def __init__(self):
        self.manager = FinancialManager('my_database.db')

    def run(self):
        while True:
            print("\n--- Hoofdmenu ---")
            print("1. Voeg een categorie toe")
            print("2. Bekijk alle categorieën")
            if self.manager.get_all_categories():
                print("3. Voeg een transactie toe")
                print("4. Bekijk alle transacties")
                print("5. Bewerk een transactie")
            if self.manager.get_all_transactions() or self.manager.get_all_categories():
                print("6. Bewerk een categorie")
                print("7. Verwijder een transactie")
                print("8. Verwijder een categorie")
            print("9. Exporteer alle transacties naar CSV")
            print("10. Stop")
            choice = input("\nMaak een keuze: ").lower()

            if choice == "1":
                name = input("\nVoer een naam in voor de nieuwe categorie: ")
                self.manager.add_category(Category(name))
                print(f"Categorie '{name}' is succesvol toegevoegd.")

            elif choice == "2":
                print("\n--- Alle categorieën ---")
                categories = self.manager.get_all_categories()
                for category in categories:
                    print(f"{category[0]}: {category[1]}")

            elif choice == "3" and self.manager.get_all_categories():
                description = input("\nVoer een beschrijving in voor de transactie: ")
                amount = float(input("Voer een bedrag in voor de transactie: "))
                print("\n--- Kies een categorie ---")
                categories = self.manager.get_all_categories()
                for category in categories:
                    print(f"{category[0]}: {category[1]}")
                category_id = int(input("\nVoer een categorie ID in: "))

                if any(category[0] == category_id for category in categories):
                    self.manager.add_transaction(Transaction(description, amount, category_id))
                    print("Transactie is succesvol toegevoegd.")
                else:
                    print("Fout: Ongeldig categorie ID.")

            elif choice == "4":
                print("\n--- Alle transacties ---")
                transactions = self.manager.get_all_transactions()
                for transaction in transactions:
                    print(f"{transaction[0]}: {transaction[1]} - {transaction[2]} (Categorie: {transaction[3]})")

            elif choice == "5" and self.manager.get_all_transactions():
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

            elif choice == "6" and (self.manager.get_all_transactions() or self.manager.get_all_categories()):
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

            elif choice == "7" and self.manager.get_all_transactions():
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

            elif choice == "8" and self.manager.get_all_categories():
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

            elif choice == "9":
                filename = input("Voer de naam van het CSV-bestand in (zonder .csv): ")
                self.manager.export_transactions_to_csv(filename + '.csv')
                print(f"Transacties zijn succesvol geëxporteerd naar {filename}.csv.")

            elif choice == "10":
                print("\nBedankt voor het gebruiken van onze applicatie. Tot ziens!")
                break

            else:
                print("\nFout: Ongeldige keuze. Probeer het opnieuw.")

if __name__ == "__main__":
    app = App()
    app.run()
