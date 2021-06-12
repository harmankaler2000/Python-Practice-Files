#iterating over a list
print("List iteration: ")
l = ['A','B','C','D']
for i in l:
    print(i)

#iterating over tuple(immutable type)
print("Tuple iteration: ")
t = ('A','B','C','D')
for i in t:
    print(i)

#iterating over string
print("String iteration: ")
s = "Harman"
for i in s:
    print(i)

#iterating over dict
print("Dictionary iteration: ")
d = dict()
d['E'] = 123
d['F'] = 345
for i in d:
    print("%s %d"%(i, d[i]))