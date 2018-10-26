# -*- coding: utf-8 -*-
"""
Takes an input string and converts it into pig latin

2/16/2018
"""
import sys


vowels = ['a','e','i','o','u','A','E','I','O','U']

def str_to_list(message):
    message_list = ['']    
    for char in message:
        if char == ' ':
            message_list.append('')
        else:
            message_list[-1] = message_list[-1] + char
            
    return(message_list)
    
def to_pig_latin(message):
    english = str_to_list(message)
    latin = []    
    for word in english:
        if word[0] in vowels:
            latin.append(word + 'way')
            
        else:
            new_word = ''
            first_vowel = 0
            for i in range(0, len(word) - 1):
                if word[i] in vowels:
                    first_vowel = i
                    break
            
            for j in range(first_vowel, len(word)):
                new_word = new_word + word[j]
            for k in range(0, first_vowel):
                new_word = new_word + word[k]
               
            latin.append(new_word + 'ay')
           
    return(' '.join(latin))
  
print(to_pig_latin(sys.argv[1]))
"""
What I learned:
You can iterate backwards through a string, x[-1] is the last character, etc.
It can be handy to iterate through a string using range(0, len(str) - 1)    
'char'.join(list) throws all the elements of a list of strings together, separating them with char
"""