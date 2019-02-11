# -*- coding: utf-8 -*-

"""
No Nine is a counting game that you can try when you are bored. In this game,
you are only allowed to say numbers that are legal. A number is legal if and only if all of the following are true:

it is a natural number (i.e. in the set {1, 2, 3...})
it does not contain the digit 9 anywhere in its base 10 representation
it is not divisible by 9
For example, the numbers 16 and 17 are legal. The numbers 18, 19, 17.2, and -17 are not legal.

On the first turn of the game, you choose and say a legal number F. On each subsequent
turn, you say the next legal number. For example, if you played a game with F = 16, you would say 16, 17, 20, 21, and so on.

Alice is very good at this game and never makes mistakes. She remembers that she 
played a game in which the first number was F and the last number was L (when she 
got tired of the game and stopped), and she wonders how many turns were in the game in total (that is, how many numbers she said).

Input
The input starts with one line containing one integer T; T test cases follow.
Each test case consists of a single line containing two integers F and L: the first and last numbers from the game, as described above.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1), and y is the number of the turns played in the game.

Limits
1 ≤ T ≤ 100.
Time limit: 60 seconds per test set.
Memory limit: 1 GB.
F does not contain a 9 digit.
F is not divisible by 9.
L does not contain a 9 digit.
L is not divisible by 9.
Small dataset (Test set 1 - Visible)
1 ≤ F < L ≤ 106.
Large dataset (Test set 2 - Hidden)
1 ≤ F < L ≤ 1018.
Sample

Input 
 	
Output 
 
2
16 26
88 102

  
Case #1: 9
Case #2: 4

  
In Sample Case #1, the game lasted for 9 turns, and the numbers Alice said were: 16, 17, 20, 21, 22, 23, 24, 25, 26.

In Sample Case #2, the game lasted for 4 turns, and the numbers Alice said were: 88, 100, 101, 102.

"""

"""
def is_legal(num):
    sum_of_digits = 0
    num = str(num)
    if int(num) < 0:
        return False
    for digit in num:
        if int(digit) == 9:
            return False
    for digit in num:
        sum_of_digits += int(digit)
    if sum_of_digits % 9 == 0:
        return False
    return True

cases = int(input())
for i in range(0, cases):
    counter = 0
    bounds = input()
    bounds = bounds.split()
    for num in range(int(bounds[0]), int(bounds[1])+1):
        if is_legal(num):
            counter+=1
    
    print("Case #"+str(i+1)+": "+str(counter))
"""          
    
    



def contains(num):
    num = str(num)
    for digit in num:
        if int(digit) == 9:
            return True
    return False

counter = 0
for i in range(3232, 5445):
    if contains(i):
        counter += 1
    
print (counter)    

def numbers_containing_nine(num_of_digits):
    if num_of_digits == 1:
        return 1
    if num_of_digits <= 0:
        return 0
    return 10**(num_of_digits - 1) + 9 * numbers_containing_nine(num_of_digits - 1)
   
def numbers_containing_nine_in_range(lower_bound, upper_bound):
    diff = upper_bound - lower_bound
    diff = str(diff)
    num = 0
    for i in range(len(diff)-1, -1, - 1):
        print(i)
        num += int(diff[i]) * numbers_containing_nine(i)    
    if int(diff) % 10 == 9:
        num += 1
        
    return num

print("count : ", numbers_containing_nine_in_range(37, 41))

































