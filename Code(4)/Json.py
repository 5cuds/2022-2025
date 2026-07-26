import json

# Test person
person = {"First-Name": "Bob", "Last-Name": "Dickerson", "Age": 21, "Job": "Google", "Has-Childen": True, "Childens": [{"Name": "Copper", "Age": 5}, {"Name": "Mary", "Age": 7}]}

Json_Person = json.dumps(person, indent=4, sort_keys=True) # you can also put separators=(":", "=") for seping

print(Json_Person)

with open ("JsonPerson.json", "w") as file_perosn:
    json.dump(Json_Person, file_perosn, indent=4)

with open ("person.json", "r") as person: # turn it back to a dict
    person = json.load(Json_Person)
    print(person)