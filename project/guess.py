import random
num = random.randint(0,100)
guess = 0 
while guess != num:
    guess = int(input("Enter a number:"))
    if (guess < num):
        print("Pick higher number!")
    elif (guess > num):
        print("Pick lower number!")
    else:
        print("Congrats!!!You have guessed the right number.")   
        break     

