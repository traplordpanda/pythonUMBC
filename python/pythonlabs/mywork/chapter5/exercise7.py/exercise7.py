def count(*nums, greater):
    x = int()
    for i in nums:
        if i > greater:
            x += 1
    return x
print(count(1,2,3,4,5,6,7, greater=4))