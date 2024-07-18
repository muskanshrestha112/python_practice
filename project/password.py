import random

Characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%&*"
length = 8
amount = 1
for x in range(amount):
    password = "".join(random.sample(Characters,length))
    print(password)

# a = ''
# for i in range(1,6):
#     a = ''.join(i)
# print(a)    
