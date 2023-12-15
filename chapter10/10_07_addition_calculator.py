
addition = 0
calculator_on = True

while calculator_on:
    print("type 'q' if you wanna close the app")
    first_number = input("choose first number: ")
    if first_number == 'q':
        calculator_on = False
        break
    else:
        second_number = input("choose second number to add: ")
        if second_number == 'q':
            calculator_on = False
            break
        else:
            try:
                addition = int(first_number) + int(second_number)
                print('The addition is: ' + str(addition))
            except (ValueError):
                print('*' * 70)
                print("please only choose numbers!!!!!!!!")
                print(" " * 1000)
