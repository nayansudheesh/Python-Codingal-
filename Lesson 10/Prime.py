lower = int(input("Enter the lower range"))
upper = int(input("Enter the higher range"))
print("The range is:", lower , "-" , upper)

print("Prime numbers between" , lower , "and" , upper , "Are:")

for num in range(lower , upper +1):

    if num > 1:
        for i in range( 2 , num):
            if ( num % i) == 0:
                break
        else:
            print(num)