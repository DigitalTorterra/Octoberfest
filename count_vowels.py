# -*- coding: utf-8 -*-
"""
Takes a string as input and returns the number of each vowel

2/16/2018
"""

vowels = ['a','e','i','o','u']
lower = 'qwertyuiopasdfghjklzxcvbnm'
upper = 'QWERTYUIOPASDFGHJKLZXCVBNM'

def to_lower_case(string):
    new_str = ''
    for i in string:
        if i in upper:
            for j in range(0, len(upper) - 1):
                if i == upper[j]:
                    new_str = new_str + lower[j]
        else:
            new_str = new_str + i
            
    return(new_str)
    
def vowel_count(string):
    string = to_lower_case(string)
    count = [0,0,0,0,0]
    
    for i in string:
        if i in vowels:
            for j in range(0, 4):
                if i == vowels[j]:
                    count[j] += 1
    return(str(count[0]) + " a's, " + str(count[1]) + " e's, " + str(count[2]) + " i's, " + str(count[3]) + " o's, " + str(count[4]) + " u's")
    
    
"""
Notes: It might have been better to use a list of duples here to eliminate extra for loops

"""