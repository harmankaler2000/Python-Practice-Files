def generator():
    yield 1
    yield 2
    yield 3

#generator function
def nextSquare():
    i = 1
    while True:
        yield i * i
        i += 1 #next execution resumes from this point

for value in generator():
    print(value)

#x is a generator object
x = generator()
  
# Iterating over the generator object using next
print(x.__next__()) 
print(x.__next__())
print(x.__next__())
#print(x.__next__()) #raises stopiteration error

for num in nextSquare():
    if num > 100:
        break
    print(num)