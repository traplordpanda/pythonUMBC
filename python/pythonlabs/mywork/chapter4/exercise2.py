userSent = ('Enter a word to calculate unique words and end to end:')

setA = set()

counter = int()

while True:

    data = input(userSent)

    if data == 'end':

        break

    elif data in setA:

        counter += 1

    else:

        setA.add(data)



print('Number of elements not added {}'.format(counter))

print(sorted(setA))
