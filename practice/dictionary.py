tiktak = {
    "keys": "values",
    "Name": "Muskan", 
    "Age": 20,
    "Address": "Maitidevi",
    "Love": "Tarun",
    "phone": 9854678900,
    "Sidechicks": ["Radhe", "Asmita", "Manju"]
    }

# first = {
#     "name" : "Ram",
#     "class" : 9
#         }

# second = {
#     "name" : "Sita",
#     "class" : 9
# }

# third = {
#     "name" : "lok",
#     "class" : 9
# }

# rank = {
#     "first" : first,
#     "second" : second,
#     "third" : third
# }

rank = {
    "first" : {
    "name" : "Ram",
    "class" : 9
},

    "second" : {
    "name" : "Sita",
    "class" : 9
},

    "third" : {
    "name" : "lok",
    "class" : 9
}
}


# print(rank["first"]["class"]) # individual item access
# print(rank["second"])

# loop in nested dict
# for x, obj in rank.items():
#     print(x)

#     for y in obj:
#         print(y + ':', obj[y])


# tiktak.update({"Age": 21}) # to update the values
# print(tiktak)

# tuktuk = tiktak.copy() # to make a copy of dic
# tuktuk = dict(tiktak)
# print(tuktuk)







# tiktak["hobbies"] = "dance" #add elements
# print(tiktak)


list1 = ["Name", "Age", "Address"]
list2 = ["Muskan", "twenty", "maitidevi"]
mylist = dict(zip(list1, list2))
print(mylist)
for x in mylist.items():
    print(x)





# mylist["list1"] = ["Name", "Age", "Address"]
# mylist["list2"] = ["Muskan", "twenty", "maitidevi"]
# print(mylist)



# print(set(list2))
# print(type(list1))


# {}{}[][[]]()
# for x in tiktak.values(): # to print values
    # print(x)

# for x in tiktak: # to print keys
#     print(x)

"""
for multiple paragraph commenting 
"""

# for x, y in tiktak.items():
#     print(x, y)



# del tiktak["phone"]
# print(tiktak)
# print(tiktak["Sidechicks"])


# print(tiktak.get("phone", "phone does not exsits"))

# if "phone" in tiktak:
#     print(tiktak["phone"])
# else:
#     print("Phone does not exists")




# # print(tiktak["Sidechicks"])
# print(tiktak["Sidechicks"][1])

# print(type(tiktak))
# print(tiktak["Age"])
# a = tiktak.keys()
# print(a)



# toktok = dict(name = "Tarun", age = 50, occupation = "my bf")
# print(toktok.keys())