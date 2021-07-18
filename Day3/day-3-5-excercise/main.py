# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_name = name1 + name2

true_count = combined_name.count("t") + combined_name.count("r") + combined_name.count("u") + combined_name.count("e") 

love_count = combined_name.count("l") + combined_name.count("o") + combined_name.count("v") + combined_name.count("e")

love_score = str(true_count) + str(love_count)

int_love_score = int(love_score)

if int_love_score <10 or int_love_score >90:
  print(f"Your score is {int_love_score}, you go together like coke and mentos.")

elif int_love_score >= 40 and int_love_score <= 50:
  print(f"Your score is {int_love_score}, you are alright together.")

else:
  print(f"Your score is {int_love_score}")