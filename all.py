#using all(iterables)
#returns True if all of the value in the iterable is True and if 
# finds False it stops
#looking for anymore in the iterable and returns False

print(all([True, True, True, True]))

print(all([False, True, False, False]))

print(all([False, False, False]))