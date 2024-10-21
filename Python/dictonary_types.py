# dictionary
info = {
    "name": "sachin",
    "age": 30,
    "city": "delhi",
    "is_married": False, 
    "hobbies": ["cricket", "coding"],
    "address": {
        "street": "abc",
        "city": "delhi"
    }
}

print(info)
print(type(info))
print(info["name"], info["age"])
info['name'] = "Shekhar"
print(info)

# dictionary methods

# keys methods -- return all the keys
print(info.keys())

# values methods -- return all the values
print(info.values())

# items methods -- return all the items
print(info.items())

# copy methods -- return a copy of the dictionary
new_info = info.copy()
print(new_info)

# update methods -- update the dictionary
info.update({"city":"patna","age":"27"})
print(info)

# pop methods -- remove the item
info.pop("city")
print(info)

# clear methods -- clear the dictionary
# info.clear()
# print(info)

