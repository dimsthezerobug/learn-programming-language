import art


def add(n1, n2):
    return n1 + n2


def substract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(art.logo)
    num1 = float(input("What's the first number?\n: "))
    for symbol in operations:
        print(symbol)
    operation_symbol = input("Pick an operation from the Line above\n: ")
    num2 = float(input("What's the next number?\n: "))

    def calculate(n1, operator, n2):
        """Return the answer of calculating"""

        calculation_function = operations[operator]
        answer = calculation_function(n1, n2)
        output = f"{n1} {operator} {n2} = {answer}"
        n = len(output)
        print("\n" + ("-" * n))
        print(output)
        print(("-" * n) + "\n")

        return answer

    answer = calculate(num1, operation_symbol, num2)

    should_continue = True
    while should_continue:
        next_calculation = input("Click 'enter' to exit.\nType 'y' to continue calcuation, or type 'n' to start a new calculation: ")
        if next_calculation == "n":
            calculator()
        elif next_calculation == "y":
            operation_symbol = input("Pick an opertation : ")
            next_number = float(input("What's the next number?\n: "))

            answer = calculate(answer, operation_symbol, next_number)
        else:
            should_continue = False
            print("Program stopped")


calculator()
