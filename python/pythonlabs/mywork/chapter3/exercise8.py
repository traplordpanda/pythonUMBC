x = input('Please enter upper, lower values ')

x = x.split()

for i in range(len(x)):

    x[i] = int(x[i])



lower = x[0]

upper = x[1]





if lower > upper:

    upper = x[0]

    lower = x[1]



totalsum = 0

for i in range(lower, upper+1):

    totalsum = totalsum + i

print(totalsum)

    
