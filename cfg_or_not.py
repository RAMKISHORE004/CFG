#Write a program to check whether given input is CFG or not.

import re
while(True):#To stop enter end
    cfg = input("Enter a cfg -- ")
    if cfg.lower() == 'end':
        break
    alpha = re.findall('(\S+)->',cfg)
    try:
        x = re.findall("[A-Z]", alpha[0])
        other = re.findall('[\S+]->(\S+)',cfg)
        if len(alpha[0]) != 1 or len(x) != 1 or len(other[0])<1:
            alpha = 2/0
        print(cfg," is CFG")
    except:
        print(cfg," is not CFG")

