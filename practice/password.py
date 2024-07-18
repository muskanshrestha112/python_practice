import random

letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%&*"
length = 8
amount = 1
for x in range(amount):
    password = "".join(random.sample(letter,length))
    print(password)