################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

#There is no block space

game_level =3
enemies = ["Skeleton", "Zombie","Alien"]

if game_level <5:
  new_enemy = enemies[0]

print(new_enemy)

#modifying Global scope 

enemies = "Skeleton"

def increase_enemies():
  global enemies 
  enemies = "zombie"
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

#global constants

PI = 3.14159 #never going to change
URL = "https:www.google.com"