#overloading equality and less than operator
class A:
    def __init__(self, a):
        self.a = a
    
    def __lt__(self, other):
        if(self.a < other.a):
            return "ob1 is less than ob2"
        else:
            return "ob2 is less than ob1"
    
    def __eq__(self, other):
        if self.a == other.a:
            return "Both are equal"
        else:
            return "Not equal"

obj1 = A(2)
obj2 = A(3)
obj3 = A(2)
print(obj1 < obj2)
print(obj1 == obj3)