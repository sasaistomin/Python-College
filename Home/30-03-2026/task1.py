basketball_players = {
    "Michael Jordan": 198,
    "LeBron James": 206,
    "Stephen Curry": 188
}

while True:
    print("\n1. Show all players")
    print("2. Add a player")
    print("3. Delete a player")
    print("4. Search by name")
    print("5. Change player's height")
    print("6. Exit")

    choice = input("\nSelect an option (1-6): ")

    if choice == '1':
        if not basketball_players:
            print("The database is empty.")
        else:
            print("\nList of basketball players:")
            for name, height in basketball_players.items():
                print(f"{name}: {height} cm")

    elif choice == '2':
        name = input("Enter full name: ")
        height = input("Enter height: ")
        if height.isdigit():
            basketball_players[name] = int(height)
            print(f"Player {name} has been added.")
        else:
            print("Error: Height must be a number!")

    elif choice == '3':
        name = input("Enter name to delete: ")
        if name in basketball_players:
            del basketball_players[name]
            print(f"Player {name} has been deleted.")
        else:
            print("Player not found.")

    elif choice == '4':
        name = input("Enter name to search: ")
        if name in basketball_players:
            print(f"Found: {name}, height: {basketball_players[name]} cm")
        else:
            print("Player not found.")

    elif choice == '5':
        name = input("Enter player's name to update: ")
        if name in basketball_players:
            new_height = input(f"Enter new height for {name}: ")
            if new_height.isdigit():
                basketball_players[name] = int(new_height)
                print("Data updated successfully.")
            else:
                print("Error: Height must be a number!")
        else:
            print("This player is not in the database.")

    elif choice == '6':
        print("Program terminated!")
        break

    else:
        print("Invalid choice, please try again.")