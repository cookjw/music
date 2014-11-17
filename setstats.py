
# Collect all set types; store as dictionary keys, with number of 
# occurences as values.

# Procedure:
# copy text in between brackets
# - start with copy mode off
# - scan each character in the file
# -- determine status of copy mode
# -- determine whether character is a bracket
# -- if character is a bracket, switch copy mode
# -- otherwise, do the action appropriate to copy mode status
# --- if off, do nothing
# --- if on, copy

from collections import Counter

f = open("webern_op5_no4_simultaneities.txt", 'r')

file = f.read()

copystring = ""

copy_mode = 0

def switch_copy_mode():
    global copy_mode
    copy_mode = (copy_mode + 1) %2

for character in file:
  if character in ["[", "]"]:
      if copy_mode:
          copystring += character + " "
      switch_copy_mode()
  if copy_mode:
      copystring += character

types = [item for item in copystring.split(' ') if item]

occurrences = Counter(types)

print occurrences






        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        