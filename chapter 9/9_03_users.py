class User():
    def __init__(self,
                 first_name,
                 last_name,
                 age='',
                 password='',
                 id=''):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age,
        self.password = password,
        self.id = id

    def describe_user(self):
        print('First name : ', self.first_name.title())
        print('Last name : ', self.last_name.title())

    def greet(self):
        print('Hello ', self.first_name.title() + ' ' +
              self.last_name.title() + ' how are you doing?')


users = [User("patrick", "nieri"),
         User("rafael", "hardy"),
         User("olga", "schuyler")]

for u in users:
    u.describe_user()
    u.greet()
