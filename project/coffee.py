data = {
    "water" : 500,
    "caffine" : 100
}


order = input("Do you want a Coffee:")
if order == "yes":
    data["water"] = data["water"]-200
    data["caffine"] = data["caffine"]-50

print(data)
