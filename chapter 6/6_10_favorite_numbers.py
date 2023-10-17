favorite_numbers = {'Alice': [42, 22],
                    'Bob': [23, 17],
                    'Charlie': [33, 11],
                    'Dustin': [3, 1],
                    'Eliza': [14, 99]
                    }
for name, number in favorite_numbers.items():
    print(name+"s favorite numbers are: ")
    for x in number:
        print(x)
