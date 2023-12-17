


from app.add_menu import AddMenu
from app.view_menu import ViewMenu
from app.edit_menu import EditMenu
from app.delete_menu import DeleteMenu
from app.export_menu import ExportMenu
from app.statistics_menu import StatisticsMenu
from app.graph_menu import GraphMenu


class MainMenu:
    def __init__(self, manager):
        self.manager = manager
        self.add_menu = AddMenu(manager)
        self.view_menu = ViewMenu(manager)
        self.edit_menu = EditMenu(manager)
        self.delete_menu = DeleteMenu(manager)
        self.export_menu = ExportMenu(manager)
        self.statistics_menu = StatisticsMenu(manager)
        self.graph_menu = GraphMenu(manager)
    def display(self):
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

    def handle_choice(self, choice):
        if choice == "1":
            self.add_menu.run()
        elif choice == '2':
            self.view_menu.run()
        elif choice == "3":
            self.edit_menu.run()
        elif choice == "4":
            self.delete_menu.run()
        elif choice == "5":
            self.export_menu.run()
        elif choice == "6":
            self.manager.close_current_month()
        elif choice == "7":
            self.statistics_menu.run()
        elif choice == "8":
            self.graph_menu.run()
        elif choice == "9":
            pass  # Deze keuze wordt in de main loop afgehandeld
        else:
            print("\nFout: Ongeldige keuze. Probeer het opnieuw.")
