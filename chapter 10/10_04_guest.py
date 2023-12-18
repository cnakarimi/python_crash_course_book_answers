from pathlib import Path

path = Path('guest.txt')

while True:
    print('what is your name?')
    input_name=input("Enter 'n' if you want to stop: ")
    
    if input_name=='n':
        break
    path.write_text(input_name)
