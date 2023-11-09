from random import randint


class Dice():

    def __init__(self, side=6):
        self.side = side

    def roll_dice(self):
        print(randint(1, self.side))


six_side = Dice(6)
for i in range(10):
    six_side.roll_dice()
print('_'*10)


six_side = Dice(10)
for i in range(10):
    six_side.roll_dice()
print('_'*10)


six_side = Dice(20)
for i in range(10):
    six_side.roll_dice()
print('_'*10)
