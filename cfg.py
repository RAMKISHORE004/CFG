#Write a program to accept a CFG and display LHS and RHS of CFG?

import re
print("if more than one cfg entered seperate them with commas")
while(True):#To stop enter end
    LHS,RHS=[],[]
    inp = input("Enter only cfg -- ")
    if inp.lower() == 'end':
        break
    cfgs = inp.split(',')
    for cfg in cfgs:
        alpha = re.findall('(\S+)->',cfg)
        try:
            x = re.findall("[A-Z]", alpha[0])
            if len(alpha[0]) != 1 or len(x) != 1:
                alpha = 2/0
            other = re.findall('[\S+]->(\S+)',cfg)
            other = re.findall(r'\w+',other[0])
            LHS.extend(alpha)
            RHS.extend(other)
        except:
            print(cfg," is not CFG")
    if LHS != [] and RHS != []:
        print("LHS = ",LHS,"\nRHS = ",RHS)

