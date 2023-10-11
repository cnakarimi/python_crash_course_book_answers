def greet_user(username):
    if username is 'admin':
        print("Hello Admin! You're now operating with special rights")
    else:
        print("Hello " + username.title() + "! How are you doing today ?")


def greeting(usernames):
    if usernames:
        for username in usernames:
            greet_user(username)
    if len(usernames) == 0:
        print("We need to find some users!")


usernames = ["admin", "mehdi", "costumer", "guest", "sister"]
greeting(usernames)
usernames = []
greeting(usernames)
