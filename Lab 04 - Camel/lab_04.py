import random

def main_instruction():
    print("Welcome to Seed of Life!")
    print("You have stolen the seed of the Tree if Life to sell it for money.")
    print("The elves want their sacred seed back and are chasing you!")
    print("Survive across the Magic Forest and escape from the elves.")

def get_user_input():
    print("R. Use a regenerative potion.")
    print("E. Use a energy potion.")
    print("A. Run as fast as you can.")
    print("D. Run carefully.")
    print("T. Sleep in a tree for the night.")
    print("S. Status check")
    print("Q. Quit.")
    user_choice = input("What do you chose? ")




def main():

    main_instruction()

    done = False
    health = 100
    stamina = 100
    distance_elves = -30

    while not done:
        user_choice = get_user_input()
        get_user_input()

        reg_potion = "R"
        if user_choice.lower() == reg_potion:
            health = 100
            print("You feel full of vitality!")

        energy_potion = "E"
        if user_choice.lower() == energy_potion:
            stamina = 100
            print("You feel refreshed!")
        quit_game = "Q"
        while quit_game == "Q":
            quit_game = input("Do you want to quit? ")
            if quit_game == "y":
                done = True

main()