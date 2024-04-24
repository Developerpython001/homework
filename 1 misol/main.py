from collections import namedtuple

Person = namedtuple('Person', ['name', 'age', 'country'])

people_data = [
    Person(name='Stas', age=30, country='Russia'),
    Person(name='Alex', age=25, country='USA'),
    Person(name='Jet Lee', age=35, country='China')
]

for person in people_data:
    print(f"Name: {person.name}, Age: {person.age}, Country: {person.country}")
