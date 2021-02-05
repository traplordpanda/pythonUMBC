num_list = [1,2,3,4,5,6,7,8,9,10]
check = input('Enter number 0-9 to check value at index')
try:
    check = int(check)
except ValueError:
    print('Please enter an integer ')
    
try:
    print('Value at index {} is {}'.format(check, num_list[check]))
except IndexError:
    print('Value is out of index')
