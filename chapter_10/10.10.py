with open("10\\article.txt") as file_object:
    content = file_object.read()

number_of_words = content.lower().count("the ")
print(number_of_words)
