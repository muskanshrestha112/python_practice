
# my_list = [1, 2, 2, 45, 4, 654]

# # print(my_list)

# def linear_search(mylist, target):
#     for i in range(len(mylist)):
#         if my_list[i] == target:
#             return i
#     return "It doesnot exists in the list."

# print(linear_search(my_list, 2))





# for i in a.split():
#     output.append(i)

# print(output)


# def linear(a):
#     my_list = a.split()
#     for i in my_list:
#         return i
    
# # print(linear(a))
    
# for i in a:
#     output.append(i)
            
# print(output)



# def linear(a):
#     my_list = a.split()
#     return my_list
# output = linear(a)
# print(output)

a = "My name is Tarun"
# output = ['My', "name", "is", "Tarun"]
output = []


# def splt(a):
#     for i in a:
#         if i not in a:
#             output.append(i)        
    
# print(splt(a))



def my_split(data):
    output = [] #to contain all the data in the list 
    holder = "" # to hold the string to make a whole list element, My => list => empty
    for i in range(len(data)): # looping through all the index of string with range
        if data[i] == " " : # if a space occurs the condition is met 
            output.append(holder) # sending holders data to output list 
            holder = "" # holded data are reset to null
        else:
            holder = holder + data[i]
            if i + 1 == len(data): # list = 10 and i = 9 + 1 = 10 Finally, list == i
                output.append(holder)
            return output
            
        
print(my_split(a))