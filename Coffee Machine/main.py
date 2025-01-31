MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}




def report(lists):
    for item in lists:
        print(f"{item}: {lists[item]}")


def espresso_error(cafe,available,items):
    if items[cafe]["ingredients"]["water"]>available["water"]:
        print("Sorry there is not enough water")
        return True
    elif items[cafe]["ingredients"]["coffee"]>available["coffee"]:
        print("Sorry there is not enough milk")
        return True
    else:
        return False

def error(cafe,available,items):
    if items[cafe]["ingredients"]["water"]>available["water"]:
        print("Sorry there is not enough water")
        return True
    elif items[cafe]["ingredients"]["milk"]>available["milk"]:
        print("Sorry there is not enough milk")
        return True
    elif items[cafe]["ingredients"]["coffee"]>available["coffee"]:
        print("Sorry there is not enough milk")
        return True
    else:
        return False

def update_espresso(cafe,available,items):
    available["water"] -= items[cafe]["ingredients"]["water"]
    available["coffee"] -= items[cafe]["ingredients"]["coffee"]
    available["Money"]+=items[cafe]["cost"]


def update_resources(cafe,available,items):
    available["water"] -= items[cafe]["ingredients"]["water"]
    available["milk"] -= items[cafe]["ingredients"]["milk"]
    available["coffee"] -= items[cafe]["ingredients"]["coffee"]
    available["Money"] += items[cafe]["cost"]


def coins():
    print("Please enter the coins.")
    quarters=float(input("Enter the number of quarters: "))
    dimes = float(input("Enter the number of dimes: "))
    nickels = float(input("Enter the number of nickels: "))
    pennies = float(input("Enter the number of pennies: "))

    total=(quarters*0.25)+(dimes*0.10)+(nickels*0.05)+(pennies*0.01)
    return float(total)

def change(cafe,price,item):
    if price<item[cafe]["cost"]:
        print("Sorry, that's not enough money. Money refunded")
        return True

    elif cafe=="espresso":
        update_espresso(cafe, resources, MENU)
        print(f"Here is ${round(price - item[cafe]['cost'], 5)} in change")
    else:
        update_resources(cafe,resources,MENU)
        print(f"Here is ${round(price - item[cafe]['cost'],5)} in change")

def espresso():
    wrong=espresso_error("espresso",resources,MENU)
    if wrong:
        return
    paid=coins()
    wrong=change("espresso",paid,MENU)
    if wrong:
        return
    print(f"Here is your espresso 🍵. Enjoy")

def latte():
    wrong = error("latte", resources, MENU)
    if wrong:
        return
    paid = coins()
    wrong=change("latte", paid, MENU)
    if wrong:
        return
    print(f"Here is your latte 🍵. Enjoy")

def cappuccino():
    wrong = error("cappuccino", resources, MENU)
    if wrong:
        return
    paid = coins()
    wrong=change("cappuccino", paid, MENU)
    if wrong:
        return
    print(f"Here is your cappuccino 🍵. Enjoy")

def replenish(item):
    item["water"]=300
    item["milk"]=200
    item["coffee"]=100



answer = ""
resources["Money"] = 0
while answer!="off":

    # print(MENU["espresso"]["ingredients"]["water"])
    answer=input("What would you like? (espresso/latte/cappuccino): ")

    if answer=="report":
        report(resources)
    elif answer=="espresso":
        espresso()
    elif answer=="latte":
        latte()
    elif answer=="cappuccino":
        cappuccino()
    elif answer=="replenish":
        replenish(resources)