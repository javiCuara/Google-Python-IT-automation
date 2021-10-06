#!/bin/env python3

import re

def check_aei(text):
    '''
    The function check_aei returns true if the submitted text contains the vowels a,e,i,
    with exactly one occurence of any other charater in betweeen
    ''' 
    result =  re.search(r"a.e.i",text)
    return result != None


print(check_aei("academia")) # T
print(check_aei("aerial")) # F
print(check_aei("paramedic")) # T
