class ViewMenu:
    def __init__(self, manager):
        self.manager = manager

    def run(self):
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
