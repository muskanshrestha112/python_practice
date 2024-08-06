total_bill = 0

tip = 0
bill = input("Enter the total bill:")
tip = input("Enter the tip:")  
  
if tip == "10":
    total_bill = int (bill) + ((10/100) * int (bill))
elif tip == "20":
    total_bill = int (bill) + ((20/100) * int (bill))
print(f"the total bill = {total_bill}")
people = input("number of people:")
splitbill = int(total_bill) / int (people)
print(f"bill per person = {splitbill}")



    
        



  