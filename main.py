# import statements
import time
import random
import sys

# list of possible enemies
random_enemy = random.choice(["dragon", "gorgon",
                             "pirate", "troll", "wicked fairie"])

# the weapons that the player need to defeat the enemy
weapons = ["sword", "bow", "crossbow", "spear"]

# randomly select a weapon for the player
player_weapon = random.choice(weapons).capitalize()

# the empty weapon list
weapon = []

# player's friends
friends = ['Thor', 'Superman']

# functions definitions
'''
Below there are different functions definitions, which have different purposes.
For a brief description read the following list:

Functions:
    - def print_pause(message):
        this function take one parameter(message)
        to print inside the other functions, and moreover,
        take care of the pausing.
    ------------------------------------------------------------------------------------------------

    - def intro():
        this function is an introduciton to the game.
        It describes the first steps of the game,
        and thanks to the random.choice() function wrote above,
        it takes randomly one enemy,
        passing it inside the print_pause function.
    ------------------------------------------------------------------------------------------------

    - def house():
        this function is called when the player choose to knock on the door.
        The player(you) approach the door and an enemy steps out to attack you.

                                        ⬇️⬇️
                                        ⬇️⬇️
                                        ⬇️⬇️

        spoiler😁: you only have a tiny digger,
        maybe is better if you choose to enter inside the cave...
    ------------------------------------------------------------------------------------------------

    - def cave():
        this function check if the weapon is inside the player's weapon list.
        If not, print different messages to the player and
        add the weapon inside the player's weapon list.
        However, if the weapon is inside the list,
        the function print few messages that describe an empty cave.
    ------------------------------------------------------------------------------------------------

    - def field():
        this function print one message telling that you're in the field again
        Later you can choose again, between the door of the house or the cave.
    ------------------------------------------------------------------------------------------------

    - def win():
        it is used to describe the context when the player win the game.
    ------------------------------------------------------------------------------------------------

    - def lose():
        the lose function describe the context when the player lose the game.
    ------------------------------------------------------------------------------------------------

    -def fight():
        with this function, the player choose to fight the enemy or run away.
        If the player want to fight, there is a chance to win,
        but only if the weapon is inside the player's weapon list😜
        Otherwise, if the weapon is not in the list, well...
        However, the player can choose to run away,
        and in this case the field and game functions are called.
    ------------------------------------------------------------------------------------------------

    - def game_over():
        that's the end. You lost. But...you can play again!!
        This function is built for that reason.
        If you type "yes" you'll play again, otherwise, if you type "no",
        well thanks for playing!
        In addition it checks if the input is valid.
    ------------------------------------------------------------------------------------------------

    - def game():
        this function asks the player to choose between knock the door
        or enter inside the cave.
        Based on the player's choice,
        the function returns different scenarios.
        Also, this function checks the input validation.
'''


def print_pause(message):
    print(message)
    time.sleep(2)  # time between messages


def intro():
    # the following lines make possible restarting the game
    # with different enemy and weapon
    global random_enemy, player_weapon, weapon
    weapon = []  # initialize the weapon list again,
    # with zero elements inside it
    random_enemy = random.choice(["dragon", "gorgon", "pirate",
                                  "troll", "wicked fairie"])  # new random enmy
    player_weapon = random.choice(weapons).capitalize()  # new random weapon
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {random_enemy} "
                "is somewhere around here, "
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty"
                "(but not very effective) dagger.")


def thor(choose_friend):
    print_pause("Yeaah! My lightning are the best weapon!")
    print_pause(f"{choose_friend} tried to hit the "
                f"{random_enemy} wiht his hammer.")
    print_pause(f"However, the {random_enemy} "
                f"avoided the hammer and hit {choose_friend}.")
    print_pause(f"{choose_friend} was flare up! "
                f"How can a {random_enemy} avoid his powerful hammer??")
    print_pause(f"At this point {choose_friend} "
                f"unleash the lightning against the {random_enemy}.")
    print_pause(f"This is the end! The {random_enemy} "
                "was struck by lightning!")
    print_pause(f"{choose_friend} won the battle, "
                "and made the village safer!")


def superman(choose_friend):
    print_pause("Look at my strength! My muscles can beat everything!")
    print_pause(f"{choose_friend} tried to speak with the {random_enemy}"
                " to give him an opportunity to surrender.")
    print_pause(f"The {random_enemy} laughed at these words!")
    print_pause(f"So {choose_friend} glanced at the enemy, "
                "his eyes were fiery red.")
    print_pause(f"He used X-ray vision at that moment. "
                f"But the {random_enemy} dodged it.")
    print_pause(f"{choose_friend} was so upset!")
    print_pause(f"He then decided to face the {random_enemy} "
                "using only his strength.")
    print_pause(f"That was the end for the {random_enemy}.")
    print_pause(f"{choose_friend} was too strong for the {random_enemy},"
                " and with a single blow, he defeated him!")
    print_pause(f"The village thanked {choose_friend}. "
                "It had become a safer place!")


