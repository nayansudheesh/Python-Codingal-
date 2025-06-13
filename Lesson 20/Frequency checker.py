test_dict ={'Codingal' : 2 , 'is': 2, 'Best': 2 , 'for': 2 , 'coding': 1}
print("Original dictionary is" , str(test_dict))
k =2 #initalising K(constant value)
res = 0
for key in test_dict:
    if test_dict[key] == k:
        res = res + 1
print("Frequency of K(2) is " , str(res))