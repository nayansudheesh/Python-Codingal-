string = input("Enter any word")
char = input("Enter any letter")
i = 0
count = 0

while( i < len(string)):

    if(string[i] == char):
        count = count+1
    i = i + 1

print("The total num of times" , char , "Has occured:" , count)