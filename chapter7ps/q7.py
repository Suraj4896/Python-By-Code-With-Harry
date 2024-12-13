n = int(input("enter n: "));

for i in range(0,n):
    print(" " * (n-i), end="");
    print("*" * (2*i + 1));
    
