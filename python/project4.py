str_length = input("please type length:\n")
str_width = input("please type width:\n")
str_money = input("how much for 1 meter?\n")

length = float(str_length)
width = float(str_width)
money = float(str_money)

area = length * width
The_agreed_upon_sum = area * money

print("Room area = " + str(area))
print("The money the worker will receive = " + str(The_agreed_upon_sum))