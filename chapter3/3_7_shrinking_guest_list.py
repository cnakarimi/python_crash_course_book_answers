def print_invitation(guest_list):
    for guest in guest_list:
        print("Hello " + guest + ". I would like to invite you to dinner.")


guest_list = ['Sadeq', 'Erfan', 'Setareh']
print_invitation(guest_list)
print("Oh no! Setareh was enslaved by the Epaphroditus. He can't come to diner!")
guest_list.remove('Setareh')
guest_list.append('Soheil')
print_invitation(guest_list)
print("Found a bigger table! More guests!")
guest_list.insert(0, 'Kazem')
guest_list.insert(2, 'Ghasem')
guest_list.append('Kamran')
print_invitation(guest_list)
print("Sorry I can invite only two people for dinner")
deleted_guest = guest_list.pop()
print(f"Sorry I can't invite you for dinner {deleted_guest.title()}")
deleted_guest = guest_list.pop()
print(f"Sorry I can't invite you for dinner {deleted_guest.title()}")
deleted_guest = guest_list.pop()
print(f"Sorry I can't invite you for dinner {deleted_guest.title()}")
deleted_guest = guest_list.pop()
print(f"Sorry I can't invite you for dinner {deleted_guest.title()}")
for guest in guest_list:
    print(f"{guest.title()} you are still invited")
del guest_list[:]
print(f"this is my guest list: {guest_list}")
