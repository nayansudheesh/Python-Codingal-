s1 = [ 1 , 2 ,4 ,5]
s2 = ['a' , 'b' , 'c' , 'd' , 'e']
s3 = zip(s1,s2)
print(s3)

list1 = [100 , 300 , 400 , 600]
list2 = [10 , 30 , 60 , 70]
for x,y in zip(list1 , list2[::-1]):
    print(x , y)

stocks = ['tcs' , 'infosys' , 'reliance']
prices = [42517 , 67531 , 32178]

new_dict = {stocks:prices for stocks, prices in zip(stocks,prices)}
print('/n{}'.format(new_dict))
