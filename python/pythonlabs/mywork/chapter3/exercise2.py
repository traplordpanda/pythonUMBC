luckyNumber = input('Please enter your lucky number')
try:
   int(luckyNumber)
   print('Your lucky number has {} digits'.format(len(luckyNumber)))
except:
   print('Please enter an integer')

