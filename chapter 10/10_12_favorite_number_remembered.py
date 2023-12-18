import json
from json import JSONDecodeError


file_name = 'favorite_number.json'


def get_favorite_number():
    user_favorite_numb = int(input('what is your favorite number? '))
    return user_favorite_numb


def save_favorite_number():
    n = get_favorite_number()
    with open(file_name, 'w') as f:
        json.dump(n, f)


try:
    with open(file_name, 'r') as f:
        print(json.load(f))
except (JSONDecodeError):
    save_favorite_number()
    print('Number saved')
