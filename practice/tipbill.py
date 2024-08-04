total_bill = 0

tip = 0
bill = input("Enter the total bill:")
tip = input("Enter the tip:")  
  
if tip == "10":
    total_bill = float(bill) + ((10/100) * float (bill))
elif tip == "20":
    total_bill = float(bill) + ((20/100) * float (bill))
print(total_bill)
people = input("number of people:")
splitbill = float(total_bill) / float (people)
print(splitbill)



    
        



  