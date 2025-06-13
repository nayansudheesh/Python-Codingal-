test_dict = { 'Age1': 6,'Age2': 12,'Age3': 8,'Age4': 6,'Age5': 12,}

print("Original dictionary:" , test_dict)
no = int(input("Which number to check frequency? (6 , 10 , 8 , 12)"))
res = 0
for key in test_dict:
    if test_dict[key] == no:
     res= res +1 
print("The frequency of" , no , "Is" , res)