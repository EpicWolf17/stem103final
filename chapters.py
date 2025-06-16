import random



def scene_one(player_name):
    print(f"story {player_name} story")

first_option = ["option1", "option2", "option3", "option4", "random"]
story_one_options = ["option5", "option6", "option7", "option8", "random"]
story_two_options = ["option9", "option10", "option11", "option12", "random"]
story_three_options = ["option13", "option14", "option15", "option16", "random"]
story_four_options = ["option17", "option18", "option19", "option20", "random"]

def scene_two(choice_one):
    if choice_one == "random":
        random_choice = random.choice(first_option)
        print(f"Randomly picked: {random_choice}")
        scene_two(random_choice)
        return
    
    elif choice_one == "option1":
        print(f"story1")
        print(story_one_options)
        second_option_one = input("What should I do next?:")
        scene_three_one(second_option_one)

    elif choice_one == "option2":
        print(f"story2")
        print(story_two_options)
        second_option_two = input("what should I do next?:")
        scene_three_two(second_option_two)

    elif choice_one == "option3":
        print(f"story3")
        print(story_three_options)
        second_option_three = input("what should I do next?:")
        scene_three_three(second_option_three)

    elif choice_one == "option4":
        print(f"story4")
        print(story_four_options)
        second_option_four = input("what should I do next?:")
        scene_three_four(second_option_four)

    else:
        print("sorry thats not an option.")



def scene_three_one(second_option_one):
    if second_option_one == "random":
        random_choice = random.choice(story_one_options)
        print(f"Randomly picked: {random_choice}")
        scene_three_one(random_choice)

    elif second_option_one == "option5":
        print("story5")

    elif second_option_one == "option6":
        print("story6")

    elif second_option_one == "option7":
        print("story7")

    else:
        second_option_one == "option8"
        print("story8")

def scene_three_two(second_option_two):
    if second_option_two == "random":
        random_choice = random.choice(story_two_options)
        print(f"Randomly picked: {random_choice}")
        scene_three_two(random_choice)

    elif second_option_two == "option9":
        print("story9")

    elif second_option_two == "option10":
        print("story10")

    elif second_option_two == "option11":
        print("story11")

    else:
        second_option_two == "option12"
        print("story12")

def scene_three_three(second_option_three):
    if second_option_three == "random":
        random_choice = random.choice(story_three_options)
        print(f"Randomly picked: {random_choice}")
        scene_three_three(random_choice)

    elif second_option_three == "option13":
        print("story13")

    elif second_option_three == "option14":
        print("story14")

    elif second_option_three == "option15":
        print("story15")

    else:
        second_option_three == "option16"
        print("story16")

def scene_three_four(second_option_four):
    if second_option_four == "random":
        random_choice = random.choice(story_four_options)
        print(f"Randomly picked: {random_choice}")
        scene_three_four(random_choice)

    elif second_option_four == "option17":
        print("story17")

    elif second_option_four == "option18":
        print("story18")

    elif second_option_four == "option19":
        print("story19")
        
    else:
        second_option_four == "option20"
        print("story20")










def start(restarting_game):
    if restarting_game == "yes":
        print("OKAY WONDERFUL lets go to the start then.")
    elif restarting_game == "no":
        print("Okay it was fun adventuring with you! BYE")
    else:
        print("Sorry thats not a correct answer")














