L = [4 , 5, 1 , 2 ,9 , 7 , 10 , 8 ]
print(L , "was orginial list")
count = 0
for i in L:
    count += i
avg = count/len(L)
sum = count
print("Sum is:" , sum)
print("average(Mean) is:" , avg)

L.sort()

print("Smallest item in list is:",L[0])
print("Largest item in list is:", L[-1])