#using any(iterables)
#returns if any of the value in the iterable is true and stops
#looking for anymore in the iterable


#False is returned as all are false
print(any([False, False, False, False]))

#here it will return True as soon as it reaches the second index
print(any([False, True, False, False]))

#it will short-circuit at the first(True) and will return True
print(any([True, False, False, False]))