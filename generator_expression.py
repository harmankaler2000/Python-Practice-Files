generator = (num ** 2 for num in range(10))

for num in generator:
    print(num)

string = 'Harman'
li = list(string[i] for i in range(len(string) -1, -1, -1))
print(li)