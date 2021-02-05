def sorter(numslist):
    return sorted(numslist, reverse=True)

numString = input('Enter a group of number seperated by space to sort\n')
numL = numString.split()
numL = list(map(int, numL)) 
print(sorter(numL))