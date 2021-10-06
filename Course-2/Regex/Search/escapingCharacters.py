#!/bin/env python3
import re
def check_character_groups(text):
    result = re.search(r"\w+\s|\d", text)
    return result != None
'''
Using metacharacters we can complete this
/w  is used to find a word character
/s is used to find a whitespace chracter
/d is sused to find any digit

'''


print(check_character_groups("One")) # False
print(check_character_groups("123  Ready Set GO")) # True
print(check_character_groups("username user_01")) # True
print(check_character_groups("shopping_list: milk, bread, eggs.")) # False
