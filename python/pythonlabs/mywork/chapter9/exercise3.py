mypath = '/home/kyleaubuchon/python/pythonlabs/mywork/chapter9/'
prompt1 = 'Enter the name of the input file: '
prompt2 = 'Enter the name of the output file: '
myinput = input(prompt1)
myoutput = input(prompt2)
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