my_set = { 1 , 2 , 3}
print(my_set)

my_set2 = {1 , "Hello" , 2.1 , 3 , True}
print(my_set2)

myset3 = { 1 , 2 ,3 ,4 , 3 ,2} #set cannot have duplicates in output
#output is { 1 , 2 , 3 ,4 }

myset4 = set[1 , 2 ,3 ,4]# we can make sets from list (using cast of "set" keyword)
print(myset4 , )

#removing numbers
num_set= {0 , 1 , 2 , 3 , 4 , 6}

print("Original set:" , num_set)
num_set.pop()
print("Set with first item removed:" , num_set)
