# Ask the user to enter the first number
num1 = float(input("Please enter the first number: "))

# Ask the user to enter the second number
num2 = float(input("Please enter the second number: "))

# Ask the user to choose an operation
print("Choose an operation: + (Addition), - (Subtraction), * (Multiplication), / (Division)")
operation = input("Pls enter your choice: ")

# Perform the calculation based on the user's choice
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
    # Check if the second number is zero to avoid division errors
    if num2 == 0:
        print("Error! You cannot divide by zero.")
    else:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
else:
    # Handle invalid input
    print("Invalid operation!!! Please enter +, -, *, or /.")

# Goodbye message
print("Thank you for using brian's SimpleCalculator..Goodbye!")