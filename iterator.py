#user defined iterable type
class Test:
    def __init__(self, limit):
        self.limit = limit
    
    #creates an iterator object and called when iteration is initialized
    def __iter__(self):
        self.x = 10
        return self

    #to move to next element but in python 3, we replace the next with __next__
    def __next__(self):
        x = self.x
        
        #stop iteration if limit is reached
        if x > self.limit:
            raise StopIteration
        
        #else increment and return old value
        self.x = x + 1
        return x

#print from 10 to 15
for i in Test(15):
    print(i)

#prints nothing
for i in Test(5):
    print(i)
        
#iterators inbuilt
iterable_variable = 'Harmandeep'
iterable_object = iter(iterable_variable)

while True:
    try:
        #iterate using next()
        item = next(iterable_object)
        print(item)
    except StopIteration:
        #exception happens when iteration is over
        break
