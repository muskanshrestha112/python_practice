string_one = ["I love football "]
string_two = ["I don't love football"]
string_three =[]

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
for a in string_one:
    if a not in string_two:
        if a not in string_three:
            string_three.append(a)                         
print(string_three)


#output
for a in string_two:
    if a not in string_one:
        if a not in string_three:
            string_three.append(a)                         
print(string_three)


 

 #output
for i in string_two :
    string_one.append(i)
    print(string_one)

for i in string_two :
    string_one.append(i)
    print(i)



# list(set(string_one).union(set(string_two)))
# print(list)