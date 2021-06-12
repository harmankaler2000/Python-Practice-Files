a, b = 10, 20
print("Basic ternary: ")
min = a if a < b else b
print(min)

print("Direct method by using tuples and dict and lambda: ")
print("using tuple for selecting as an item: ")
print((b, a) [a < b])

print("Use dict for selecting an item: ")
print({True: a, False: b}[a < b])

#lambda is more efficient than above two methods
#as we are sure that only one expression will be evaluated unlike
#in tuple and dictionary
print((lambda: b, lambda: a)[a<b]())

#using nested if else
a, b = 10, 20

print("Both are equal" if a == b else "a is greater than b" if a > b else "b is greater than a")