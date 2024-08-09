
def calculator(opr):
    cal = True
    value = 0


    while cal:
        num1 = int(input("enter the first num:"))
        num2 = int(input("enter the first num:"))
        if opr == '+':
            value = num1 + num2
            print(f"value:{value}")
        elif opr == '-' :
            value =  num1 - num2
            print(f"value:{value}")
        elif opr == '*' :   
            value = num1 * num2
            print(f"value:{value}")
        elif opr == '/':
            value = num1 / num2
            print(f"value:{value}")
        else:
            return("The operater is invalid")    
        ans = input("do you want to run the operation again")
        ans = ans.strip()
        if ans == 'no':
            cal = False
            
print(calculator('/'))        


