#c-style strings
l = ['A','B','C','D']
i = 0

while i < len(l):
    print(l[i])
    i += 1

#for-in or foreach type loop
for i in l:
    print(i)

#enumerate
for i, x in enumerate(l):
    print(x)

#this also works for enumerate
for x in enumerate(l):
    print(x[0], x[1])

#return value of enumerate
print(enumerate(l))

#using two separate lists
cars = ["Aston", "Audi", "McLaren"]
accessories = ["GPS kit", "Car repair-tool kit"]

#single dict holds the prices fo cars and its accessories
#first three for cars and the next three for accessories
prices = {1:"570000$", 2:"68000$", 3:"450000$", 4:"8900$", 5:"4500$"}

for index,c in enumerate(cars, start=1):
    print("Car: %s Price: %s: "%(c, prices[index]))

for index, a in enumerate(accessories, start=1):
    # index+len(cars) as we need to skip the first price values of cars
    print("Accessory: %s Price: %s"%(a, prices[index + len(cars)]))

#zip
#combining lists and printing
for c, a in zip(cars, accessories):
    print("Car: %s, Accessory required: %s"%(c,a))

#unzip lists
l1,l2 = zip(*[('Aston','GPS'),
            ('Audi','Car Repair'),
            ('McLaren', 'Dolby sound kit')
            ])
#printing unzipped lists
print(l1)
print(l2)