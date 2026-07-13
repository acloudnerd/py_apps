import art



def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return abs(n1-n2)

def multip(n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2

calc = {"+": add,
        "-": sub,
        "/": divide,
        "*": multip
}

def calculator():
    print(art.logo)
    feeling_like_a_mathematician = True
    num1 = float(input("Insert the first number:  "))

    while feeling_like_a_mathematician:

        for op in calc:
            print(op)
        operator = input("Mathematical operator of your choice from the choices above: ")

        num2 = float(input("Insert the second number: "))

        result = calc[operator](num1,num2)
        print(f"{num1} + {num2} = {result}")


        WannaContinue = input(f"Type 'y' if you wanna continue calculating with {result}:   ").lower()

        if WannaContinue == 'y':
            num1 = result
        else:
            feeling_like_a_mathematician = False
            print("\n" * 10)
            calculator()

calculator()




