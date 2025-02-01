from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

item_list=Menu()
machine=CoffeeMaker()
money=MoneyMachine()

off=False
while not off:

    answer=input(f"What would you like? ({item_list.get_items()}): ")

    if answer=="report":
        machine.report()
        money.report()

    elif answer=="latte":
        possible=machine.is_resource_sufficient(item_list.find_drink("latte"))
        if possible:
            paid=money.make_payment(item_list.find_drink("latte").cost)
            if paid:
                machine.make_coffee(item_list.find_drink("latte"))

    elif answer=="espresso":
        possible=machine.is_resource_sufficient(item_list.find_drink("espresso"))
        if possible:
            paid=money.make_payment(item_list.find_drink("espresso").cost)
            if paid:
                machine.make_coffee(item_list.find_drink("espresso"))

    elif answer=="cappuccino":
        possible=machine.is_resource_sufficient(item_list.find_drink("cappuccino"))
        if possible:
            paid=money.make_payment(item_list.find_drink("cappuccino").cost)
            if paid:
                machine.make_coffee(item_list.find_drink("cappuccino"))

    elif answer=="off":
        off=True