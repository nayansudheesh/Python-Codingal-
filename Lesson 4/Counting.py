amount = int(input("Enter amount to withdraw"))
note_1 = (amount//100)
note_2 = (amount%100)//50
note_3 = (amount%100)%50//10
print("No. of  100 notes is:" , note_1)
print("No. of  50 notes is:" , note_2)
print("No. of  10 notes is:" , note_3)