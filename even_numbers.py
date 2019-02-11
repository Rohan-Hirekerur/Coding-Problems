# -*- coding: utf-8 -*-

def evenDigits(num):
    num = str(num)
    for digit in str(num):
        if int(digit)%2==1:
            return False
    return True

cases = int(input())
for x in range(0, cases):
    num = int(input())
    str_num = list(str(num))
    lb = list(str(num))
    ub = list(str(num))
    mod_by = "1"
    nine = False
    counter = 0
    length = len(str(num))
    
    for i in range(0, length-1):
        mod_by+="0"
    
    mod_by = int(mod_by)
    div = int(num / mod_by)
    if not evenDigits(num):
        for i in range(0, length):
            if int(str_num[i]) % 2 != 0:
                if int(str_num[i]) == 9:
                    nine = True
                lb[i] = str(int(str_num[i]) - 1)
                ub[i] = str(int(str_num[i]) + 1)
                for j in range(i+1, length):
                    lb[j] = "8"
                    ub[j] = "0"
                break
        lb = int("".join(lb))
        ub = int("".join(ub))
        if nine:
            counter = int(num - lb)
        else:
            counter = min(int(num - lb), int(ub - num))
            
    print("Case #"+str(x+1)+": "+str(counter))
          
          
          


N=950
888
2000

for i in range(0, N):
    if evenDigit(N-i):
        break
    if evenDigit(N+i):
        break