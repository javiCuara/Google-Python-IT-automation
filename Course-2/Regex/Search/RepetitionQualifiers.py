#!/bin/env python3

import re
'''
This functions checks if the text passed includes the letter 'a' upper or lower
at least twice!
'''
def repeating_letter_a(text):
    result = re.search(r"(.*[aA]){2}", text)
    return result != None

'''
BREAKDOWN:
    ()  : make scope for matching any text that inxludes consecutive a or A
    .   : any characters can be in between the 'a/A' 
    *   : indicates 0 or more occurences of the provided characters
    {}  : limit the proceeding to at least 2
'''
print(repeating_letter_a("banana")) # True
print(repeating_letter_a("pineapple")) # False
print(repeating_letter_a("Animal Kingdom")) # True
print(repeating_letter_a("A is for apple")) # True
print(repeating_letter_a("A cat above air")) 
