print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))


if height >= 120:
  print("You can go to the rollercoaster ")
  age = int(input("What is your age? "))
  if age < 12:
    print("Please pay 7 $")
  elif age >=12 and age <=17:
    print("Please pay 10 $")
  else:
    print("Please pay 15$")

else:
  print("Grow your height first")