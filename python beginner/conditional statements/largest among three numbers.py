a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a>=b and a>=c:
    print("largest is:",a)
elif b>=a and b>=c:
    print("largest is:",b)
else:
    print("largest is:",c)