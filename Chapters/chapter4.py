#lists are mutable in python
list = [12, 23, "suraj", True, 64, 3, False]
print(list)
list.insert(3, "555")
print(list)

l1 = [23, 56, 32, 2, 45, 34, 78, 5, 13]
# l1.sort()
print(l1)
l1.reverse()
print(l1)
print(l1.pop(2))
print(l1)     

#tuple
#immutable
a = (1,2,3,"kanha","rupa", True, False)
print(type(a))
no = a.count(3)
print(no)
print(a.index(2))