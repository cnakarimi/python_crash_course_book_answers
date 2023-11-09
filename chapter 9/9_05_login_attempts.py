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
        self.login_attempts = 0

    def increament_login_attempts(self):
        self.login_attempts += 1

    def describe_user(self):
        print('First name : ', self.first_name.title())
        print('Last name : ', self.last_name.title())
        print('Login attempts : ', self.login_attempts)

    def greet(self):
        print('Hello ', self.first_name.title() + '' +
              self.last_name.title() + 'How are you doing?')

    def reset_login_attempts(self):
        self.login_attempts = 0


users = [User("patrick", "nieri"),
         ]

for u in users:
    u.increament_login_attempts()
    u.describe_user()

    u.increament_login_attempts()
    u.describe_user()

    u.increament_login_attempts()
    u.describe_user()

    u.increament_login_attempts()
    u.describe_user()

    u.increament_login_attempts()
    u.describe_user()

    u.reset_login_attempts()
    u.describe_user()
    u.greet()
