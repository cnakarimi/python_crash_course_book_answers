def send_message():
    while copied_message:
        current_message = copied_message.pop()
        print(f"sending message : {current_message}")
        sent_message.append(current_message)


unsend_message = ['LOL – laughing out loud.',
                  'OMG – oh my god (or oh my gosh)',
                  'IMO – in my opinion.',
                  'BTW – by the way.',
                  "IDK – I don't know.",
                  'LMK – let me know.']
copied_message = unsend_message[:]
sent_message = []


send_message()

print('folowing messages are sent : ')
for message in sent_message:
    print(message)

print('folowing messages are not sent : ')
for message in copied_message:
    print(message)

print('following messages are archived : ')
for message in unsend_message:
    print(message)
