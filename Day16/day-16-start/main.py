# # import turtle
#
# from turtle import Turtle, Screen
# timmy = Turtle() #OBJECT
# print(timmy)
# timmy.shape("turtle") #method
# timmy.color("magenta") #method
# timmy.forward(100) #method
#
#
# my_screen = Screen() #object
# print(my_screen.canvheight) #attribute
# my_screen.exitonclick() #method


from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"

print(table)