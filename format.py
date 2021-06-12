# print integer and float value
print("Geeks : %2d, Portal : %5.2f" % (1, 05.333))
 
# print integer value
print("Total students : %3d, Boys : %2d" % (240, 120))
 
# print octal value
print("%7.3o" % (25))
 
# print exponential value
print("%10.3E" % (356.08977))

# using format() method
print('I love {} for "{}!"'.format('Geeks', 'Geeks'))
 
# using format() method and refering
# a position of the object
print('{0} and {1}'.format('Geeks', 'Portal'))
 
print('{1} and {0}'.format('Geeks', 'Portal'))
 
 
# the above formatting can also be done by using f-Strings
# Although, this features work only with python 3.6 or above.
 
print(f"I love {'Geeks'} for \"{'Geeks'}!\"")
 
# using format() method and refering
# a position of the object
print(f"{'Geeks'} and {'Portal'}")


cstr = "I love geeksforgeeks"
   
# Printing the center aligned 
# string with fillchr
print ("Center aligned string with fillchr: ")
print (cstr.center(40, '#'))
 
# Printing the left aligned 
# string with "-" padding 
print ("The left aligned string is : ")
print (cstr.ljust(40, '-'))
 
# Printing the right aligned string
# with "-" padding 
print ("The right aligned string is : ")
print (cstr.rjust(40, '-'))

#if you want to access same named variable inside a function of global scope use global keyword
def f():
    global s
    s = "ABC"
    print(s)
s ="python"
f()
print(s)