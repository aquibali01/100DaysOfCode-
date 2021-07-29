#print higher lower logo
#Select two random item from the list data
#compare their follower count.
# ask user for the answer.
#If user answer correct increase score and optionA = optionB
#else print score game over 
#score keeping
#make game repeatable
#clear the screen between rounds

from art import logo, vs
from game_data import data
import random
from replit import clear

def check_answer(guess,A_followers,B_followers):
  '''check the user answer against correct followers and return if they are right or not'''
  if A_followers > B_followers:
    if guess == "a":
      return True
    else:
      return False
  else:
    if guess == "b":
      return True
    else:
      return False



#print logo
print(logo)
score = 0
should_continue = True
option_B = random.choice(data)


#Make game repeatable
while should_continue:
  #generate a random account from the game data.
  option_A = option_B
  option_B = random.choice(data)
  while option_A == option_B:
    option_B = random.choice(data)


  #Format the accout data 
  print(f"Compare A: {option_A['name']}, a {option_A['description']}, from {option_A['country']}")

  print(vs)


  print(f"Against B: {option_B['name']}, a {option_B['description']}, from {option_B['country']}")

  ask_user = input("Who has more follwers? Type 'A' or 'B': ").lower()

  #check if user is correct

  follower_count_A = option_A['follower_count']
  follower_count_B = option_B['follower_count']

  is_correct = check_answer(ask_user,follower_count_A,follower_count_B)

  #Clear the screen
  clear()
  print(logo)
  #Give user feedback on their guess 
  #score keeping
  if is_correct:
    score+=1
    print(f"You are right, Current score: {score}")
  else:
    should_continue =False
    print(f"Sorry, that's wrong. Final Score: {score}")

