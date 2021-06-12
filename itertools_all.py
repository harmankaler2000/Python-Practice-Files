#infinite iterators
import itertools
import operator
#count
for i in itertools.count(5, 5):
    if i == 35:
        break
    else:
        print(i , end = " ")

#cycle
count = 0
for i in itertools.cycle('AB'):
    if count > 7:
        break
    else:
        print(i, end=" ")
        count+=1

#using next function
l = ['A', 'B','C','D']
iterators = itertools.cycle(l)
for i in range(6):
    print(next(iterators), end=" ")

#repeat
print("Printing the numbers repeatedly: ")
print(list(itertools.repeat(25, 4)))

#product function
print("cartesian product using repeat: ")
print(list(itertools.product([1,2],repeat=2)))

print("The cartesian product of the containers:") 
print(list(itertools.product(['geeks', 'for', 'geeks'], '2'))) 

print("The cartesian product of the containers:") 
print(list(itertools.product('AB', [3, 4])))

#permutations
print ("All the permutations of the given list is:")  
print (list(itertools.permutations([1, 'geeks'], 2))) 

print ("All the permutations of the given string is:")  
print (list(itertools.permutations('AB'))) 
    
print ("All the permutations of the given container is:")  
print(list(itertools.permutations(range(3), 2)))

#combinations
print ("All the combination of list in sorted order(without replacement) is:")  
print(list(itertools.combinations(['A', 2], 2))) 
    
print ("All the combination of string in sorted order(without replacement) is:") 
print(list(itertools.combinations('AB', 2))) 
    
print ("All the combination of list in sorted order(without replacement) is:") 
print(list(itertools.combinations(range(2), 1))) 

#combinations_with_replacement
print ("All the combination of string in sorted order(with replacement) is:") 
print(list(itertools.combinations_with_replacement("AB", 2))) 
    
print ("All the combination of list in sorted order(with replacement) is:") 
print(list(itertools.combinations_with_replacement([1, 2], 2))) 
    
print ("All the combination of container in sorted order(with replacement) is:") 
print(list(itertools.combinations_with_replacement(range(2), 1)))

li1 = [1, 4, 5, 7] 
    
# using accumulate() 
# prints the successive summation of elements 
print ("The sum after each iteration is : ", end ="") 
print (list(itertools.accumulate(li1))) 
    
# using accumulate() 
# prints the successive multiplication of elements 
print ("The product after each iteration is : ", end ="") 
print (list(itertools.accumulate(li1, operator.mul))) 
    
# using accumulate() 
# prints the successive summation of elements 
print ("The sum after each iteration is : ", end ="") 
print (list(itertools.accumulate(li1))) 
    
# using accumulate() 
# prints the successive multiplication of elements 
print ("The product after each iteration is : ", end ="") 
print (list(itertools.accumulate(li1, operator.mul))) 

li1 = [1, 4, 5, 7] 
li2 = [1, 6, 5, 9]  
li3 = [8, 10, 5, 4]
  
# using chain() to print all elements of lists 
print ("All values in mentioned chain are : ", end ="") 
print (list(itertools.chain(li1, li2, li3))) 

li4 = [li1, li2, li3] 
  
# using chain.from_iterable() to print all elements of lists 
print ("All values in mentioned chain are : ", end ="") 
print (list(itertools.chain.from_iterable(li4)))

#compress
print ("The compressed values in string are : ", end ="") 
print (list(itertools.compress('absdfghctvhiy', [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0])))

#dropwhile
li = [2, 4, 5, 7, 8] 
    
# using dropwhile() to start displaying after condition is false 
print ("The values after condition returns false : ", end ="") 
print (list(itertools.dropwhile(lambda x : x % 2 == 0, li))) 

#filterfalse
# using filterfalse() to print false values 
print ("The values that return false to function are : ", end ="") 
print (list(itertools.filterfalse(lambda x : x % 2 == 0, li))) 

#islice
print ("The sliced list values are : ", end ="") 
print (list(itertools.islice(li, 1, 6, 2))) 

#starmap
li = [ (1, 10, 5), (8, 4, 1), (5, 4, 9), (11, 10, 1) ] 
    
# using starmap() for selection value acc. to function 
# selects min of all tuple values 
print ("The values acc. to function are : ", end ="") 
print (list(itertools.starmap(min, li))) 

#takewhile
li = [2, 4, 6, 7, 8, 10, 20] 
    
# using takewhile() to print values till condition is false. 
print ("The list values till 1st false value are : ", end ="") 
print (list(itertools.takewhile(lambda x : x % 2 == 0, li )))

#tee
iti = iter(li)  
    
# using tee() to make a list of iterators 
# makes list of 3 iterators having same values. 
it = itertools.tee(iti, 3) 
    
# printing the values of iterators 
print ("The iterators are : ") 
for i in range (0, 3): 
    print (list(it[i])) 

#zip_longest()
print ("The combined values of iterables is  : ") 
print (*(itertools.zip_longest('GesoGes', 'ekfrek', fillvalue ='_' ))) 