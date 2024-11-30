a = int(input("enter 1st no: "))
b = int(input("enter 2nd no: "))
c = int(input("enter 3rd no: "))
d = int(input("enter 4th no: "))

if(a > b and a > c and a > d):
    print("a is the greatest number")
elif(b > a and b > c and b > d):
    print("b is the greatest number")
elif(c > a and c > b and c > d):
    print("c is the greatest number")
else:
    print("d is the greatest number")
