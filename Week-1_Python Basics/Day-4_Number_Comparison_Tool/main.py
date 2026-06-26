# Number Comparison Tool

#Step 1: Get user input for two numbers
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

#Step 2: Compare the two numbers and display the result
if number1 > number2:
    print(f"{number1} is greater than {number2}.")
elif number1 < number2:
    print(f"{number1} is less than {number2}.")
else:
    print(f"{number1} is equal to {number2}.")
