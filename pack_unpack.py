#*args
def fun(a, b, c, d):
    print(a, b, c, d)

my_list = [1, 2, 3, 4]

#gives error: too less arguments
#func(my_list)

#unpacking: all param passed as different values
fun(*my_list)

#the len(args) and no elements in the list should be same
'''
args = [0, 1, 4, 9]

def func(a,b,c):
    return a+b+c

func(*args) #unpacking gives as too many arguments
'''

#also works
print(range(*my_list))

#packing: when we don't know how many args to use in a function just 
# use *args which will pack all given values to a tuple
def mySum(*args):
    return sum(args)

print(mySum(1, 2, 3, 4, 5, 6, 7))
print(mySum(10, 20))

# **kwargs
#unpacking of dictionaries using **
# **d is equal to => b = 4 anf c = 10
def funct(a, b, c):
    print(a, b, c)

d = {'a':2, 'b':4, 'c':10}
funct(**d)

def funct1(**kwargs):
    #kwargs is a dict
    print(type(kwargs))
    #print the dict items
    for key in kwargs:
        print("%s = %s" % (key, kwargs[key]))

funct1(name="harman", id = '101', lang = 'python')