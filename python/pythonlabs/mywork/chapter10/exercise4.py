import os
global mypath
mypath = '/home/kyleaubuchon/python/pythonlabs/mywork/chapter10/'
def get_owner():
    with open(mypath + 'data.txt', 'r') as f:
        owner_list = f.readlines()
    return [i.rstrip().split() for i in owner_list]

owners = get_owner()
data = dict()
for i in owners:
    name, computer, amount = i
    if name in data:
        if computer in data[name]:
            data[name][computer] += int(amount)
        else:
            data[name].update({computer:int(amount)})
    else:
        data[name] = {computer:int(amount)}
print(data)