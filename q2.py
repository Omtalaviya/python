#2 print largest and smallest value of three
a=int(input("enter the first value"))
b=int(input("enter the second value"))
c=int(input("enter the third value"))
if a>b and a>c:
    print("first number is greater")
elif b>a and b>c:
    print("second number is greater")
else:
    print("third number is greater")
