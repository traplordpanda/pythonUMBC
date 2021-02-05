rangeNum = input('Please enter 3 numbers, lower limit, upper limit, and step :')
rangeNum = rangeNum.split()
x = lambda x: int(x)
for i in range(3):
    rangeNum[i] = x(rangeNum[i])
for i in range(rangeNum[0], rangeNum[1], rangeNum[2]):
   print(i)
