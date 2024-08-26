# a = "My name is Muskan"
# b = "tarun"
# c = "What are you doing?"

# print(c[13:18])
# print(c[-2:12:-1])

# print(b[::-1])

# temp = a[0:10]
# print(temp, b)
# print(a[3:7])


# mylist = ["ram", "sam", "muskan","neegan", "tarun"]

# for i in mylist:
#     print(f"Hello {i}, how are you?")


# num_list = "123456789"
# print(num_list [::1])




# 0 => nothing
# 1 => ascending
# -1 => descending
# 2 => jump steps
# -2 => reverse (jump steps)

# print(mylist[0])



common = []
unique = []
first = "I love football"
second = "I dont love football"

for i in second.split():
    if i not in first.split():
        unique.append(i)
    else:
        common.append(i)
    
print(common)
print(unique)    



# print(num.split("-"))