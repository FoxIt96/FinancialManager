import matplotlib.pyplot as plt

class GraphMenu:
    def __init__(self, manager):
        self.manager = manager

    def run(self):
        print("\n--- Grafieken ---")
        print("1. Toon verdeling van transacties per categorie")
        print("2. Toon percentage van transacties per categorie")
        sub_choice = input("\nMaak een keuze: ").lower()

        if sub_choice == "1":
            self.plot_transaction_distribution_per_category()
        elif sub_choice == "2":
            self.plot_transaction_distribution_percentages()
        else:
            print("\nFout: Ongeldige keuze bij grafieken.")

    def plot_transaction_distribution_per_category(self):
        self.manager.plot_transaction_distribution_per_category()

    def plot_transaction_distribution_percentages(self):
        self.manager.plot_transaction_distribution_percentages()