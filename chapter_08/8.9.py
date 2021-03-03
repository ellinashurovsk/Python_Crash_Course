messages = ["Hello!", "How are you?", "How are you doing?"]


def print_message(messages):
    """
    Выводит текст каждого сообщения в списке.
    """
    for message in messages:
        print(f"The message is \"{message}\".")


print()
print_message(messages)
