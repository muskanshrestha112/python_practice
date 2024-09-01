
f = open("num.txt","r")
number = f.read()
# print(number)

# output = []

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
    
# for i in number:
#     output.append(converter(i))
# print(output)


f = open("num.txt","w")
f.write(number)
f.close()


f = open("num.txt","r")
print(f.read())


