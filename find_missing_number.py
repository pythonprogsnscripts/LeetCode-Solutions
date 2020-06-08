"""
Given a contiguous sequence of numbers in which each number repeats thrice, there is exactly one missing number. Find the missing number.
eg: 11122333 : Missing number 2
11122233344455666 Missing number 5
"""


def missing_number(num):
    dict ={}
    
    while num>0:
        rem = num%10
        
        if rem not in dict:
            dict[rem] = 1
        else:
            dict[rem] = dict.get(rem) + 1
        
        num = num//10
    
    for key, val in dict.items():
        if val < 3:
            print (key)
            

missing_number(101010199)