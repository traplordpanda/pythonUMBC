firstNum = input('Please enter first int ')
secondNum = input('Please enter second int ')
x = 0
for i in range(int(firstNum),int(secondNum)):
    x = x+i
print('Total sum for range: {}'.format(x))
