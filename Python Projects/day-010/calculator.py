def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = float(input("First number: "))
    for symbol in operations:
        print(symbol)
    continue_operating = True
    while continue_operating:
        operation = input("Operation: ")
        num2 = float(input("Second number: "))
        answer = operations[operation](num1, num2)
        print(f"{num1} {operation} {num2} = {answer}")
        continue_operating = input(f"Type 'y' to continue operating with {answer}, 'n' to start operating from scratch, or anything else to exit: ")
        if continue_operating == "y":
            num1 = answer
        elif continue_operating == "n":
            calculator()
        else:
            continue_operating = False

calculator()