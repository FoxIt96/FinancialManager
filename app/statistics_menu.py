class StatisticsMenu:
    def __init__(self, manager):
        self.manager = manager

    def run(self):
        print("\n--- Statistieken ---")
        print("1. Toon algemene statistieken")
        print("2. Toon statistieken per categorie")
        sub_choice = input("\nMaak een keuze: ").lower()

        if sub_choice == "1":
            self.display_general_statistics()
        elif sub_choice == "2":
            self.display_category_statistics()
        else:
            print("\nFout: Ongeldige keuze bij statistieken.")

    def display_general_statistics(self):
        statistics = self.manager.calculate_statistics()
        if statistics:
            mean_amount, total_amount, max_amount, min_amount = statistics
            print("\n--- Algemene Statistieken ---")
            print(f"Gemiddeld Bedrag: €{mean_amount:.2f}")
            print(f"Totaal Bedrag: €{total_amount:.2f}")
            print(f"Maximaal Bedrag: €{max_amount:.2f}")
            print(f"Minimaal Bedrag: €{min_amount:.2f}")
        else:
            print("Geen transacties om statistieken te tonen.")

    def display_category_statistics(self):
        categories = self.manager.get_all_categories()
        if categories:
            print("\n--- Statistieken per Categorie ---")
            for category in categories:
                category_id, category_name = category
                category_total = self.manager.calculate_category_total(category_id)
                print(f"{category_name}: €{category_total:.2f}")
        else:
            print("Geen categorieën beschikbaar.")
