# add data to a tuple thats turned into a list
appliances = ("oven", "refrigerator", "coffee maker", "rice cooker")


list_appliances = list(appliances)

print(list_appliances)

appliance_additions = ("blender", "food processor", "stove")

list_appliances.extend(appliance_additions)

print(list_appliances)

# add data to a tuple
appliances = ("oven", "refrigerator", "coffee maker", "rice cooker")

appliances = set(appliances)

appliances.update(["blender", "food processor", "stove"])

appliances = tuple(appliances)
print(appliances)
