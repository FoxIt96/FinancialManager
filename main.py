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
            print("5. Exporteer alle transacties naar CSV")
            print("6. Stop")
            choice = input("\nMaak een keuze: ")

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
                    print(f"{transaction[1]}: {transaction[2]} (Categorie: {transaction[3]})")

            elif choice == "5":
                filename = input("Voer de naam van het CSV-bestand in (zonder .csv): ")
                self.manager.export_transactions_to_csv(filename + '.csv')
                print(f"Transacties zijn succesvol geëxporteerd naar {filename}.csv.")

            elif choice == "6":
                print("\nBedankt voor het gebruiken van onze applicatie. Tot ziens!")
                break

            else:
                print("\nFout: Ongeldige keuze. Probeer het opnieuw.")


if __name__ == "__main__":
    app = App()
    app.run()
