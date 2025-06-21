#ACP , Tuple product , lesson 121.
tuple1 = (4,3,2,2,-1,18,1)# 1 extra as tuples need to be equal.
tuple2 = (2,4,8,8,3,2,9)

product = (tuple1[0]*tuple2[0],tuple1[1]*tuple2[1], tuple1[2]*tuple2[2] , tuple1[3]*tuple2[3] , tuple1[4]*tuple2[4] , tuple1[5]*tuple2[5], tuple1[-1] * tuple2[-1])
print("The product of tuples" , product)