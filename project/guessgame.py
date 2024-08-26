import random

num = random.randint(0,10)
guess = int(input("Enter a num: "))
if guess > num:
    print(f" the number is lower !!!")
elif guess < num:
    print(f"tne number is greater !!!")    
elif guess == num:
    print("Congrats !!! you have guess the right number.")
        

