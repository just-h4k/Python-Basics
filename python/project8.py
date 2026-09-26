import random
frist_way = random.random()
second_way=random.randint(0,1)


print("welcome to the coin gussing game!")
print("1. Using random.random()")
print("2. Using random.randint()")
user_choice = input("Enter your choice (1 or 2): ")

if user_choice == "1" or user_choice == "one":
    if frist_way >= 0.5:
        combuter_choice = "heads"
    else:
        combuter_choice = "tails"
elif user_choice == "2" or user_choice == "two":
    if second_way == 0:
        combuter_choice = "heads"
    else:
        combuter_choice ="tails"
else:
    print("This choice is incomprehensible.")
choice = input("Enter your choice (heads or tails): ")
if choice.lower() == combuter_choice.lower():
    print("Congratulations on the choice; it matches the computer.")
else:
    print("Sorry, the choice is incorrect. Please try again.")
print(f"The computer chose: {combuter_choice}")        
