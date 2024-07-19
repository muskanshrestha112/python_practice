import random
num = random.randint(0,30)
guess = 0
i = 0
while i < 3 :    
    guess = int(input("Enter a number:"))
    if guess > 30:
        print('Input number less then 30 ')
        break
    if (guess < num):
         print("Pick higher number!")
    elif (guess > num):
        print("Pick lower number!")
    else:         
        print("Congrats!!!You have guessed the right number.") 
    i += 1
    print(f"You have {3 - i} guess left")




# while guess != num  : 