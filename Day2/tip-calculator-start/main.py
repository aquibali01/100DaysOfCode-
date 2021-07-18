#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
print("Welcome to the tip calculator")

total_amount = float(input("What was the total bill? $"))

percentage_tip = float(input("What percentage tip would you like to give? e.g 10,12 or 15? "))

people_split = int(input("What many people to split the bill? "))

amount_to_be_paid = ( total_amount / people_split) * (1 + percentage_tip/100) 

round_amount = round(amount_to_be_paid , 2)
round_amount = "{:.2f}".format(amount_to_be_paid) # convert float to string and to 2 decimal place
print(f"each person should pay: ${round_amount}")