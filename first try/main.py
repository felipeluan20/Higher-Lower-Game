import art
import game_data
import random

print(art.logo)
selected_dict_A = random.choice(game_data.data)
selected_dict_B = random.choice(game_data.data)
if selected_dict_A == selected_dict_B:
    selected_dict_B = random.choice(game_data.data)

choice_A = f"{selected_dict_A['name']}, a {selected_dict_A['description']}, from {selected_dict_A['country']}."
choice_B = f"{selected_dict_B['name']}, a {selected_dict_B['description']}, from {selected_dict_B['country']}."


print("Compare A:", choice_A)
print(art.vs)
print("Against B:", choice_B)

if selected_dict_A['follower_count'] > selected_dict_B['follower_count']:
    answer = 'A'
else:
    answer = 'B'

user_guess = input("Who has more followers? Type 'A' or 'B': ")
score = 0
if user_guess.upper() == answer:
    print("You're right!")
    score += 1
else:
    print(f"Sorry, that's wrong. Final score: {score}")

