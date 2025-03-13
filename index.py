
# Basic Calculator Program

# Welcome message
print("Welcome to the Basic Calculator!")
print("This program performs basic mathematical operations on two numbers.")

# Get the first number from the user
num1 = float(input("Enter the first number: "))

# Get the second number from the user
num2 = float(input("Enter the second number: "))

# Get the operation from the user
print("\nChoose an operation:")
print("+ for addition")
print("- for subtraction")
print("* for multiplication")
print("/ for division")
operation = input("Enter the operation symbol: ")

if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == "/":
    if num2 == 0: #check division by 0
        print("Error: Cannot divide by zero!")
    else:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
else:
    print("Invalid operation! Please use +, -, *, or /")

print("\nThank you for using the Basic Calculator!")