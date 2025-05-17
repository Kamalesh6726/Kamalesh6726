def calculator():
    print("Simple Calculator")
    num1 = float(input("Enter first number: "))
    op = input("Enter operation (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Cannot divide by zero.")
            return
    else:
        print("Invalid operation.")
        return

    print(f"Result: {result}")

calculator()
