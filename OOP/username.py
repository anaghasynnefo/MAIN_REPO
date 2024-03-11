# import re
# username=str(input("ENTER YOUR USERNAME      :"))

# def validate_username(username):

#   terms ="^[a-zA-Z]{3,25}$"

""""""""""""""""""

import re 
# day=int(input("ENTER THE DATE :     "))
terms= "^([012]\d|3[01])(-|.|/)([0]\d|1[012])(-|.|/)(\d{4}(\b(?:0*([1-9][0-9]*))\b)$"
x=re.search(terms,"10/10/2000")
if x:
  print("validate")
else:
    print("not validate")


""""""""


