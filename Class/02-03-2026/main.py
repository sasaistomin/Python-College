# import random


# player_score = 0
# bot_score = 0

# for turn in range(1, 3 + 1):
#     print(f"Round : {turn}")
#     player_choice = str(input("Enter choice : [r],[p],[s] : "))
#     bot_choice = random.choice(['r', 'p', 's'])
#     print(f"Bot choice: {bot_choice}")
    
#     if player_choice == bot_choice:
#         print('Draw round!')
#     elif (player_choice == 'r' and bot_choice == 's') or \
#          (player_choice == 'p' and bot_choice == 'r') or \
#          (player_choice == 's' and bot_choice == 'p'):
#         player_score += 1
#         print(f"Player won the round!")
#     else:
#         bot_score += 1
#         print(f"Bot won the round!")

# print(f"Final Score - Player: {player_score}, Bot: {bot_score}")

input_string = input("Введіть список рядків, розділених комою: ")
string_list = [s.strip() for s in input_string.split(',')]

start_char = input("Введіть літеру, з якої мають починатися рядки: ").strip()[0]

filtered_list = []


for s in string_list:
    if s.startswith(start_char):
        filtered_list.append(s)


print(f"Рядки, що починаються з '{start_char}': {filtered_list}")
