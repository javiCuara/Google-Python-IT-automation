#!/bin/env python3

import re
def check_sentence(text):
      result = re.search(r"^[A-Z][\w\s].*[.!?]$", text)
      return result != None
'''
Solution:
    ^       : the begging must match the following
    [A-Z]   : A capital letter
    [\w\s]  : It can be followed up by any other letters upper or lower or by a space
    .       : It call be followed up with anything
    *       : But must match the following paramater
    [?!.]$   : Must contain some form of punctuation at the end
'''


print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True
