print(r'''
       \****__              ____                                              
         |    *****\_      --/ *\-__                                          
         /_          (_    ./ ,/----'                                         
            \__         (_./  /                                                
                \__           \___----^__                                       
               _/   _                  \                                      
        |    _/  __/ )\"\ _____         *\                                    
        |\__/   /    ^ ^       \____      )                                   
         \___--"                    \_____ )                                  
                                          "
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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
ans1 = input("You're now standing in the center of a bridge, move 'left' or 'right'?")
if ans1 == "Left" or ans1 == "left":
    ans2 = input("You've come to the fantasy island. There is a lake. 'Swim' or 'wait' for the dragon?")
    if ans2 == "Wait" or ans2 == "wait":
        ans3 = input("The dragon brought you to the triple mountain, which mountain top you want to get down? 'Red', 'Blue', 'Green'?")
        if ans3 == "Green" or ans3 == "green":
            print("You've safely reached the treasure forest. The treasure is yours!")
        elif ans3 == "Blue" or ans3 == "blue":
            print("You've fell into the Mountain Lake! GAME OVER!!!")
        else:
            print("You've fell by the Volcano Mountain! GAME OVER!!!")
    else:
        print("You've drowned into the lake! GAME OVER!!!")
else:
    print("You fell down the hole in the bridge in to the river! GAME OVER!!!")


