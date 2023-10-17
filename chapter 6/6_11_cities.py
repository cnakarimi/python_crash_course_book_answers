madrid = {
    "name": "madrid",
    "country": "spain",
    "population": "3.223 million",
    "fact": "According to FIFA, Real Madrid FC is the world's most successful football club of the 20th Century."
}
athens = {
    "name": "athens",
    "country": "greece",
    "population": "3.154 million",
    "fact": "Athens is Europe's oldest capital"
}
birmingham = {
    "name": "birmingham",
    "country": "england",
    "population": "1.149 million",
    "fact": "Birmingham is a national leader in urban green spaces"
}
rotterdam = {
    "name": "rotterdam",
    "country": "nerthlands",
    "population": "0.623 million",
    "fact": "You can travel the city by water-taxi"}

copenhagen = {
    "name": "copenhagen",
    "country": "denmark",
    "population": "0.602 million",
    "fact": "Two of the oldest amusement parks in the world are in Copenhagen"}

cities = [madrid, athens, birmingham, rotterdam, copenhagen]

for city in cities:
    print(f"Name of the city is : {city['name']}")
    print(f"it's in : {city['country']}")
    print(f"the population is : {city['population']}")
    print(f"{city['fact']}")
    print("-" * 10)
