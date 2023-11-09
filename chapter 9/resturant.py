class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.open = False

    def describe_restaurant(self):
        print('Name: ', self.restaurant_name)
        print('type : ', self.cuisine_type)

    def open_resturant(self):
        self.open = True
        print('restaurant is open now!')


ins1 = Restaurant("Happy Lotus", "Chinese")
ins2 = Restaurant("Dancing Sombrero", "Mexican")
ins3 = Restaurant("Feisty Pretzel", "German")

ins1.describe_restaurant()
ins1.open_resturant()
ins2.describe_restaurant()
ins3.describe_restaurant()
