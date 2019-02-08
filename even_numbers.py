# -*- coding: utf-8 -*-

def evenDigits(num):
    num = str(num)
    for digit in str(num):
        if int(digit)%2==1:
            return False
    return True

num = 99
str_num = list(str(num))
lb = list(str(num))
ub = list(str(num))
inc = True
mod_by = "1"
length = len(str(num))

for i in range(0, length-1):
    mod_by+="0"

mod_by = int(mod_by)
div = int(num / mod_by)
if not evenDigits(num):
    for i in range(0, length):
        if int(str_num[i]) % 2 != 0:
            if int(str_num[i]) == 9:
                inc = False
                break
            lb[i] = str(int(str_num[i]) - 1)
            ub[i] = str(int(str_num[i]) + 1)
            for j in range(i+1, length):
                lb[j] = "8"
                ub[j] = "0"
            lb = int("".join(lb))
            ub = int("".join(ub))
            print(lb, ub)
            break
    if inc and num - lb < ub - num:
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
