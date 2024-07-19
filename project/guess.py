import random
from os import system as muskan


muskan('cls')
num = random.randint(0,10)
print(num)
i = 0
while i < 3 : 
    try:   
        guess = int(input("Enter a number:"))
    except Exception as e:
        print("Can only enter number !!!")
        print("ERROR",e)
        break
    if guess > 10:
        print('Input number less then 30 ')
        break
    if (guess < num):
         print("Pick higher number!")
    elif (guess > num):
        print("Pick lower number!")
    else:         
        print("Congrats!!!You have guessed the right number.") 
        break
    i += 1
    print(f"You have {3 - i} guess left")






# while guess != num  : 