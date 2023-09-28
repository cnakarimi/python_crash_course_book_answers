def print_invitation(guest_list):
    for guest in guest_list:
        print("Hello " + guest + ". I would like to invite you to dinner.")


guest_list = ['Sadeq', 'Erfan', 'Setareh']
print_invitation(guest_list)
print("Oh no! Setareh was enslaved by the Epaphroditus. He can't come to diner!")
guest_list.remove('Setareh')
guest_list.append('Soheil')
print_invitation(guest_list)
