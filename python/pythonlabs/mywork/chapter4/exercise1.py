#exercise1

prompt = ('Enter a number (or the word "end" to quit) ')

setA = set()

counter = int()

while True:

    data = input(prompt)

    if data == 'end':

        break

    elif int(data) in setA:

        counter += 1

    else:

        setA.add(int(data))

print('Number of elements not added {}'.format(counter))

print(setA)

        
