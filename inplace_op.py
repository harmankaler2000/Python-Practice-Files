#for inplace operator we will use the functions defined in operator module
import operator

#iadd()
x = operator.iadd(2, 3)
print("iadd: ", x)

#iconcat()
y = "Hello "
z = "World!"
y = operator.iconcat(y, z)
print("iconcat: ", y)

#isub()
x = operator.isub(2, 3)
print("isub: ",x)

#imul()
x = operator.imul(2, 3)
print("imul: ", x)

#itruediv()
x = operator.itruediv(6, 4)
print("itruediv: ", x)

#imod()
x = operator.imod(6, 4)
print("imod: ", x)

#ipow()
x = operator.ipow(2, 3)
print("ipow: ",x)

#ixor()
x = operator.ixor(10, 5)
print("ixor: ", x)

#iand
x = operator.iand(10, 5)
print("iand: ", x)

#ior
x = operator.ior(5, 4)
print("ior: ", x)

#ilshift()
x = operator.ilshift(8, 2)
print("ilshift: ", x)

#irshift
x = operator.irshift(8, 2)
print("irshift: ", x)
