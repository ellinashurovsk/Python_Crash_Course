with open('C:\\Users\\Эллина\\Desktop\\Python\\10\\pi_digits.txt') as file_object:
    lines = file_object.readlines()

final_line = ''
for line in lines:
    final_line += line.strip()

print(final_line)
