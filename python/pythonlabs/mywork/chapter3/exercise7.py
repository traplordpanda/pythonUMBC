helper = int()

for i in range(5):

    for x in range(10):

        print('{:=2}'.format(helper), end=' ')

        helper += 1

    print('')
