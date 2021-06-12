#any in practical example
list1 = []
list2 = []

#index ranges from 1 to 10 to multiply
for i in range(1, 11):
    list1.append(4 * i)

#index to access the list2 is from 0 to 9
for i in range(0,10):
    list2.append(list1[i] % 5 == 0)

print("See whether at least one number is divisible by 5 in list 1=> ")
print(any(list2))