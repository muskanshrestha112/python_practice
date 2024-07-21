# practice_list = [1, 4, 7, 8, 9, 3, 6]
# nes_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# flatList = [j for i in nes_list for j in i if j % 2 == 0]
import copy


a = [1, 2, 3, 4, 5, 6]
b = a.copy()
b.append('muskan')
print(id(a))
print(id(b))
print(a)
print(b)


# print('Flat list',flatList)

# a = []
# for i in practice_list:
    # s = i*4
    # print(s)
    # if i % 2 == 0:
#     if i > 4:
#         a.append(i)

# print(a) 

# new_list = [i for i in practice_list if i % 2 == 0 ]
# print(new_list)



