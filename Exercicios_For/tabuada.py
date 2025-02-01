# # Tabuada  

number = int(input('Tabuada de qual numero o senhor de seja ? '))
print("{:^40}".format("Tabuada de {} ".format (number)))
for aux in range(1,10+1):
    print("{} x {} = {} ".format(number,aux,number*aux))


