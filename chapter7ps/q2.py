
#one way
l = ["Harry", "Soham", "Sachin", "Rahul"]

for i in l:
    if i[0] == 'S':
        print("Hello! ", i);


#2nd way
for name in l:
    if(name.startswith('S')):
        print(f"Hello {name}");