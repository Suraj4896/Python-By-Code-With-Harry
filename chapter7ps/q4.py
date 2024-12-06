n = int(input("Enter a number: "))

i = 1
cntDiv = 0

while(i*i <= n):
    if n % i == 0:
        cntDiv += 1
        if n / i != i:
            cntDiv += 1
    i += 1

if cntDiv == 2:
    print(f"{n} is Prime number")
else:
    print(f"{n} is not a Prime number")