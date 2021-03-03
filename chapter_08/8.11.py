messages = ["Hello!", "How are you?", "How are you doing?"]


def send_message(messages, sent_message):
    """
    Выводит каждое сообщение и перемещает его в новый список с именем sent_message.
    """
    for message in messages:
        print(f"The message is {message}")
    while messages:
        msg = messages.pop()
        sent_message.append(msg)


sent_message = []
send_message(messages[:], sent_message)
print(messages)
print(sent_message)
