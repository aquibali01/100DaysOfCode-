# # Review: 
# # Create a function called greet(). 
# # Write 3 print statements inside the function.
# # Call the greet() function and run your code.

# def greet():
#   print("Welcome to the cipher")
#   print("You can encrypt the word")
#   print("You can decrypt the word using this software")

# greet()

# def greet_with_name(name):
#   print(f"Welcome to the cipher {name}")
#   print("You can encrypt the word")
#   print("You can decrypt the word using this software")

# greet_with_name("Aquib")

#functions with more than one input

def greet_with(name,location):
  print(f"Hello {name}")
  print(f'what is it like in {location}')
greet_with("Aquib","Portugal") #positional argument
greet_with(location = "Turkey", name = "Aquib")# Keyword argument