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


ins = Restaurant("Happy Lotus", "Chinese", 45)
ins.describe_restaurant()
ins.set_number_served(22)
ins.describe_restaurant()
ins.increament_number_served()
ins.describe_restaurant()
ins.increament_number_served()
ins.describe_restaurant()
