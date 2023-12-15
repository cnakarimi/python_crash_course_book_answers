from pathlib import Path

cat_path = Path('cat.txt')
dog_path = Path('dogs.txt')

wrong_path = False

try:
    with open(cat_path, mode='r') as f:
        cat_name = f.read()
        print('cat names are:\n' + cat_name + '\n\n')
except (FileNotFoundError):
    print('you chose wrong path for cat names')
    wrong_path = True
if not wrong_path:
    try:
        with open(dog_path, mode='r') as f:
            dog_name = f.read()
            print('dog names are: \n' + dog_name + '\n')
    except (FileNotFoundError):
        print('you chose wrong path for dog names')
