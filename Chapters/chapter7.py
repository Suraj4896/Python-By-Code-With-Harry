#while loop
i = 0;
while(i < 5):
    print(i);
    i += 1;



#for loop
name = ["suraj", "rupa", "kanha", "butu"];
for i in name:
    print(i);

j = 0;
while(j < len(name)):
    print(name[j]);
    j += 1;


#range function
for i in range(8):
    print(i);

#steps after increment of 4
for i in range(0, 50, 4):
    print(i);

#for loop in tuple
t = (23, 45, 67,89);
for i in t:
    print(i);

#for with else
l= [1,7,8]
for item in l:
    print(item)
else:
    print("done") 


#break
for i in range (0,80):
    print(i) # this will print 0,1,2 and 3
    if i==3:
        break

#continue
for i in range(4):
    print("printing")
    if i == 2: # if i is 2, the iteration is skipped
        continue
    print(i)

#pass
l = [1,7,8]
for item in l:
    pass        # without pass, the program will throw an error