#fibonacci using for loop and generator function
def fib(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b , a + b

#generator object
x = fib(5)
print(x.__next__)
print(x.__next__)
print(x.__next__)
print(x.__next__)
print(x.__next__)
print(x.__next__)
print(x.__next__)
print(x.__next__)

print("Using for loop : ")
for i in fib(8):
    print(i)