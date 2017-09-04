import random
choices_for_sequence = ["6", "a", "b", "c"]


game_sequence = []

for e in range(3):
        i = random.choice(choices_for_sequence)
        choices_for_sequence.remove(i)
        game_sequence.append(i)
print(game_sequence)