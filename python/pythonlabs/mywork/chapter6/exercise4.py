def sorter(numslist):
    total = sum(numslist)

    average = total/(len(numslist))
    return total, average

numString = input('Enter a group of number seperated by space to add\n')
numL = numString.split()
numL = list(map(int, numL)) 
print(sorter(numL))
