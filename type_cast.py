#convert one datatype to another
x = 1
y = 2.0
z = "3"

print(x, y, z, sep="\n")
#type casting
print(x, int(y), int(z), sep="\n")
#or for permanent replacement do reassignment
#y = int(y)
print(float(x), (y), float(z), sep="\n")
print(str(x), str(y), (z), sep="\n")

#implicit type conversions

a = 10
print("a is of type: ", type(a))
b = 10.6
print("b is of type: ", type(b))
#changed to float
a = a + b
print("a is of type: ", type(a))

#explicit type conversion
s = "10010"
c = int(s, 2)
print("After converting to integer base 2: ", end=" ")
print(c)
#printing string converting to float
e = float(s)
print ("After converting to float : ", end="")
print (e)

s = '4'
#printing character converting to integer
c = ord(s)
print("After converting char to int: ")
print(c)

#int to hex string
c = hex(56)
print("converting 56 to hex str: ")
print(c)

#int to octal string
c = oct(56)
print("converting 56 to octal string: ")
print(c)

s = 'harman'
c = tuple(s)
print('string to tuple: ')
print(c)

#string to set
c = set(s)
print('string set')
print(c)

#string list
print('string to list')
print(c)

p = 1
q = 2
tup = (('a', 1), ('f', 2),('g', 3))

#convert int to complex number
c = complex(1, 2)
print("converting int to complex: ")
print(c)

#int to string
c = str(a)
print('int to string: ')
print(c)

#tuple to expression dict
c = dict(tup)
print('convert tuple to dict: ')
print(c)

#convert int to ascii
m = chr(76)
n = chr(77)

print(m)
print(n)

#string object
s = 'Harman'

#byte object
u = b'Harman'

#encode string to ascii mapping
d = s.encode('ASCII')

#check if a is converted to bytes or not
if(d == u):
    print("Encoding successful")
else:
    print("Encoding unsuccessful")

#decoding to convert a byte object to string
#a byte string can be decoded back into a char string
d= u.decode('ASCII')

if d == s:
    print('Decoding successful')
else:
    print("Decoding unduccessful")

#swap variables without using temp variables
var1 = 10
var2 = 20
print(var1, var2)
var1, var2 = var2, var1
print(var1, var2)