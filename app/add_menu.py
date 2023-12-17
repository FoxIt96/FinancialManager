from app.models import Category, Transaction

class AddMenu:
    def __init__(self, manager):
        self.manager = manager

    def run(self):
        print("\n--- Toevoegen ---")
        print("1. Voeg een categorie toe")
        print("2. Voeg een transactie toe")
        sub_choice = input("\nMaak een keuze: ").lower()

        if sub_choice == "1":
            self.add_category_menu()
        elif sub_choice == "2" and self.manager.get_all_categories():
            self.add_transaction_menu()
        else:
            print("\nFout: Ongeldige keuze bij toevoegen.")

    def add_category_menu(self):
        name = input("\nVoer een naam in voor de nieuwe categorie: ")
        self.manager.add_category(Category(name))
        print(f"Categorie '{name}' is succesvol toegevoegd.")

    def add_transaction_menu(self):
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
