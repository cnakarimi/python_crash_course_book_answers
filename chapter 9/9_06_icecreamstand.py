class Restaurant():

    def __init__(self,
                 restaurant_name,
                 cuisine_type,
                 number_served=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.open = False
        self.number_served = number_served

    def describe_restaurant(self):
        print('Name: ', self.restaurant_name)
        print('type : ', self.cuisine_type)
        print('number served : ', self.number_served)

    def open_resturant(self):
        self.open = True
        print('restaurant is open now!')

    def set_number_served(self, new_numb):
        self.number_served = new_numb

    def increament_number_served(self):
        self.number_served += 1


class Ice_Cream(Restaurant):
    def __init__(self, name, cuisine_type, flavors):
        super().__init__(name, cuisine_type)
        self.flavors = flavors

    def available_flavors(self):
        for flavors in self.flavors:
            print(f'Available flavors are: {flavors.title()}')


flavors = ['vanilla', 'chocolate', 'melon']
ins = Ice_Cream('Ice Cream stand', 'Ice_cream', flavors)
ins.describe_restaurant()
ins.available_flavors()
