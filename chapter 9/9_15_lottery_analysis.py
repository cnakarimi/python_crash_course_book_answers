from random import choice
list = [1, 5, 34, 2, 3, 7, 8, 45, 78, 26, 'a', 'f', 'j', 'k', 'c']
ticket = []
prize_ticket = ['j', 'c', 2, 34]
while ticket != prize_ticket:
    for i in range(4):
        selected_word = choice(list)
        ticket.append(selected_word)
        print(ticket)
        if len(ticket) == 4 and ticket != prize_ticket:
            ticket.clear()
        elif ticket == prize_ticket:
            print("You've won the lottery with this ticket: ")


print(ticket)
