import random
#have functions for the each chapter to make code nicer
from chapters import *


#input from the user and the start of the game
player_name = input("What is the name of your character?:")
#opening scene with the player_name
scene_start = scene_one(player_name)
#the list for the start
first_choices = print(first_option)
choice_one = input("What would you like to do?:")
#the players choices outcome
chapter_two = scene_two(choice_one)
#the different lists depending on the players choice
#the ending of the game depending on the choices they made
#ask if they want to play again
restarting_game = input("Would you like to play again? Please put Yes or No:")
restart_scene(restarting_game)
#send them back to the start if they want to play again










