#functions


#function definition
def avg():
    a = int(input("Enter a: "));
    b = int(input("Enter b: "));
    c = int(input("Enter c: "));
    average = (a + b + c)/3;
    print(average);

#function call
avg();
avg();
avg();
avg();


#function with argument
def goodDay(name):
    print("Good Day " + name);
    return "done"

a = goodDay("suraj");
print(a);



#recursion
def factorial(n):
    if(n == 1 or n == 0):
        return 1;
    return n * factorial(n-1);


n = int(input("Enter a number: "));
print(f"factorial of {n} is: {factorial(n)}");