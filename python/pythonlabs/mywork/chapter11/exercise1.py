#exercise 2 -\d+.\d+
#exercise 3 \d{2}[A-Z]{2}\s*.*

import re
def isneg_int(mynum):
    r = re.compile('(-\d+)')
    match = r.match(mynum)
    if match == None:
        return 'Not Negative'
    else:
        return 'Negative'

print(isneg_int('-11'))
