from app.models import Transaction, Category
from app.manager import FinancialManager

class App:
    def __init__(self):
        self.manager = FinancialManager('my_database.db')

    def run(self):
        while True:
            print("\n--- Financiële Manager ---")

            print("\n--- Transacties ---")
            print("1. Voeg een transactie toe")
            print("2. Bekijk alle transacties")

            print("\n--- Categorieën ---")
            print("3. Voeg een categorie toe")
            print("4. Bekijk alle categorieën")

            if self.manager.get_all_categories():
                print("\n--- Bijwerken ---")
                print("7. Werk een categorie bij")
                print("8. Werk een transactie bij")

                print("\n--- Exporteren ---")
                print("5. Exporteer alle transacties naar CSV")

            print("\n6. Stop")

            choice = input("\nMaak een keuze: ")

            if choice == "1":
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

            elif choice == "2":
                print("\n--- Alle transacties ---")
                transactions = self.manager.get_all_transactions()
                for transaction in transactions:
                    print(f"{transaction[1]}: {transaction[2]} (Categorie: {transaction[3]})")

            elif choice == "3":
                name = input("\nVoer een naam in voor de nieuwe categorie: ")
                self.manager.add_category(Category(name))
                print(f"Categorie '{name}' is succesvol toegevoegd.")

            elif choice == "4":
                print("\n--- Alle categorieën ---")
                categories = self.manager.get_all_categories()
                for category in categories:
                    print(f"{category[0]}: {category[1]}")

            elif choice == "5":
                filename = input("Voer de naam van het CSV-bestand in (zonder .csv): ")
                self.manager.export_transactions_to_csv(filename + '.csv')
                print(f"Transacties zijn succesvol geëxporteerd naar {filename}.csv.")

            elif choice == "6":
                print("\nBedankt voor het gebruiken van onze applicatie. Tot ziens!")
                break

            elif choice == "7":
                print("\n--- Categorie bijwerken ---")
                categories = self.manager.get_all_categories()
                for category in categories:
                    print(f"{category[0]}: {category[1]}")
                category_id = int(input("\nVoer een categorie ID in: "))
                new_name = input("Voer de nieuwe naam in voor de categorie: ")
                self.manager.update_category(Category(new_name, id=category_id))
                print(f"Categorie met ID {category_id} is succesvol bijgewerkt naar '{new_name}'.")

            elif choice == "8":
                print("\n--- Transactie bijwerken ---")
                transactions = self.manager.get_all_transactions()
                for transaction in transactions:
                    print(f"{transaction[0]}: {transaction[1]} (Categorie: {transaction[3]})")
                transaction_id = int(input("\nVoer een transactie ID in: "))
                new_description = input("Voer de nieuwe beschrijving in voor de transactie: ")
                new_amount = float(input("Voer het nieuwe bedrag in voor de transactie: "))
                new_category_id = int(input("Voer het nieuwe categorie ID in voor de transactie: "))
                self.manager.update_transaction(Transaction(new_description, new_amount, new_category_id, id=transaction_id))
                print(f"Transactie met ID {transaction_id} is succesvol bijgewerkt.")

            else:
                print("\nFout: Ongeldige keuze. Probeer het opnieuw.")

if __name__ == "__main__":
    app = App()
    app.run()
