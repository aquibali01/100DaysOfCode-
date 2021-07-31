MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

money = 0
is_coffee_serving = True


def check_resource_sufficient(drink):
    global depleted
    if resources['water'] > MENU[drink]['ingredients']['water']:
        if resources['milk'] > MENU[drink]['ingredients']['milk']:
            if resources['coffee'] > MENU[drink]['ingredients']['coffee']:
              return True
            else:
              depleted = "coffee"
              return False
        else:
          depleted = "milk"
          return False
    else:
      depleted = "water"
      return False

def check_transaction_Successful(drink, total_money):
    global money
    if total_money < MENU[drink]['cost']:
         print("Sorry that's not enough money. Money Refunded.")
         return False
    elif total_money == MENU[drink]['cost']:
        money = money + total_money
        return True
    elif total_money > MENU[drink]['cost']:
        change_money = total_money - MENU[drink]['cost']
        money = money + total_money - change_money
        print(f"Here is ${change_money} dollars in change")
        return True

def process_coins(no_quarters, no_dimes, no_nickles, no_pennies):
    return (0.25 * no_quarters) + (0.1 * no_dimes) + (0.05 * no_nickles) + (0.01 * no_pennies)


def make_coffee(drink):
    global resources
    resources['water'] = resources['water'] - MENU[drink]['ingredients']['water']
    resources['milk'] = resources['milk'] - MENU[drink]['ingredients']['milk']
    resources['coffee'] = resources['coffee'] - MENU[drink]['ingredients']['coffee']
    print(f"Here is your {drink}. Enjoy!")


while is_coffee_serving:

  prompt = input("What would you like? (espresso/latte/cappuccino): ")

  if prompt == "off":
    is_coffee_serving = False

  elif prompt == "report":
      print(f"Water: {resources['water']}ml")
      print(f"milk: {resources['milk']}ml")
      print(f"coffee: {resources['coffee']}g")
      print(f"Money: {money}$")
  elif prompt == "espresso" or "latte" or "cappuccino":
      is_resource_sufficient = check_resource_sufficient(prompt)

      if is_resource_sufficient:
          no_quarters = int(input("How many quarters?: "))
          no_dimes = int(input("How many dimes?: "))
          no_nickles = int(input("How many nickles?: "))
          no_pennies = int(input("How many pennies?: "))
          total_money = process_coins(no_quarters, no_dimes, no_nickles, no_pennies)
          is_transaction_successful = check_transaction_Successful(prompt,total_money)

          if is_transaction_successful:
              make_coffee(prompt)
      else:
          print(f"Sorry there is not enough {depleted}")
          is_coffe_serving = False