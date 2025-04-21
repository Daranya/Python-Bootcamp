# This was a problem I worked on the following link to navigate the robot to the goal

# https://reeborg.cs20.ca/?lang=en&mode=python&menu=%2Fworlds%2Fmenus%2Fsk_menu.json&name=Maze&url=%2Fworlds%2Ftutorial_en%2Fmaze1.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal(): # Function provided in the site
    if right_is_clear(): # Function provided in the site
        turn_right()
        move() # Function provided in the site
    elif front_is_clear():# Function provided in the site
        move() # Function provided in the site
    else:
        turn_left() # Function provided in the site
        if front_is_clear(): # Function provided in the site
        move() # Function provided in the site

