print("Welcome to the university grade calculator program.")
print("")
print("")
grade = int(input("Write the total score of your university degree:\n")) 

if grade >= 90:
    print("Your university grade is Excellent")
elif grade >= 75:
    print("Your university grade is Good")
elif grade >= 50:
    print("Your university grade is Acceptable")
else:
    print("Your university grade is Fail")
