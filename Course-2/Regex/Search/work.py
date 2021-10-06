#!/bin/env python3

import re

def contains_acronym(text):
  '''
  Using escape chracters
  \( matches the first paraenthesis
  (.*) matches anything that is inside the parenthesis
  \) match closing parenthesis
  '''
  pattern = r"\((.*)\)" 

  result = re.search(pattern, text)
  return result != None



# print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
# print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
# print(contains_acronym("Please do NOT enter without permission!")) # False
# print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
# print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True

# import re
def check_time(text):

  '''
  Solution:
  {1-12} : {00-59} [am|pm]
  No leading zero
  ^((?!0)[1-9]|1[0-2]) This should result in a numer that ranges fron 1-9 or 10-12 
                      : colon must be here
                        ([0-5]\d) minutes dont go over 59 so we limit the first 
                                 \s* 0 or more spces allowed
                                    ((?i)) case insensitve
                                          (am|pm)$) the respective words must be at the end of the string 
  '''
  pattern = r"^((?!0)[1-9]|1[0-2]):[0-5]\d\s*((?i)(am|pm)$)"
  result = re.search(pattern, text)
  return result != None

# print(check_time("12:45Pm")) # True
# print(check_time("01:45pm")) # True
# print(check_time("9:59 am")) # True
# print(check_time("6:60am")) # False
# print(check_time("five o'clock")) # False

# import re
def contains_acronym(text):
  pattern = r"" 
  result = re.search(pattern, text)
  return result != None

# print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
# print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
# print(contains_acronym("Please do NOT enter without permission!")) # False
# print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
# print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True
