car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.keys()
y = car.values()
z = car.items()

print(x)
print(y)
print(z)

car["color"] = "white"
print(x)
print(y)
print(z)