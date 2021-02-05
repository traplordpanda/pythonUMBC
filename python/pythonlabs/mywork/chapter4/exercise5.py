from collections import OrderedDict

numToWord = {0:'zero',

             1:'one',

             2:'two',

             3:'three',

             4:'four',

             5:'five',

             6:'six',

             7:'seven',

             8:'eight',

             9:'nine'}

convert = input('Please enter a number')

counter = dict()

for i in convert:

    if i in counter:

        counter[i] += 1

    else:

        counter[i] = 1

    print('{}'.format(numToWord[int(i)]), end=' ')

print('')

counterSort = OrderedDict(sorted(counter.items(), reverse=True))

for i in counterSort:

    print('count for {}: {}'.format(numToWord[int(i)], counterSort[i]))


