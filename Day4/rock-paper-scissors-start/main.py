import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = int(input("What do you chose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

computer_choice = random.randint(0,2)

if choice == 0:
  print(rock,"\n")
  print("Computer chose:\n")
 
  if computer_choice == 0:
    print(rock,"\n")
    print("Match draw")
  elif computer_choice == 1:
    print(paper,"\n")
    print("You lose")
  elif computer_choice == 2:
    print(scissors,"\n")
    print("Match win")
  
if choice == 1:
  print(paper,"\n")
  print("Computer chose:\n")

  if computer_choice == 0:
    print(rock,"\n")
    print("You win")
  elif computer_choice == 1:
    print(paper,"\n")
    print("Match Draw")
  elif computer_choice == 2:
    print(scissors,"\n")
    print("Match lose")

if choice == 3:
  print(scissors,"\n")
  print("Computer chose:\n")

  if computer_choice == 0:
    print(rock,"\n")
    print("you lose")
  elif computer_choice == 1:
    print(paper,"\n")
    print("You win")
  elif computer_choice == 2:
    print(scissors,"\n")
    print("Match draw")

if choice >2 :
  print("You lose, you chose an invalid number")