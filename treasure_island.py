print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

path = input("Which path do you want to choose? left or right? ").lower()
#lowercase_path = "path".lower()

if path == "left":
    condition_1 = input("Yoy have come to a lake, ther is island middle of the lake so, do you want to swim or wait: ").lower()
  
    if condition_1 == "wait":
        condition_2 = input("You arrived at the unharmed door, there are 3 doors, which door do you want? red, blue or yellow: ").lower()
        if condition_2 == "red":
            print("Burned by fire.")
            print("Game over")
        elif condition_2 == "blue":
            print("Eaten by beast.")
            print("Game over")
        elif condition_2 == "yellow":
            print("You win!")
        else:
            print("Game Over")
    else:
        print("Attacked by trout.")
        print("Game Over")
    
else:
    print("Fall into a hole.")
    print("Game Over")
    
  