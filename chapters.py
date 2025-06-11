def scene_one(player_name):
    print(f"story {player_name} story")

first_option = ["option1, option2, option3, option4"]

def scene_two(choice_one,first_option):
    if choice_one == first_option[0]:
        print(f"story")
    elif choice_one == first_option[1]:
        print(f"story2")
    elif choice_one == first_option[2]:
        print(f"story3")
    elif choice_one == first_option[3]:
        print(f"story4")
    else:
        input("that isn't a choice please pick a choice.:") 