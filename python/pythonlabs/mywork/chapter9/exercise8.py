import os
mypath = '/home/kyleaubuchon/python/pythonlabs/starter/io/'
isfile = [f for f in os.listdir(mypath) if os.path.isfile(mypath+f)]
name_count = dict()
for i in isfile:
    f = open(mypath+i, 'r')
    while True:
        txt = f.readline()
        if not txt:
            break
        else:
            name = txt.replace('\n','')
        if name not in name_count:
            name_count[name] = 1
        else:
            name_count[name] += 1
    f.close()
for k in name_count:
    print('{}\t{}'.format(k,name_count[k]))
