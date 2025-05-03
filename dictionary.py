# dictionary = a changeable, unordered collection of unique key: value pairs 
# fast because they use hashing, allow us to access a value quickly 

capitals = {
    "Russia": "Moscow",
    "England": "London",
    "Brazil": "Brasilia",
    "Portugal": "Lisbon"
}
capitals.update({"Germany":"Berlin"})
capitals.update({"Russia":"Las Vegas"})

capitals.pop("Russia")
capitals.clear()

print(capitals.get("Portugal"))
print(capitals.keys())
print(capitals.values())
print(capitals.items())

for key,value in capitals.items():
    print(key, value)