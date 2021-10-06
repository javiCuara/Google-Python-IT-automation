#!/bin/env python3

import re
# examples

#result = re.search(r"^(\w*),(\w*)$","Lovelace","ada")
#print(result)

# The following will print the touples 
#print(result.groups())

# we can also access these groups like any other touple
# mystring  = "{}{}".format(result[2],result[1])

'''
Repetition Qualifiers
How do we match a string of exactly five leters?

re.search(r"[a-zA-Z]{6}, Smaple Text whooa this is cool")

{5,} <- this means at least 5
{5,19} <- a range 5-19
{0,29} <- 0 to limit
'''

'''
Extracting a PID Using regexes

Some Exmaples of how to caputuer special characters

"\[" : using a backslash we express we want to match a opening bracket
"\]" : signifies we want to match the closing bracket

'''


def extract_pid(log_l):
    regex = r"\[(\d+)\]"
    result  = re.search(regex,log_l)
    if(result is None):
        return ""
    return result[1]

'''
SEARCH AND FIND ALL

re.split(r"[.?!]", "One scentence, Anther one? and the last one!")


re.sub(r"\w.%+-"+@[\w.]+", "[REDACTED]", 

'''