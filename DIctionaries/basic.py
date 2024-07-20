from collections import OrderedDict

ages = {
    "Peter": 10,
    "Isabel": 11,
    "Anna": 9,
    "Thomas": 10,
    "Bob": 10,
    "Joseph": 11,
    "Maria": 12,
    "Gabriel": 10,
}


print(ages["Anna"])

for key, value in ages.items():
    print(f"{key} is {value} years old")

for key in ages:
    print(key)

for item in ages.keys():
    print(item + "is awesome")

for value in ages.values():
    print(value)

students = {
    "Peter": {"age": 10, "address": "Lisbon"},
    "Isabel": {"age": 11, "address": "Sesimbra"},
    "Anna": {"age": 9, "address": "Lisbon"},
}

print(students["Peter"]["age"])

for student_name, student_info in students.items():
    print("\nPerson Name:", student_name)
    for attribute, value in student_info.items():
        print(f"{attribute}: {value}")