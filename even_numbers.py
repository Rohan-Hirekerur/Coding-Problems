# -*- coding: utf-8 -*-

def evenDigits(num):
    num = str(num)
    for digit in str(num):
        if int(digit)%2==1:
            return False
    return True

num = 5454
inc = False
lb = ""
ub = "2"
mod_by = "1"
length = len(str(num))

for i in range(0, length-1):
    mod_by+="0"
    ub = "1" + ub

mod_by = int(mod_by)
ub = int(ub)
mod = num % mod_by
div = int(num / mod_by)
if not evenDigits(num):
    if div % 2 == 0:
        if num % 10 < 5:
            inc = False
        else:
            inc = True
    else:
        lb = str(int(num / mod_by)-1)
        for i in range(0, length-1):
            lb += "8"
        ub = int(lb) + ub
        print(lb, ub)
        if num - int(lb) > int(ub) - num:
            inc = True
        else:
            inc = False
    
counter = 0
or_num = num    
if inc:
    while not evenDigits(num):
        num+=1
        counter+=1
else:
    while not evenDigits(num):
        num-=1
        counter +=1
        
print(or_num, num, counter)
    

(359-288)%112