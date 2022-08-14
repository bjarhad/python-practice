a=int(input("enter the a marks :"))
b=int(input("enter the b marks :"))

if a>=55 and b>=45:
    print("pass")
elif a>=45 and 55<=a and b>=55:
    print("pass")
elif a>=65 and b<=45:
    print("reappear")
else:
    print("failed")