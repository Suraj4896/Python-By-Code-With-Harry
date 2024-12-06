n = int(input("Enter a number: "))

#for loop
sum = 0;
for i in range(1, n+1):
    sum += i;

print(f"sum of {n} natural numbers: ", sum);

#while loop
j = 1;
sum2 = 0;
while(j <= n):
    sum2 += j;
    j += 1;

print(f"sum of {n} natural numbers: ", sum2);

