y=int(input("enter a year:"))
if (y%4==0 and y%100 !=0) or (y%400==0):
    print("Leapyear")
else:
    print("Not a leap year")