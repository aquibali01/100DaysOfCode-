from replit import clear
from art import logo

print(logo)
#calculator 

def add(n1,n2):
  return n1+n2
#substract
def substract(n1,n2):
  return n1-n2
#multiply
def multiply(n1,n2):
  return n1*n2
#Divide
def divide(n1,n2):
  return n1/n2

operations = {
  "+" : add,
  "-" : substract,
  "*" : multiply,
  "/" : divide,
}

def calculation():
  num1 = float(input("What's the first number? "))
  should_continue = True

  while should_continue:
    num2 = float(input("What's the next number? "))

    for symbol in operations:
      print(symbol)

    operation_symbol = input("Pick an opeartion from the above: ")

    calc_func = operations[operation_symbol]

    answer = calc_func(num1,num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

    continue_further = input("Type 'y' to continue calculating with & type 'n' to exit: ").lower()
    if continue_further == "n":
      should_continue = False
      clear()
      calculation()#recursion
    num1 = answer

calculation()