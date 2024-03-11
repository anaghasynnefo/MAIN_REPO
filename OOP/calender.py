import re

day=str(input("ENTER THE DATE      :"))

def calendar(day):
 terms= "^([012]\d|3[01])(-|.|/)([0]\d|1[012])(-|.|/)(\d{4})$"
day=re.search("terms")
if day:
   day= day.groups()
   print("validate")
else:
    print("not validate")