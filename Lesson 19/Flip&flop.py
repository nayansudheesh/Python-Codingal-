def palindrome(r):
    e = len(r) - 1
    s = 0
    while s<e:
        if(r[s] != r[e]):
            return False
        else:
            return True
r = (1 , 2 , 3 , 3 , 2 , 1)
   
if palindrome(r):
        print(r , "Is palindromic(Flip -flop)")
else:
        print(r , "Is not palindromic(not flip flop)")