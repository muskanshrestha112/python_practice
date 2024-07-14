# String list
str_list = ['ram','devi','tarun','muskan']
int_list = [1, 2, 3, 4, 5]
boolean_list = [True, False]
mix_list = ['ram', 1, True]
# print(type(str_list))
# print(str_list[2])
# print(int_list[-3])
# print(str_list)
# for name in str_list: 
#     print(name)
# for num in int_list:
#     print(num)

# print(len(str_list))
# str_list.append('anjila')   
# str_list.insert(0,'anjila')   
# str_list.remove('devi')
# str_list.pop(1) 

# str_list.pop()   
# str_list = []
str_list.extend(boolean_list)         
print(str_list[:3:-1])

