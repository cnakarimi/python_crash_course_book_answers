def make_shirt(size, message='I love python'):
    print('size of the shirt:', size)
    print('message in the shirt:', message)


tshirt_size = 'medium'
make_shirt(tshirt_size)

tshirt_size = 'large'
make_shirt(tshirt_size)

tshirt_message = 'Just do it'
make_shirt(tshirt_size, tshirt_message)
