#various looping techniques
#enumerate()
print("Enumerate: ")
for key, value in enumerate(['A','B','C','D','E']):
    print(key)
    print(key, value)
    print(value)

#zip
print("Zip: ")
questions = ['name', 'color', 'shape']
answers = ['apple','red','circle']

for ques, ans in zip(questions, answers):
    print('What is your {0}? I am {1}'.format(ques, ans))

d = {'name':'Harman', 'age': 21}

#iteritems for dict key-value pair
#python 3 does not allow iteritems anymore
#it was removed only available in python 2
# print("Iteritems: ")
# for i,j in d.iteritems():
#     print(i, j)

print("items: ")
for i,j in d.items():
    print(i, j)

dic = {'A': 1, 'B': 2, 'C':3}

#using items
print("items: ")
for key, value in dic.items():
    print(key, value)

#using sorted()
l = [1,3,5,6,2,1,3]
print("sorted: ")
for i in sorted(l):
    print(i, end=" ")

#using sorted set
#sort the list and remove duplicate
print("sorted using set: ")
for i in sorted(set(l)):
    print(i, end=" ")

basket = ['guave', 'orange', 'apple', 'pear', 'guava', 'banana', 'grape']
#using sorted() and set()
print("sorted using set: ")
for fruit in sorted(set(basket)):
    print(fruit)

#using reversed print it in reversed
print("using reversed: ")
for i in reversed(l):
    print(i, end=" ")

#rversed over a range
for i in reversed(range(1, 10, 3)):
    print(i)