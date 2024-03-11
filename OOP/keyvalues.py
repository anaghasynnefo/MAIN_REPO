a= int(input("enter the number"))
b=int(input("enter the divisor"))
try:
    print(a/b)

except:
    print("cant divisible by zero")
    a=int(input("enter the number"))
    b=int(input("enter the divisor"))
    print(a/b)