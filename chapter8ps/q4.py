def sumNaturalNum(n):
    if(n == 1):
        return 1;
    return n + sumNaturalNum(n-1);


n = int(input("enter a number: "));
ans = sumNaturalNum(n);
print(ans);