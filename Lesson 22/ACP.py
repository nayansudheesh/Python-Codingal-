#list comprehension ACP
num1 = [ 1 , 2 , 7 , 9]
num2 = [ 5 , 6 , 5 , 4]
result = map(lambda x , y: x+y , num1 , num2)
print("Sum of two lists:" ,list(result))

num = [ 3 , 6 , 7 , 8 , 10]
def cu(n):
    return n*n*n
cube = list(map(cu , num))
print("cube of numbers are:" , cube)