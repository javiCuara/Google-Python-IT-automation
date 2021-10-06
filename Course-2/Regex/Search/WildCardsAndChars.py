#!/bin/env python3

import re

def check_punctuation(txt):
    '''
    This function checks if the passed text contains punctuation symbols
    commas, periods, colons, semicolons, questions, and exclamation
    '''
    result = re.search(r"[!|,|.|;|:|?]",txt)
    return result != None


print(check_punctuation("This is a sentence that ends with a period.")) # True
print(check_punctuation("This is a sentence fragment without a period")) # False
print(check_punctuation("Aren't regular expressions awesome?")) # True
print(check_punctuation("Wow! We're really picking up some steam now!")) # True
print(check_punctuation("End of the line")) # False
