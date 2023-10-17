favorite_places = {"serah": ["barcelona", "manchester", "berlin"],
                   "sam": ["madrid", "tokyo", "londen"],
                   "mohammad": ["new york", "california", "las wegas"]}

for name, places in favorite_places.items():
    print(f"{name.title()} favorite places are: ")
    for place in places:
        favorite_p = print(place)
    print("-" * 10)
