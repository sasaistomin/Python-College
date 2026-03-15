from random import choice

userScore = 0
botScore = 0

for turn in range(1, 3+1):
    print(f"Round: {turn}")
    user = input("Enter choice(scissors, paper, rock, lizard, spock): ")
    bot = choice(['sc', 'p', 'r', 'l', 'sp'])
    
    if user == bot:
        print("Draw round")
    elif((user == 'sc' or  user == 'scissors') and (bot == 'p' or  bot == 'l')) or \
        ((user == 'p' or user == 'paper') and (bot == 'r' or bot == 'sp')) or \
        ((user == 'r' or user == 'rock') and (bot == 'l' or bot == 'sc')) or \
        ((user == 'l' or user == 'lizard') and (bot == 'sp' or bot == 'p')) or \
        ((user == 'sp' or user == 'spock') and (bot == 'sc' or bot == 'r')):
        userScore += 1
        print("User won the round")

    else:
        botScore += 1
        print("Bot won the round")

print(f"\nFinel score\n\tUser: {userScore}\n\tBot: {botScore}")