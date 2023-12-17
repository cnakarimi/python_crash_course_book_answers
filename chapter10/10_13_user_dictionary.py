from pathlib import Path
import json


def get_stored_information(path):
    if path.exists():
        contents = path.read_text()
        information = json.loads(contents)
        return information
    else:
        return None


def greet_user():
    path = Path('information.json')
    information = get_stored_information(path)
    print(information)
    if information:
        print(f'Welcome back,{information[0]['name']}')
        print(f'We know that you are {information[0]['age']}')
        print(f'and live in {information[0]['city']}')
    else:
        user_name = input('What is your name?\n')
        age = int(input('How old are you?\n'))
        city = input('Which city you live in?\n')

        contents = json.dumps([{'name': user_name, 'age': age, 'city': city}])
        path.write_text(contents)
        print(f"we'll remember you when you comeback, {user_name}")


greet_user()
