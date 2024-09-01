a = [2, 2, 4, 1, 5, 5, 8]
# remove duplicate

print(list(set(a)))


b = []
for i in a:
    if i not in b:
        b.append(i)
print(b)        


# arrange in ascending order
# a.sort()
# print(a)

#arrange in descending order
# a.sort(reverse = True)
# print(a)

