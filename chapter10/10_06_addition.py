first_number = input("choose first number: ")
second_number = input("choose second number to add: ")
addition = 0

try:
    addition = int(first_number) + int(second_number)
except (ValueError):
    print('*' * 70)
    print("please only choose numbers")
    print(" " * 1000)


print(addition)
