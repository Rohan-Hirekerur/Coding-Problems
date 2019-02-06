"""
In this exercise, you're going to decompress a compressed string.
Your input is a compressed string of the format number[string] and the 
decompressed output form should be the string written number times. For example:
The input
3[abc]4[ab]c
Would be output as
abcabcabcababababc
Other rules
Number can have more than one digit. For example, 10[a] is allowed, and just means aaaaaaaaaa
One repetition can occur inside another. For example, 2[3[a]b] decompresses into aaabaaab
Characters allowed as input include digits, small English letters and brackets [ ].
Digits are only to represent amount of repetitions.
Letters are just letters.
Brackets are only part of syntax of writing repeated substring.
Input is always valid, so no need to check its validity.
Learning objectives
This question gives you the chance to practice with strings, recursion, 
algorithm, compilers, automata, and loops. It’s also an opportunity to work on coding with better efficiency.
"""

ip = "10[a]"
ip1 = "3[abc]4[ab]c]"
ip2 = "2[3[a]b]"
def decompress(inputString):
    i = 0
    count = ""
    subString = ""
    outputString = ""
    while inputString[i].isdigit() and i<len(inputString)-1:
        count+=inputString[i]
        i+=1
    if inputString[i] == "[":
        i+=1
    if inputString[i].isdigit():
        if i<len(inputString):
            j = i
            while inputString[j] != "]" and j < len(inputString)-1:
                j+=1
            subString+=decompress(inputString[i:j+1])
            print(inputString[i:j+1])
            i = j
    if inputString[i] == "]":
        i+=1
    while inputString[i].islower() and i<len(inputString)-1:
        subString += inputString[i]
        i+=1
    if count == '':
        count = "1"
    for x in range(0, int(count)):
        outputString += subString
    if i<len(inputString)-1:
        outputString+=decompress(inputString[i:len(inputString)])
    return outputString

print(decompress(ip2))
    
        
        