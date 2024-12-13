
def greatest(a, b, c):
    if(a > b and a > c):
        return a;
    elif(b > a and b > c):
        return b;
    elif(c > a and c > b):
        return c;

num = greatest(44, 22, 11);
print("greatest number is: ", num);