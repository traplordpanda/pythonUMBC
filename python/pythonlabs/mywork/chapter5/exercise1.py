#1
def tester(num):
    if num > 0 and isinstance(num, int):
        return num
    else: 
        return 0

positive = input('Please enter a positive int: ')
positive = int(positive)
print(tester(positive))
