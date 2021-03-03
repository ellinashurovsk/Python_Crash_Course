from random import choice

lottery = [5, 6, 7, 8, 3, 11, 45, 8, 20, 10, 'l', 'm', 'a', 't', 'y']

winner = []
for i in range(0, 4):
    lottery_choice = choice(lottery)
    winner.append(lottery_choice)

print(f"The winner is the owner of {winner} ticket.")
