import requests
import json


url = "https://raw.githubusercontent.com/benoitvallon/100-best-books/master/books.json"
response = requests.get(url)
data = response.json()
# print(data)


countrylist = []

for i in data:
    if i["country"] not in countrylist:
        countrylist.append(i["country"])

print(countrylist)    





    

# for a in countrylist:
#     # print(a)

    
















# contree = json.loads('a')
# a = json.dumps(data['country'])
# print(contree)



# keys = ['country']
# contree = {x:data[1][2] for x in keys}
# print(contree)

# for a in data:
#     print(a)




# with open('data.json') as f: 
#     data = json.load(f) 

# if "country" in data:
#     data = json.dumps(data)
#     print(data)








    
