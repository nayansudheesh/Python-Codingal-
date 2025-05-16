def due():
    bill = int(input("Enter your bill"))
    bill_paid = int(input("Enter the amount of bill you have paid"))
    due = bill - bill_paid
    print("Due amount is:" , due)
due()