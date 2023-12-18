import json


def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    verifying = False
    if username:
        user_response = input(f"{username}, Is this your user name? \n")
        if user_response == 'yes':
            verifying = True
            print("Welcome back, " + username + "!")
        elif user_response == 'no':
            username = get_new_username()

    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")


greet_user()
