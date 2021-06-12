#else with for
for i in range(1, 4):
    print(i)
else:
    #executed as break is not used
    print("No break")

#else is not executed as there is break is used
for i in range(1, 4):
    print(i)
    break
else:
    #not executed as there is a break
    print("No Break")