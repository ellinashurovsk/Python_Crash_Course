from random import choice

lottery = [5, 6, 7, 8, 3, 11, 45, 8, 20, 10, 'l', 'm', 'a', 't', 'y']

winner = []
for i in range(0, 4):
    lottery_choice = choice(lottery)
    winner.append(lottery_choice)

print(f"The winner is the owner of {winner} ticket.")

my_ticket = []
count = 0


while my_ticket != winner:
    my_ticket = []
    for i in range(0, 4):
        lottery_choice_1 = choice(lottery)
        my_ticket.append(lottery_choice_1)
    count += 1

print(my_ticket)
print(count)
