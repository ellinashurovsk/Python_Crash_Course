def make_shirt(size, text):
    print(f"The size is {size}.")
    print(f"The text is {text}.")


make_shirt("L", "Love my mom")  # позиционные аргументы
make_shirt(size="L", text="Love my mom")  # именованные аргументы
