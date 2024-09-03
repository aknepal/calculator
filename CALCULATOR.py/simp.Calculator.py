# Python Simple Calculator

# Initialize values
output = 0
num1 = ""
operation = ""
num2 = ""

# Get user inputs
num1 = input("Hello, what is your first number?\n")
operation = input("Operation (+, -, *, /)?\n")
num2 = input("Your second number?\n")

try:
    # Convert inputs to floats
    floatnum1 = float(num1)
    floatnum2 = float(num2)

    # Perform calculation based on operation
    if operation == "+":
        output = floatnum1 + floatnum2
    elif operation == "-":
        output = floatnum1 - floatnum2
    elif operation == "*":
        output = floatnum1 * floatnum2
    elif operation == "/":
        if floatnum2 != 0:
            output = floatnum1 / floatnum2
        else:
            print("Error: Division by zero is not allowed.")
            exit()
    else:
        print("Invalid operation. Please try again.")
        exit()

    # Print the result
    print("Your answer: " + str(output))

except ValueError:
    print("Invalid input. Please enter valid numbers.")
