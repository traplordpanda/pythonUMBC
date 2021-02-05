numList = input('Please enter multiple numbers seperated by a space: ')
numList = numList.split()
for i in numList:
    if int(i) > 0:
        print(i)
