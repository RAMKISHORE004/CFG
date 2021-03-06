#Write a program to accept CFG and count number of productions in it.

import re
print("if more than one cfg entered seperate them with commas")
while(True):#To stop enter end
    produc = 0
    inp = input("Enter only cfg -- ")
    if inp.lower() == 'end':
        break
    cfgs = inp.split(',')
    for cfg in cfgs:
        alpha = re.findall('(\S+)->',cfg)
        try:
            x = re.findall("[A-Z]", alpha[0])
            other = re.findall('[\S+]->(\S+)',cfg)
            if len(alpha[0]) != 1 or len(x) != 1 or len(other[0])<1:
                alpha = 2/0
            other = re.findall(r'\w+',other[0])
            produc += len(other)
        except:
            print(cfg," is not CFG")
    print("Number of productions : ",produc)



