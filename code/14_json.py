import json 

x =  '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)#from string to json
print(y["age"]) 

# ===========================
x1 = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
y1 = json.dumps(x1)#from Python object to json
print(y1) 
# ===========================





x2 = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x2))
print(json.dumps(x2, indent=4))# use four indents to make it easier to read the result:
print(json.dumps(x2, indent=4, separators=(". ", " = ")))#default value is (", ", ": "),you can use . and a space to separate objects, and a space, a = and a space to separate keys from their values:
print(json.dumps(x2, indent=4, sort_keys=True))# sort the result alphabetically by keys:









# ===========================
# Convert Python objects into JSON strings
# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))
# ===========================