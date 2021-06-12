#overload binary operator + 

class A:
    def __init__(self, a):
        self.a = a
    
    #adding two objects
    def __add__(self, o):
        return self.a + o.a

obj1 = A(1)
obj2 = A(2)
obj3 = A("Harmandeep ")
obj4 = A(" Kaur")

print(obj1 + obj2)
print(obj3 + obj4)
# print(obj1 + obj4) error