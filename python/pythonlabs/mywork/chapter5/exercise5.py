import os

def addition(x,y):
    return x+y
def subtraction(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def division(x,y):
    return x/y
def main():
    prompt = """Calculator options:
    1. Add
    2. Subtract
    3. Multiply
    4. Divide
    5. Quit
    """

    select = input(prompt)
    if select == '5':
        return
    numbers = input('Enter number seperated by space: ')
    numbers = numbers.split()
    numbers[0] = int(numbers[0])
    numbers[1] = int(numbers[1])
    if select == '1':
        print(addition(numbers[0], numbers[1]))
    elif select == '2':
        print(subtraction(numbers[0], numbers[1]))
    elif select == '3':
        print(multiplication(numbers[0], numbers[1]))
    elif select == '4':
        print(division(numbers[0], numbers[1]))

main()
    