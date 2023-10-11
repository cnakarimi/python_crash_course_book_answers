current_users = ["admin", "mehdi", "customer", "guest", "sister"]
new_users = ['Admin', 'mehdi', 'hossein', 'john', 'black knight', 'CUSTOMER']


def all_title():
    return [x.title() for x in current_users]


def all_upper():
    return [x.upper() for x in current_users]


current_users_title = all_title()
current_users_upper = all_upper()

for new_user in new_users:
    if new_user in current_users or new_user in current_users_title or new_user in current_users_upper:
        print("You need to enter new username")
    else:
        print("Your user name is availabel")
