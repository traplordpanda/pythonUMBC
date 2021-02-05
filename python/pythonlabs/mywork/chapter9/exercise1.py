import os
file = input('Enter file name: ')
f = open(file, 'r')
lines = f.readlines()
sum_words = int()
sum_char = int()
sum_lines = len(lines)
for i in lines:
    sum_char += len(i)
    sum_words += len(i.split())
fmt = '{} has {} lines, {} words and {} characters'
print(fmt.format(file, sum_lines, sum_words, sum_char))