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


class Admin(User):
    def __init__(self, first_name, last_name, privileges, age='', password='', id='',):
        super().__init__(first_name, last_name)
        self.privileges = privileges

    def show_privileges(self):
        for priv in self.privileges:
            print(f'Admin privileges are : {priv}')


privileges = ['can add post', 'can delete post', 'can ban user']

ins = Admin('Lionel', 'Messi', privileges)
ins.describe_user()
ins.greet()
ins.show_privileges()
