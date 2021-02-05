
def pos_only(numList):
    pos_list = list()
    [pos_list.append(i) for i in numList if i > 0]
    return pos_list

numbers=[2,3,4,-3,-6]
print(pos_only(numbers))