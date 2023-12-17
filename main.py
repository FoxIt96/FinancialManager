from app.menu import MainMenu
from app.manager import FinancialManager

def run_app():
    manager = FinancialManager('my_database.db')
    main_menu = MainMenu(manager)

    while True:
        main_menu.display()
        choice = input("\nMaak een keuze: ").lower()

        if choice == "9":
            print("\nBedankt voor het gebruiken van onze applicatie. Tot ziens!")
            break
        else:
            main_menu.handle_choice(choice)

if __name__ == "__main__":
    run_app()
