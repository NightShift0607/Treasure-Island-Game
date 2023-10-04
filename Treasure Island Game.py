while True:
    print('''
    *******************************************************************************
            |                   |                  |                     |
    _________|________________.=""_;=.______________|_____________________|_______
    |                   |  ,-"_,=""     `"=.|                  |
    |___________________|__"=._o`"-._        `"=.______________|___________________
            |                `"=._o`"=._      _`"=._                     |
    _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
    |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
    |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
            |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
    _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
    |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
    |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
    ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
    /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
    ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
    /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
    ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
    /______/______/______/______/______/______/______/______/______/______/_____ /
    *******************************************************************************
    ''')
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.") 
    print("""You're standing at a Crossroad in a Jungle's End.
There are two paths, one path leads you into an open field near a river and another goes downhill towards a cave.
Left leads to open field near a river.
Right leads to downfill cave.""")
    option = input("Where do you want to go? Left or Right \n")
    option = option.capitalize()
    if option == "Left":
        print("""You arrive at a river.
You have only two ways cross the river.
Swim across the river.
Make a boat to cross the river.""")
        option = input("What do you want to do? Swim or Wait \n")
        option = option.capitalize()
        if option == "Wait":
            print("""You cross the river unharmed.
There are 3 houses with 3 different colour of doors.
1st house have a Red Door.
2nd house have a Yellow Door.
3rd house have a Blue Door.""")
            option = input("Which house do you want to in? Red, Yellow or Blue \n")
            option = option.capitalize()
            if option == "Yellow":
                print("Congratulations, You found the Treasure!!!")
            elif option == "Red":
                print("""There was a Killer in the house.
    GAME OVER !!!""")
            else:
                print("""There was a bomb in the house.
    GAME OVER !!!""")
        else:
            print("""There was a Crocodile in the river.
    GAME OVER !!!""")
    else:
        print("""There was a lion in the cave.
    GAME OVER !!!""")
    c = input("Do you want play again? Y/N: ")
    if c.upper() == 'N':
        break