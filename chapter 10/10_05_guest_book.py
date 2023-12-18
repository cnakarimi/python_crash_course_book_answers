from pathlib import Path
path = Path("text_book.txt")

names = []

while True:
    print("what's your name?")
    input_user= input("print 'n' if you wanna stop:")
    
    if input_user == 'n':
        break
    names.append(input_user)
    
with open(path, 'a') as file_object:
    for name in names:
        file_object.write(name + '\n')