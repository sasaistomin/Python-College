import random

a = 1
b = 20
user_number = 0
secret_number = random.randint(a, b)
attempts_count = 0  #лічильник спроб
difference = 0
while user_number != secret_number:
    user_number = int(input(f"Enter number between : [{a}] to [{b}] : "))
    attempts_count += 1
    if user_number > secret_number:
        print("Your number greater than secret")
        difference = user_number - secret_number
        if difference > 8:
            print("Difference is significant!")
        else:
            print("You are close!")

    elif user_number < secret_number:
        print("Your number less than secret")
        difference = secret_number - user_number
        if difference > 8:
            print("Difference is significant!")
        else:
            print("You are close!")
# повідомлення при перемозі та статистику
print("YOU WON!")
print(f"You guessed number [{secret_number}]\nAttempts count [{attempts_count}]")