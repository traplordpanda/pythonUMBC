mypath = '/home/kyleaubuchon/python/pythonlabs/mywork/chapter9/'
prompt1 = 'Enter the name of the input file and output file seperated by space: '
mystdin = input(prompt1)
while True:
    try:
        myinput = mystdin.split()[0]
        myoutput = mystdin.split()[1]
        break
    except:
        mystdin = input(prompt1)
try:
    f = open(mypath+myinput, 'r')
    f2 = open(mypath+myoutput, 'w')
    output = str()
    while True:
        txt = f.readline()
        if not txt:
            break
        output += txt

    f2.write(output)
    f.close()
    f2.close()
except OSError:
    print('File not found')

