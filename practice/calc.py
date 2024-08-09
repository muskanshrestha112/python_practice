num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the seconf number:"))

print("1) Add")
print("2) Sub")
print("3) Mul")
print("4) Div")

opr = (input("Choose an option from the above operation:"))

if opr == "1":
    opr = num1 + num2
    print(f"The sum = {opr}")
elif opr == "2":
    opr = num1 - num2
    print(f"The difference = {opr}")
elif opr == "3":
    opr = num1 * num2
    print(f"The product ={opr}")    
elif opr == "4":
    opr = num1 / num2
    print(f"The divident ={opr}")    
else : 
    print("The number is invalid")




