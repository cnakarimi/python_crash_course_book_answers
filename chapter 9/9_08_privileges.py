class Privileges():
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        for priv in self.privileges:
            print(f'Admin privileges are : {priv}')


privileges = ['can add post', 'can delete post', 'can ban user']
ins = Privileges(privileges)
ins.show_privileges()
