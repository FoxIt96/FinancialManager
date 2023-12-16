from app.manager import FinancialManager

class App:
    def __init__(self):
        self.manager = FinancialManager('my_database.db')

    def run(self):
        while True:
            print("1. Voeg een transactie toe")
            print("2. Bekijk alle transacties")
            print("3. Voeg een categorie toe")
            print("4. Bekijk alle categorieën")
            print("5. Stop")
            choice = input("Maak een keuze: ")
            if choice == "1":
                description = input("Voer een beschrijving in: ")
                amount = float(input("Voer een bedrag in: "))
                category_id = int(input("Voer een categorie ID in: "))
                self.manager.add_transaction(Transaction(description, amount, category_id))
            elif choice == "2":
                transactions = self.manager.get_all_transactions()
                for transaction in transactions:
                    print(f"{transaction[1]}: {transaction[2]} (Categorie ID: {transaction[3]})")
            elif choice == "3":
                name = input("Voer een naam in: ")
                self.manager.add_category(Category(name))
            elif choice == "4":
                categories = self.manager.get_all_categories()
                for category in categories:
                    print(f"{category[0]}: {category[1]}")
            elif choice == "5":
                break

if __name__ == "__main__":
    app = App()
    app.run()