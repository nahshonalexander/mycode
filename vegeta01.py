#!/usr/bin/env python3

## create a dictionary
vegeta = {"race": "saiyan", "weight": "56kg", "age": 732, "realitves": ["trunks", "future trucks", "dead trunks"],
        "rival": "Goku"}

 # add another key value pair
vegeta.update({"SS level": "4(gt)"})
#print the Keys
print(vegeta.keys())
#ask user what key they want
choice = input("choose a key  ")

#look inside dictornary to see if choice == key

if choice in vegeta:
    print("the value is:", vegeta[choice])
else:
    print('That key is not in the dictionary')
