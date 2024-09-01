# 

# a=string_one.split()
# b=string_two.split()
# a.extend(b)
# # print(set(a.extend(b)))
# print(set(a))


# for a in string_one.split():
#     if a in string_two.split():
#         string_three.append(a)
        
# print(string_three)

# for a in string_two.split():
#     if a not in string_one.split():
#         string_three.append(a)
        
# print(string_three)


# def common_string(string_one, string_two):
#     string_one = set(string_one)
#     string_two = set(string_two)
 
#     if (string_one & string_two ):
#         print(string_one & string_two)
#     else:
#         print("No common elements")


# def common_member(string_one, string_two):
#     result = [i for i in string_one if i in string_two]
#     return result

 
# print("The common elements in the two lists are: ")
# print(common_member(string_one, string_two))


# string_three = list(set(string_one)&set(string_two))
# print(string_three)



# s = set(string_one)
# list3 = [x for x in string_two if x not in s]
# print(list3)

#output 1
# for a in string_one:
#     if a not in string_two:
#         if a not in string_three:
#             string_three.append(a)                         
# print(string_three)


#output
# for a in string_two:
#     if a not in string_one:
#         if a not in string_three:
#             string_three.append(a)                         
# print(string_three)


 

#  #output
# for i in string_two :
#     string_one.append(i)
#     print(string_one)

# for i in string_two :
#     string_one.append(i)
#     print(i)



# list(set(string_one).union(set(string_two)))
# print(list)



# mylist=[2, 100, 2, 5, 1, 3, 55, 21, 69] 
# a=list(set(mylist))
# a.sort(reverse= True)
# a.reverse()
# a.sort()
# print(a[::-1]) #reverse 

# b=(1, 2, 3, 4)
# b.