n = int(input("enter a number: "));

i = 10;
while i >= 1:
    print(f"{n} X {i} = {n*i}");
    i = i-1;


#another way
n = int(input("enter a number: "));

for i in range(1, 11):
    print(f"{n} X {11-i} = {n*(11-i)}");