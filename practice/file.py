
# f = open("num.txt","r")
# number = f.read()
# # print(number)

# # output = []

def converter(number):
    for x in number:

        first_part = number.split("-")[:-1] 
        second_part = number.split("-")[-1] 
        result = "" 
        for i in first_part: 
            star = len(i) * "*" 
            result = result + star + "-" 
        return result + second_part 


print(converter(number))
    
# # for i in number:
# #     output.append(converter(i))
# # print(output)


# f = open("num.txt","w")
# f.write(number)
# f.close()


# f = open("num.txt","r")
# print(f.read())

# Read files
file = open('num.txt')
data_list = file.readlines()
file.close()

# Convert numbers to stars and store then to new_data
new_data = []
for i in data_list:
    new_data.append(converter(i))  # i: aauta number linxa => converter: Convert => new_data.append: Append to new_data
    
file = open('num.txt', 'w')
    
for i in new_data:    
    file.writelines(i)

file.close()
