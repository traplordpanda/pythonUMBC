numL = list()
while True:
    try:
        num_add = input('Please enter value: ')
        num_add = int(num_add)
        numL.append(num_add)
    except ValueError:
        print("Please enter integer")
    except KeyboardInterrupt:
        pass
    except EOFError:
        print('\nSum of number is {}'.format(sum(numL)))
        break
