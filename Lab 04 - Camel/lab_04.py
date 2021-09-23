import random

def main_instruction():
    print("Welcome to Seed of Life!")
    print("You have stolen the seed of the Tree if Life to sell it for money.")
    print("The elves want their sacred seed back and are chasing you!")
    print("Survive across the Magic Forest and escape from the elves.")





def main():

    main_instruction()

    done = False
    health = 100
    stamina = 100
    reg_potions = 2
    stamina_potions = 2
    distance_elves = 70
    dark_elves = random.randrange(10, 200)
    distance_traveled = 100
    out_forest = 300

    while not done:
        print("R. Use a regenerative potion.")
        print("E. Use a energy potion.")
        print("A. Run as fast as you can.")
        print("D. Run carefully.")
        print("T. Sleep in a tree for the night.")
        print("S. Status check")
        print("Q. Quit.")
        user_choice = input("What do you chose? ")

        # Uses regenerative potion
        if user_choice.lower() == "r":
            health = 100
            reg_potions -= 1
            print("You feel full of vitality!")

        # Uses stamina potion
        if user_choice.lower() == "e":
            stamina = 100
            stamina_potions -= 1
            print("You feel refreshed!")

        # Fast run
        if user_choice.lower() == "a":
            fast_travel = random.randrange(20, 40)
            elves_travel = random.randrange(10, 30)
            distance_traveled += fast_travel
            distance_elves += elves_travel
            print("You have traveled", fast_travel, "miles.")
            arrow_hit = random.randrange(1, 6)
            health_arrow_hit = random.randrange(5, 25)
            stamina_lost = random.randrange(15, 40)
            stamina -= stamina_lost
            if arrow_hit == 1:
                health -= health_arrow_hit
                print("They are too good! They hit you with an arrow and now you have", health, "health remaining!")

            if distance_traveled == dark_elves:
                print("You have encountered the dark elves!They fought against the elves and everyone died.")
                print("You won!")
                done = True

        # Slow run
        if user_choice.lower() == "d":
            slow_travel = random.randrange(10, 20)
            elves_travel = random.randrange(10, 30)
            distance_traveled += slow_travel
            distance_elves += elves_travel
            print("You have traveled", slow_travel, "miles.")
            stamina_lost = random.randrange(10, 30)
            stamina -= stamina_lost
            arrow_hit = random.randrange(1, 6)
            health_arrow_hit = random.randrange(5, 25)
            if arrow_hit == 1:
                health -= health_arrow_hit
            if distance_traveled == dark_elves:
                print("You have encountered the dark elves!They fought against the elves and everyone died.")
                print("You won!")
                done = True

        # Player sleeps
        if user_choice.lower() == "t":
            stamina = 100
            elves_travel = random.randrange(5, 20)
            distance_elves += elves_travel
            print("You feel refresh and ready for another ardous day!")

        # Player checks his status
        if user_choice.lower() == "s":
            print("Your health is", health)
            print("Your stamina is", stamina)
            print("You have", reg_potions, "regenerative potions remaing.")
            print("You have", stamina_potions, "stamina potions remaing.")
            print("The elves are",distance_traveled-distance_elves, "miles away.")
            print("You have traveled", distance_traveled, "miles so far. You still need to travel", out_forest-distance_traveled, "miles to win!")

        if distance_elves >= distance_traveled:
            print("The elves caught you!")
            print("You lose")
            done = True

        if health <= 0:
            print("You died!")
            done = True

        if distance_traveled >= out_forest:
            print("You got out of the forest!")
            print("You win!")
            done = True

        # Quitting the game
        if user_choice.lower() == "q":
            print("Thank you for playing Seed of Life")
            done = True


main()