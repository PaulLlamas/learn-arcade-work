import random


def main_instruction():
    print("Welcome to Seed of Life!")
    print("You have stolen the seed of the Tree of Life to sell it for money.")
    print("You have run 30 miles ahead when the elves realized their seed was stolen.")
    print("The elves want their sacred seed back and are chasing you!")
    print("Survive across the Magic Forest and escape from the elves.")


def main():

    main_instruction()

    done = False
    health = 100
    stamina = 100
    reg_potions = 2
    stamina_potions = 2
    distance_elves = 0
    dark_elves = random.randrange(80, 400)
    distance_traveled = 30
    out_forest = 450

    while not done:
        print("R. Use a regenerative potion. (Refill health)")
        print("E. Use a energy potion. (Refill stamina to 80%)")
        print("A. Run as fast as you can. (15-40 stamina)")
        print("D. Run carefully. (10-25 stamina)")
        print("T. Sleep in a tree for the night. (Refill stamina)")
        print("S. Status check")
        print("Q. Quit.")
        user_choice = input("What do you chose? ")

        # Player checks his status
        if user_choice.lower() == "s":
            print("Your health is", health)
            print("Your stamina is", stamina)
            print("You have", reg_potions, "regenerative potions remaining.")
            print("You have", stamina_potions, "stamina potions remaining.")
            print("The elves are", distance_traveled - distance_elves, "miles away.")
            print("You have traveled", distance_traveled, "miles so far. You still need to travel",
                  out_forest - distance_traveled, "miles to win!")

        # Uses regenerative potion
        if user_choice.lower() == "r":
            if reg_potions == 0:
                print("You have no regenerative potions left!")
            elif reg_potions >= 1:
                health = 100
                reg_potions -= 1
                print("You feel full of vitality!")

        # Uses stamina potion
        if user_choice.lower() == "e":
            if stamina_potions == 0:
                print("You have no stamina potions left!")
            elif stamina_potions >= 1:
                stamina = 80
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
            damage_arrow_hit = random.randrange(10, 50)
            fall = random.randrange(1, 10)
            fall_damage = random.randrange(10, 25)
            stamina_lost = random.randrange(15, 40)
            stamina -= stamina_lost
            reg_potions_prob = random.randrange(1, 40)
            stamina_potions_prob = random.randrange(1, 40)
            reg_potion_bag = random.randrange(1, 2)
            stamina_potion_bag = random.randrange(1, 2)

            if arrow_hit == 1:
                health -= damage_arrow_hit
                print("They are too good! They hit you with an arrow and now you have", health, "health remaining!")
            elif health <= 0:
                print("An arrow took your last breath.")
                print("You died!")
                break

            if reg_potions_prob == 5:
                reg_potions += reg_potion_bag
                print("You found a bag of a dead adventure and you found", reg_potion_bag,
                      "regenerative potions in it!")

            if stamina_potions_prob == 30:
                stamina_potions += stamina_potion_bag
                print("You found a bag of a dead adventure and you found", stamina_potion_bag, "stamina potions in it!")

            if fall == 3:
                health -= fall_damage
                print("You was so distracted that you fell and now you have", health, "health remaining!")
            elif health <= 0:
                print("Your carelessness made you fall to death.")
                print("You died!")
                break


        # Slow run
        if user_choice.lower() == "d":
            slow_travel = random.randrange(10, 20)
            elves_travel = random.randrange(10, 30)
            distance_traveled += slow_travel
            distance_elves += elves_travel
            print("You have traveled", slow_travel, "miles.")
            stamina_lost = random.randrange(10, 25)
            stamina -= stamina_lost
            arrow_hit = random.randrange(1, 6)
            health_arrow_hit = random.randrange(5, 25)
            reg_potions_prob = random.randrange(1, 40)
            stamina_potions_prob = random.randrange(1, 40)
            reg_potion_bag = random.randrange(1, 2)
            stamina_potion_bag = random.randrange(1, 2)

            if arrow_hit == 1:
                health -= health_arrow_hit
            elif health <= 0:
                print("An arrow took your last breath.")
                print("You died!")
                break

            if reg_potions_prob == 5:
                reg_potions += reg_potion_bag
                print("You found a bag of a dead adventure and you found", reg_potion_bag,
                      "regenerative potions in it!")

            if stamina_potions_prob == 30:
                stamina_potions += stamina_potion_bag
                print("You found a bag of a dead adventure and you found", stamina_potion_bag, "stamina potions in it!")

        # Player sleeps
        if user_choice.lower() == "t":
            stamina = 100
            elves_travel = random.randrange(15, 35)
            distance_elves += elves_travel
            print("You feel refresh and ready for another arduous day!")

        # Quitting/Winning/Losing the game
        if user_choice.lower() == "q":
            print("Thank you for playing Seed of Life")
            break
        if distance_traveled >= out_forest:
            print("You got out of the forest!")
            print("You win!")
            break
        if distance_traveled == dark_elves:
            print("You have encountered the dark elves!They fought against the elves and everyone died.")
            print("You won!")
            break
        if distance_elves >= distance_traveled:
            print("The elves caught you!")
            print("You lose!")
            break
        if stamina <= 0:
            print("You collapsed from tiredness and the elves caught you!")
            print("You lose!")
            break
        if 40 >= stamina > 0:
            print("You are feeling tired.")
        if distance_elves >= distance_traveled - 40:
            print("The elves are close! Choose carefully!")


main()
