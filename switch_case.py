#using dictionary mapping
def numbers_to_strings(arg):
    switch = {
        0 : "zero",
        1 : "one",
        2 : "two"
    }

    #get() method of dict data type returns value of passed
    #arg if it is present in dict otherwise second arg will
    #be assigned as default value of passed arg
    return switch.get(arg, "nothing")

arg = 0
print(numbers_to_strings(arg))
arg = 1
print(numbers_to_strings(arg))
arg = 5
print(numbers_to_strings(arg))