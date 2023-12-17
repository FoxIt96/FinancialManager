import numpy as np
import matplotlib.pyplot as plt
from app.manager import FinancialManager
from app.models import Transaction, Category

class App:
    def __init__(self):
        self.manager = FinancialManager('my_database.db')

    def view_all_transactions(self):
        print("\n--- Alle transacties ---")
        transactions = self.manager.get_all_transactions()
        for transaction in transactions:
            print(f"{transaction[0]}: {transaction[1]} - {transaction[2]} (Categorie: {transaction[3]})")
        input("\nDruk op Enter om terug te keren naar het hoofdmenu.")

    def view_all_categories(self):
        print("\n--- Alle categorieën ---")
        categories = self.manager.get_all_categories()
        for category in categories:
            print(f"{category[0]}: {category[1]}")
        input("\nDruk op Enter om terug te keren naar het hoofdmenu.")

    def view_statistics(self):
        statistics = self.manager.calculate_statistics()
        if statistics:
            mean, total, max_value, min_value = statistics
            print("\n--- Statistieken ---")
            print(f"Gemiddelde bedrag: {mean}")
            print(f"Totaal bedrag: {total}")
            print(f"Maximaal bedrag: {max_value}")
            print(f"Minimaal bedrag: {min_value}")

            std_dev = np.std(self.manager.get_transaction_amounts())
            print(f"Standaarddeviatie: {std_dev}")

            input("\nDruk op Enter om terug te keren naar het hoofdmenu.")
        else:
            print("Geen transacties voor statistieken.")

    def plot_transaction_distribution(self):
        self.manager.plot_transaction_distribution()

    def run(self):
        while True:
            print("\n--- Hoofdmenu ---")
            print("1. Toevoegen")
            print("2. Bekijken")
            print("3. Bewerken")
            print("4. Verwijderen")
            print("5. Exporteren")
            print("6. Afsluiten Huidige Maand en Exporteren")
            print("7. Statistieken")
            print("8. Grafieken")
            print("9. Exit")

            choice = input("\nMaak een keuze: ").lower()

            if choice == "1":
                print("\n--- Toevoegen ---")
                print("1. Voeg een categorie toe")
                print("2. Voeg een transactie toe")
                sub_choice = input("\nMaak een keuze: ").lower()

                if sub_choice == "1":
                    name = input("\nVoer een naam in voor de nieuwe categorie: ")
                    self.manager.add_category(Category(name))
                    print(f"Categorie '{name}' is succesvol toegevoegd.")
                elif sub_choice == "2" and self.manager.get_all_categories():
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
                else:
                    print("\nFout: Ongeldige keuze bij toevoegen.")

            elif choice == '2':
                print("--- Bekijken ---")
                print("1. Transacties")
                print("2. Categorieën")
                view_choice = input("Maak een keuze: ")
                if view_choice == '1':
                    self.view_all_transactions()
                elif view_choice == '2':
                    self.view_all_categories()
                else:
                    print("Ongeldige keuze voor bekijken.")

            elif choice == "3":
                print("\n--- Bewerken ---")
                print("1. Bewerk een transactie")
                print("2. Bewerk een categorie")
                sub_choice = input("\nMaak een keuze: ").lower()

                if sub_choice == "1" and self.manager.get_all_transactions():
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
                elif sub_choice == "2" and (self.manager.get_all_transactions() or self.manager.get_all_categories()):
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
                else:
                    print("\nFout: Ongeldige keuze bij bewerken.")

            elif choice == "4":
                print("\n--- Verwijderen ---")
                print("1. Verwijder een transactie")
                print("2. Verwijder een categorie")
                sub_choice = input("\nMaak een keuze: ").lower()

                if sub_choice == "1" and self.manager.get_all_transactions():
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
                elif sub_choice == "2" and self.manager.get_all_categories():
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
                else:
                    print("\nFout: Ongeldige keuze bij verwijderen.")

            elif choice == "5":
                print("\n--- Exporteren ---")
                print("1. Exporteer alle transacties naar CSV")
                sub_choice = input("\nMaak een keuze: ").lower()

                if sub_choice == "1":
                    filename = input("Voer de naam van het CSV-bestand in (zonder .csv): ")
                    self.manager.export_transactions_to_csv(filename)
                    print(f"Transacties zijn succesvol geëxporteerd naar {filename}.")
                else:
                    print("\nFout: Ongeldige keuze bij exporteren.")

            elif choice == "6": 
                print("\n--- Afsluiten Huidige Maand en Exporteren ---")
                self.manager.close_current_month()

            elif choice == "7":
                self.view_statistics()

            elif choice == "8":
                print("\n--- Grafieken ---")
                print("1. Plot uitgaven per categorie")
                print("2. Plot uitgaven per categorie (in percentages)")
                sub_choice = input("\nMaak een keuze: ").lower()

                if sub_choice == "1":
                    self.manager.plot_transaction_distribution_per_category()
                elif sub_choice == "2":
                    self.manager.plot_transaction_distribution_percentages()
                else:
                    print("\nFout: Ongeldige keuze bij plots.")

            elif choice == "9":
                print("\nBedankt voor het gebruiken van onze applicatie. Tot ziens!")
                break

            else:
                print("\nFout: Ongeldige keuze. Probeer het opnieuw.")

if __name__ == "__main__":
    app = App()
    app.run()
