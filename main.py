#Write your code below this line 👇
print("Welcome to the Spaceship!")
print("Your mission is to find the hidden weapon. ")

# PART 1 LEFT OR RIGHT DOOR

door = input("You enter a ship, you notice two doors. Do You choose the left door or the right door? ")
# Convert to lower case
door = door.lower()
# Your good if door is left. Other wise you die. 
if door == "left":
    # MOVE ON TO NEXT QUESTION (wait == good)
    pool = input("You are standing infront of a pool with a bunch of unknown fish. Do you swim or do you wait? ")
    # CONVERT TO LOWER
    pool = pool.lower()
    # WAIT == good
    if pool == "wait":
    # MOVE ON TO NEXT QUESTION
        tunnel = input("You are in front of three tunnels. Do you choose the red, blue, or yellow tunnel? ")
        # CONVERT TO LOWER
        tunnel = tunnel.lower()
        if tunnel == "yellow":
            print("You WIN!")
        elif tunnel == "red":
            print("Burned by fire. Game Over.")
        elif tunnel == "Blue":
            print("Eaten by aliens. Game Over.")
        else:
            print("GAME OVER!!")
    else:
        print("Attacked by shark. Game Over.")
               
else:
    print("You were burned by lasers. GAME OVER.")

        


    

    
    



