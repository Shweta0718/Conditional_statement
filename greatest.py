# input two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# finding the greatest number
if num1 > num2:
    print(f"The greatest number is: {num1}")
elif num2 > num1:
    print(f"The greatest number is: {num2}")
else:
    print("Both numbers are equal.")
