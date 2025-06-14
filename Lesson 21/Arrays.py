import array as arr #importing array

num_array = arr.array('i', [ 3 , 2 , 4 , 3 ,6 ,3 , ])#original array
print("original array is:" , str(num_array))#printing
#no. of times 3 is repeated
print("Number of times 3 has been repeated in the array:" , num_array.count(3))
#reversing array
num_array.reverse()
print("Reverse of array is:")
print(num_array)