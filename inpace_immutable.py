import operator

#using immutable targets
i1 = 5
i2 = 6
n1 = 5
n2 = 6

#using add
z = operator.add(n1, n2)
print("Value using normal operator: ", z)
print("Value of first argument of normal operator: ", n1)
#using iadd
p = operator.iadd(i1, i2)

#produces same result
print("Value after inplace operator: ", p)
print("Value of first argument of inplace operator: ", i1)

#using mutable targets
li = [1,2,4,5]
#using add
x = operator.add(li, [1,2,3])
print("Value using normal operator: ", x)
print("Value of first argument of normal operator: ", li)
#using iadd
y = operator.iadd(li, [1,2,3])

#produces different result
print("Value after inplace operator: ", y)
print("Value of first argument of inplace operator: ", li)