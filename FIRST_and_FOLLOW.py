#Write a program to accept a CFG and write First and Follow of CFG?

import re

def first(lhs,i):
    global FIRST,LHS,RHS
    if lhs not in FIRST:
        FIRST[lhs] = []
    else:
        return
    for j in range(len(RHS[i])):
        if RHS[i][j][0] in LHS:
            first(RHS[i][j][0],LHS.index(RHS[i][j][0]))
            FIRST[lhs].extend(FIRST[RHS[i][j][0]])
        elif RHS[i][j][0] not in FIRST[lhs]:
            if len(re.findall("[A-Z]",RHS[i][j][0]))<1:
                FIRST[lhs].append(RHS[i][j][0])

def follow(rhs,rhs1,i):
    global FOLLOW,LHS,RHS,f
    if rhs in LHS:
        if rhs not in FOLLOW:
            FOLLOW[rhs] = []
        if rhs1 in LHS:
            print(FOLLOW[rhs],"---",FIRST[rhs1])
            FOLLOW[rhs].extend([k for k in FIRST[rhs1] if k not in FOLLOW[rhs]])
        elif rhs1 == 'LHS':
            print(rhs,"---",FOLLOW[rhs],"---",rhs1,"---",FOLLOW[LHS[i]],"---",LHS[i])
            FOLLOW[rhs].extend([k for k in FOLLOW[LHS[i]] if k not in FOLLOW[rhs]])
            if rhs not in f:
                f[rhs]=[]
            if LHS[i] not in f[rhs]:
                f[rhs].extend(LHS[i])
        else:
            if rhs1 not in FOLLOW[rhs]:
                FOLLOW[rhs].append(rhs1)
                
print("if more than one cfg entered seperate them with commas")
while(True):#To stop enter end
    FIRST = dict()
    FOLLOW = dict()
    LHS,RHS=[],[]
    f = dict()
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
            other = other[0].split('/')
            LHS.extend(alpha)
            RHS.append(other)
        except:
            print(cfg," is not CFG")
            
    for i in range(len(LHS)):
        first(LHS[i],i)
        
    FOLLOW[LHS[0]]=['$']
    for i in range(len(RHS)):
        for j in range(len(RHS[i])):
            rhs = RHS[i][j]
            for a in range(len(rhs)):
                if rhs[a] in LHS:
                    if a+1 >= len(rhs):
                        follow(rhs[a],'LHS',i)
                    else:
                        follow(rhs[a],rhs[a+1],i)
            
    print("FIRST = ",FIRST)
    for i in f:
        for j in f[i]:
            FOLLOW[i].extend([k for k in FOLLOW[j] if k not in FOLLOW[i]])
    print("FOLLOW = ",FOLLOW)