def choose_friends():
    choose_friend = input("Type 'Thor', or 'Superman': ").capitalize()
    for friend in friends:
        if choose_friend == "Thor":
            thor(choose_friend)
            game_over()
        elif choose_friend == "Superman":
            superman(choose_friend)
            game_over()
        else:
            print_pause("Please, enter 'Thor' or 'Superman'")
            choose_friends()


def player_friends():
    print_pause("Your friends are here to help you!")
    print_pause(f"I friend, I'm Thor. "
                f"With my lightning we'll defeat the {random_enemy}!")
    print_pause(f"I friend, I'm Superman. "
                f"With my strength we'll defeat the {random_enemy}!")
    print_pause(f"What friend you want to choose to beat the {random_enemy}?")
    choose_friends()


def call_friends():
    print_pause("Would you like to call a friend?")
    call_friend = input("Type 'yes' or 'no': ").lower()
    if call_friend == 'yes':
        player_friends()
    elif call_friend == 'no':
        print_pause("Ok! Your are alone in this battle!"
                    "It will be difficult!")
        fight()
        game_over()
    else:
        print_pause("Please, enter 'yes' or 'no'")
        call_friends()


def house():
    print_pause("You approach the door of the house.")
    print_pause(f"You are about to knock when the door opens "
                f"and out steps a {random_enemy}.")
    print_pause(f"Eep! This is the {random_enemy}'s house!")
    print_pause(f"The {random_enemy} attacks you!")
    # check if the player has the weapon found inside the cave
    if weapon:  # if yes call the following functions
        print_pause("You feel that you can defeat the "
                    f"{random_enemy} with your {player_weapon}")
        fight()
        game_over()
        return
    else:  # otherwise continue with the normal game
        print_pause("You feel a bit under-prepared for this, "
                    "what with only having a tiny dagger.")
        call_friends()


def cave():
    if not weapon:  # check if the list is empty
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        weapon.append(player_weapon)  # add weapon to the list
        print_pause(f"You have found the magical {player_weapon} of Ogoroth!")
        print_pause("You discard your silly old dagger and take the "
                    f"{player_weapon} with you.")
        print_pause("You walk back out to the field.")
    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("You've been here before, and gotten all the good stuff."
                    " It's just an empty cave now.")
        print_pause("You walk back out to the field.")


def field():
    print_pause("You run back into the field. Luckily, "
                "you don't seem to have been followed.")


def win():
    print_pause(f"As the {random_enemy} moves to attack, "
                f"you unsheath your new {player_weapon}.")
    print_pause(f"The {player_weapon} of Ogoroth shines brightly in your hand"
                " as you brace yourself for the attack.")
    print_pause(f"But the {random_enemy} takes one look at your shiny new toy"
                " and runs away!")
    print_pause(f"You have rid the town of the {random_enemy}. "
                "You are victorious!")


def lose():
    print_pause("You do your best...")
    print_pause(f"but your dagger is no match for the {random_enemy}.")
    print_pause("You have been defeated!")
    print_pause("GAME OVER!")


def fight():
    fight_choice = input("Would you like to (1) fight or (2) run away?: ")
    if fight_choice == "1":  # check the choice made by the player
        if weapon:
            win()  # call the win function
        else:
            lose()  # call the lose function
    elif fight_choice == "2":
        field()  # otherwise call the field function
        game()  # and the game function
    else:
        print_pause("Please, enter a valid input")
        fight()


def game_over():
    print_pause("Would you like to play again?")  # take a choice
    fight_again = input("Type yes or no: ").lower()
    if fight_again == 'yes':
        print_pause('Perfect! Restarting the game...')
        intro()  # restarting the game
        game()
    elif fight_again == 'no':
        # print_pause("Thank you for playing!")
        # return the return statement loop two time on
        # "Would you like to (1) fight or (2) run away?:" question.
        sys.exit("Thank you for playing!")  # but this works
    else:
        print_pause("Please, enter 'yes' or 'no'")
        game_over()  # recall the game function to make a choice


def game():
    print_pause("Enter 1 to knock the door of the house")
    print_pause("Enter 2 to peer into the cave")
    print_pause("What would you like to do?")
    game_choice = input("(Please enter 1 or 2): ")
    if game_choice == "1":  # if you choose the door:
        house()
        fight()
        game_over()
    elif game_choice == "2":  # else:
        cave()
        game()
    else:
        print_pause("Please, enter a valid input")
        game()


# main functions calls
intro()
game()
