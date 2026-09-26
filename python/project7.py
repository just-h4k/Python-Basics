print("""
            ______________________________    . \  | / .
     /                            / \     \ \ / /
    |                            | ==========  - -
     \____________________________\_/     / / \ \
  ______________________________      \  | / | \
 /                            / \     \ \ / /.   .
|                            | ==========  - -
 \____________________________\_/     / / \ \    /
      ______________________________   / |\  | /  .
     /                            / \     \ \ / /
    |                            | ==========  -  - -
     \____________________________\_/     / / \ \
                                        .  / | \  .

""")
print("welcome to my island 👋") 
print("there are tow doors in front you. a red door 🚪 and a blue door🚪")
door = input("witch one do you want to open🤔? ").lower()
if door == "red" or door == "red door":
    print("Oops! you chose the crocodile door.")
    print("Gameover! 🐊🐊🐊🐊🐊")
elif door == "blue" or door == "blue door":
    print("Great! now you entered a room🎉.")
    print("you found 3 boxes: withe🎁, black🎁, green🎁")
    box = input("which box do you open? ").lower()
    if box == "white" or box == "withe box":
        print("Oops! you opened a box filled with snakes 🐍🐍🐍")
    elif box == "black" or box == "black box":
        print("Oops! you opened a box filled with spiders 🕷️🕷️🕷️")
    elif box == "green" or box == "green box":
        print("Congratulation!👏 you found the treasure!🤑💰💰")
    else:
        print(f"Sorry! {box} i don't understand what that mean!!!.")
else:
    print(f"Sorry! {door} i don't understand what that mean!!!.")
