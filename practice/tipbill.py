
tip = 0
bill = input("Enter the total bill:")
tip = input("Enter the tip:")  
  
if tip == 10:
    tip += 10
    bill = float(bill) + ((tip/100) * float (bill))
elif tip == 20:
    tip += 20
    bill = float(bill) + ((tip/100) * float (bill))
    print(bill)
people = input("number of people:")
splitbill = float(bill) / float (people)
print(splitbill)



    
        



  