#2

def lengthLongest(stringList):

    longest = str()

    for i in stringList:

        if len(i) > len(longest):

            longest = i

    return i

stringL = 'eat my shorts bart you stupid monkey'.split()

print(lengthLongest(stringL))
