import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ") #it converts string to list
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

chosen_name = random.randint(0, len(names)-1) # beacuse randint includes the last number too "-1"
person_who_buy = names[chosen_name]
print(f"{person_who_buy} is going to buy the meal today!")
