calc = input("Choose " \
"1. Add " \
"2. Subtract " \
"3. Multiply " \
"4. Devide ")
if calc == "1" or "Add" or "add" or "ADD":
    number1 = input("First number: ")
    number2 = input("Second number: ")
    number1 = int(number1)
    number2 = int(number2)
    print(number1 + number2)
if calc == "2" or "Subtract" or "subtract" or "SUBTRACT":
    number3 = input("First number: ")
    number4 = input("Second number: ")
    number3 = int(number3)
    number4 = int(number4)
    print(number3 - number4)
if calc == "3" or "Multiply" or "multiply" or "MULTIPLY":
    number5 = input("First number: ")
    number6 = input("Second number: ")
    number5 = int(number5)
    number6 = int(number6)
    print(number5 * number6)
if calc == "4" or "Devide" or "devide" or "DEVIDE":
    number7 = input("First number: ")
    number8 = input("Second number: ")
    number7 = int(number7)
    number8 = int(number8)
    print(number7 / number8)
