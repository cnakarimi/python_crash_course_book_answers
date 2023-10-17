pet_one = {'name': 'puppet', 'type': 'dog', 'owner_name': 'jim'}
pet_one = {'name': 'nishi', 'type': 'cat', 'owner_name': 'serah'}
pet_one = {'name': 'sisi', 'type': 'bird', 'owner_name': 'kate'}

pets = [pet_one]

for pet in pets:
    print(
        f"pet's name is {pet['name'].title()} who is {pet['type'].title()} and it owner name is {pet['owner_name'].title()}")
