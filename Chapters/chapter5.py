#dictionary
marks = {
    "suraj": 98,
    "Ram": 88,
    "Butu": 89,
    "Rupa": 100
}

# print(marks, type(marks))
# print(marks["Butu"])
# print(marks.items())
# print(marks.keys())
# print(marks.values())
# print(marks.update({"kanha": 500, "Butu": 67}))
# print(marks.items())

#set
s = {2, 3, 3, 5, 5, 56,45, "suraj"}
s.add(566)
s.remove(3)
print(s)

s1 = {7, 2, 4, 6, 5}
s2 = {2, 3, 4, 4}
print(s1.union(s2))
print(s1.intersection(s2))