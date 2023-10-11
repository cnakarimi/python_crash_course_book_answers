def alien_shot(alien_color):
    if alien_color == "green":
        print("You just earned 5 points")
    elif alien_color == "yellow":
        print("You just earned 10 points")
    elif alien_color == "red":
        print("You just earned 15 points")


alien_shot("green")
alien_shot("yellow")
alien_shot("red")
