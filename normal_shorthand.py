#cases when a += b is not equal to a = a + b

list1 = [5, 4, 3, 2, 1]
list2 = list1
#list2 also gets changes as they point to same position
#using a+=b
list1 += [1,2,3,4]
#both become the same
print(list1)
print(list2)

list3 = [5, 4, 3, 2, 1]
list4 = list3
list3 = list3 + [1,2,3,4]

#contents of list4 don't change as list1 becomes different
print(list3)
print(list4)