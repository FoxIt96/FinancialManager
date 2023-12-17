class ExportMenu:
    def __init__(self, manager):
        self.manager = manager

    def run(self):
        print("\n--- Exporteren ---")
        print("1. Exporteer alle transacties naar CSV")
        sub_choice = input("\nMaak een keuze: ").lower()

        if sub_choice == "1":
            self.export_transactions_menu()
        else:
            print("\nFout: Ongeldige keuze bij exporteren.")

    def export_transactions_menu(self):
        filename = input("Voer de naam van het CSV-bestand in (zonder .csv): ")
        self.manager.export_transactions_to_csv(filename)
        print(f"Transacties zijn succesvol geëxporteerd naar {filename}.csv.")
