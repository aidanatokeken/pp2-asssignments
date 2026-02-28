#1
import json
person = {"name": "Ayan", "age": 18, "city": "Almaty"}
person_json = json.dumps(person)
print(person_json)      #{"name": "Ayan", "age": 18, "city": "Almaty"}

#2
import json
json_data = '{"name": "Dana", "age": 17, "city": "Astana"}'
data = json.loads(json_data)
print(data["name"])      #Dana

#3
import json
data = {"name": "Alina", "score": 95}
with open("data.json", "w") as file:
    json.dump(data, file)

#4
import json
with open("data.json", "r") as file:
    data = json.load(file)
print(data)

#5
import json

x = {
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

print(json.dumps(x))