calc = input("Choose " \
"1. Add " \
"2. Subtract " \
"3. Multiply " \
"4. Divide ")
if calc == "1" or calc == "Add" or calc == "add" or calc == "ADD":
    number1 = input("First number: ")
    number2 = input("Second number: ")
    number1 = float(number1)
    number2 = float(number2)
    print(number1 + number2)
if calc == "2" or calc == "Subtract" or calc == "subtract" or calc == "SUBTRACT":
    number3 = input("First number: ")
    number4 = input("Second number: ")
    number3 = float(number3)
    number4 = float(number4)
    print(number3 - number4)
if calc == "3" or calc == "Multiply" or calc == "multiply" or calc == "MULTIPLY":
    number5 = input("First number: ")
    number6 = input("Second number: ")
    number5 = float(number5)
    number6 = float(number6)
    print(number5 * number6)
if calc == "4" or calc == "Divide" or calc == "divide" or calc == "DIVIDE":
    number7 = input("First number: ")
    number8 = input("Second number: ")
    number7 = float(number7)
    number8 = float(number8)
    print(number7 / number8)
