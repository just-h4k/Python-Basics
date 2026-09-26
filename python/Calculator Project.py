num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))
operator = input("Enter an operater (+ - * /):")

if operator == "+":
    reuslt = num1 + num2
    print(round(reuslt, 2))
elif operator == "-":
    reuslt = num1 - num2
    print(round(reuslt ,2))
elif operator == "*":
    print(round(num1 * num2, 2))
elif operator =="/":
    print(round(num1 / num2, 2))
else:
    print("you Entered wrong operator")