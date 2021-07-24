programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}

#retrieving items from dictionary
print(programming_dictionary["Bug"])

#Adding new item to a dictionary 
programming_dictionary["loop"] = "The action of doing something over and over again"

#create and empty dicyionary

empty_dictionary = {}

#wipe and existing dictioanry

# programming_dictionary = {}

#Edit and item in dictionary
programming_dictionary["Bug"] = "A moth in a computer"
print(programming_dictionary["Bug"])

for key, value in programming_dictionary.items():
  print(key,":",value)