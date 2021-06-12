#using split method
x, y = input("Enter two values").split()
print(x,y)

#multiple input mapping using map and list
x = list(map(int, input("Enter values").split()))

print(x)

#using list comprehension

x = [int(x) for x in input("Enter multiple value: ").split()]
print(x)