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


num_list = "432156789"
print(num_list [::-1])




# 0 => nothing
# 1 => ascending
# -1 => descending
# 2 => jump steps
# -2 => reverse (jump steps)

# print(mylist[0])



# common = []
# unique = []
# first = "I love football"
# second = "I dont love football"

# for i in second.split():
#     if i not in first.split():
#         unique.append(i)
#     else:
#         common.append(i)
    
# print(common)
# print(unique)    







# num = "988-8787-5444-1212"
# # output = "***-****-****-1212"

# def converter(num):
#     first_part = num.split("-")[:-1] # make them stars
#     second_part = num.split("-")[-1] # keep as it is
#     result = "" #to store the star
#     for i in first_part: # looping in list to make them stars
#         star = len(i) * "*" # converting length of number to stars
#         result = result + star + "-" # adding stars to the result variable 
#     return result + second_part #adding star and last number to return

# print(converter(num))    



numbers = [ "988-8787-5444-1212","7878-5454-8787-7878"]
# output = ["***-****-****-1212",  "****-****-****-7878"]
output = []


# def converter(number):
#     first_part = number.split("-")[:-1] 
#     second_part = number.split("-")[-1] 
#     result = "" 
#     for i in first_part: 
#         star = len(i) * "*" 
#         result = result + star + "-" 
#     return result + second_part 
    
# for i in numbers:
#     output.append(converter(i))

# print(output)





   
    
