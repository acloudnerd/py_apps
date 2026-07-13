from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def main():
    money_machine = MoneyMachine()
    coffee_maker = CoffeeMaker()
    menu = Menu()
    machine_on = True

    while machine_on:

        choice = input(f"What would you like? ({menu.get_items()}):   ").strip().lower()

        if choice == "off":
            machine_on = False
        elif choice == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(choice)

            if drink is None:
                continue

            if not coffee_maker.is_resource_sufficient(drink):
                continue

            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)

if __name__ == "__main__":
    main()