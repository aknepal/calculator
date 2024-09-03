import math
import random

output = 0
num1 = ""
operator = ""
num2 = ""
memStore = "Empty"

def abilitiesList():
    print("+...Addition")
    print("-...Subtraction")
    print("*...Multiplication")
    print("/...Division")
    print("^...Powers")
    print("/-...Square Roots")
    print("!...Factorials (Input Cannot Be Negative)")
    print("Abs...Absolute Value")
    print("d/r...Degrees To Radians")
    print("r/d...Radians To Degrees")
    print("pi...Returns PI")
    print("e...Returns 'e'")
    print("tau...Returns TAU (2xPI)")
    print("M+...Save input to memory")
    print("MR...Recall Memory")
    print("M-...Clear Memory")
    print("sin...Sine")
    print("cos...Cosine")
    print("tan...Tangent")
    print("asin...Arc Sine")
    print("acos...Arc Cosine")
    print("atan...Arc Tangent")
    print("log10...Log(10) of Input")
    print("log...Returns The Appropriate Log of the Input (input1 is the log power)")
    print("rand...Returns A Random Number Between 0 and 1")
    print("randint...Returns A Random Number Between The Two Inputs")
    print("--|| ADVANCED CALCULATOR ||--")

def askForNumInput(textPrompt):
    convertedNum = math.nan
    while True:
        num = input(textPrompt)
        try:
            convertedNum = float(num)
            break
        except ValueError:
            print("ERROR: Syntax: Invalid Number")
    return convertedNum

while True:
    print("--|| ADVANCED CALCULATOR ||--")
    print("Type 'help' for a list of abilities")
    
    while True:
        operator = input("What operation do you want to perform? ")
        if operator == "help":
            abilitiesList()
        elif operator == "pi":
            print(math.pi)
        elif operator == "e":
            print(math.e)
        elif operator == "tau":
            print(math.pi * 2)
        elif operator == "MR":
            print(str(memStore))
        elif operator == "M-":
            memStore = "Empty"
            print("Memory Cleared")
        elif operator == "rand":
            print(random.random())
        elif operator in ["+", "-", "*", "/", "^", "/-", "!", "Abs", "d/r", "r/d", "M+", "sin", "cos", "tan", "asin", "acos", "atan", "log10", "log", "randint"]:
            break
        else:
            print("ERROR: Invalid Operator")

    while True:
        num1 = askForNumInput("First Number? ")
        if (operator == "asin" or operator == "acos") and (num1 > 1 or num1 < -1):
            print("ERROR: Math: 'asin' and 'acos' commands only accept inputs in range -1 to +1")
        elif operator == "!" and num1 < 0:
            print("ERROR: Math: Factorials only accept non-negative integers")
        else:
            break

    if operator not in ["/-", "!", "Abs", "d/r", "r/d", "M+", "sin", "cos", "tan", "asin", "acos", "atan", "log10"]:
        while True:
            num2 = askForNumInput("Second Number? ")
            if operator == "/" and num2 == 0:
                print("ERROR: Math: Cannot divide by 0!")
            else:
                break

    if operator == "+":
        output = num1 + num2
    elif operator == "-":
        output = num1 - num2
    elif operator == "*":
        output = num1 * num2
    elif operator == "/":
        output = num1 / num2
    elif operator == "^":
        output = math.pow(num1, num2)
    elif operator == "/-":
        output = math.sqrt(num1)
    elif operator == "!":
        output = math.factorial(int(num1))
    elif operator == "Abs":
        output = math.fabs(num1)
    elif operator == "d/r":
        output = math.radians(num1)
    elif operator == "r/d":
        output = math.degrees(num1)
    elif operator == "M+":
        memStore = num1
        print("Number Stored")
        continue
    elif operator == "sin":
        output = math.sin(num1)
    elif operator == "cos":
        output = math.cos(num1)
    elif operator == "tan":
        output = math.tan(num1)
    elif operator == "asin":
        output = math.asin(num1)
    elif operator == "acos":
        output = math.acos(num1)
    elif operator == "atan":
        output = math.atan(num1)
    elif operator == "log10":
        output = math.log10(num1)
    elif operator == "log":
        output = math.log(num2, num1)
    elif operator == "randint":
        output = random.randint(int(num1), int(num2))

    print("Your Answer: " + str(output))
