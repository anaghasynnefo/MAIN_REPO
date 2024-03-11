import re
username=str(input("ENTER YOUR USERNAME      :"))
def validate(email):

 terms ="^[a-zA-Z0-9\w]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+$"
 if re.match(username,terms,email):
  print("validate")
 else:
    print("not validate")





                                                       