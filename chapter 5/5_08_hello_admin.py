usernames = ["admin", "mehdi", "costumer", "guest", "sister"]


def greeting_message(username):
    if username == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username}, thank you for logging in again")


greeting_message(usernames[0])
greeting_message(usernames[2])
