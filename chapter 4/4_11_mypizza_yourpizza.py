my_pizzas = ["pepperoni", "vegtable", "roastbeef"]
friend_pizza = my_pizzas[:]
for pizza in my_pizzas:
    print(f"I love {pizza.title()} Pizza")

my_pizzas.append("mushroom")
friend_pizza.append("chicken")
print(f"my pizzas are: {my_pizzas} and my friend pizzas are: {friend_pizza}")
