import json

file_name = ('favorite_number.json')


def get_favorite_number_user():
    return int(input('what is your favorite number?'))


def save_favorite_number():
    n = get_favorite_number_user()
    with open(file_name, mode='w') as f:
        json.dump(n, f)


def get_favorite_number():
    try:
        with open(file_name) as f:
            return json.load(f)
    except FileNotFoundError:
        save_favorite_number()
        return 'Number saved'


print(get_favorite_number())
