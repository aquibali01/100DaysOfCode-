# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

BMI = round(weight/(height**2))

if BMI < 18.5:
  print(f"Your Bmi is {BMI}, You are underweight")
elif BMI <25:
  print(f"Your Bmi is {BMI}, You have a normal weight")
elif BMI < 30:
  print(f"Your Bmi is {BMI}, You are overweight")
elif BMI < 35:
  print(f"Your Bmi is {BMI}, You are obese")
else:
  print(f"Your Bmi is {BMI}, You are clinically obese")


