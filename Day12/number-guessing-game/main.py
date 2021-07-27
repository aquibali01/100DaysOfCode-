#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art import logo

print(logo)
print("Welcome to the number guessing game")
print("I'm thinking of a number between 1 and 100")
difficulty_level = input("Choose a difficulty level. Type 'easy' or 'hard': ").lower()

if difficulty_level == "easy":
  guess_remaining = 10
elif difficulty_level == "hard":
  guess_remaining = 5

number = random.randint(1,100)

guess_number = int(input("Make a guess: "))
def decrease_guess():
  print("Guess again.")
  print(f"You have {guess_remaining -1} attempts remaining to guess the answer.")
  return guess_remaining - 1

game_end = False
while game_end != True :
  if guess_remaining == 1:
    print("Game Over. You run out of guesses")
    print(f"The correct answer was {number}")
    break
  
  if guess_number > number:
    print("Too High.")
    guess_remaining = decrease_guess()

  elif guess_number < number:
    print("Too Low.")
    guess_remaining = decrease_guess()
  else:
    print(f"You got it! The answer was {number}")
    game_end = True
    break
  guess_number = int(input("Make a guess: "))

