#4

def sumOfList(numList):

    total = 0

    for i in numList:

        total = total + i

    average = total/(len(numList))

    return total, average



numbers = [5,4,2,2,1,34,45]

print(sumOfList(numbers))
