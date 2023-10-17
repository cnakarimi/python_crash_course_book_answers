person_one = {'first_name': 'sina', 'last_name': 'karimi',
              'age': '23', 'city': 'tehran', }

person_two = {'first_name': 'mohsen', 'last_name': 'sadeqi',
              'age': '32', 'city': 'tabriz', }

person_three = {'first_name': 'sadeq', 'last_name': 'mohammadi',
                'age': '29', 'city': 'neyshaboor', }

people = [person_one, person_two, person_three]

for person in people:
    print(f"his name is {person['first_name'].title()}")
    print(f"his last name is {person['last_name'].title()}")
    print(f"his age is {person['age']}")
    print(f"he lives in {person['city'].title()}")
    print('-' * 10)
