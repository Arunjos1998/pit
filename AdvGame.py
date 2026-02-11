def intro():
    print("Welcome to the Adventure Game!")
    print("You are standing in front of a mysterious castle.")
    print("Your goal is to explore and find the hidden treasure.")
    print("Type 'quit' anytime to exit the game.")
    start_game()

def start_game():
    print("\nYou see two paths: One leads to the castle, and the other leads to the forest.")
    choice = input("Which path do you choose? (castle/forest): ").lower()

    if choice == "castle":
        castle_path()
    elif choice == "forest":
        forest_path()
    elif choice == "quit":
        print("Thanks for playing!")
    else:
        print("Invalid choice. Please choose 'castle' or 'forest'.")
        start_game()

def castle_path():
    print("\nYou enter the castle. It's dark, and you hear strange noises.")
    print("You see a door to your left and a staircase leading up.")
    choice = input("Do you go left (door) or up (stairs)? ").lower()

    if choice == "door":
        door_choice()
    elif choice == "stairs":
        stairs_choice()
    elif choice == "quit":
        print("Thanks for playing!")
    else:
        print("Invalid choice. Please choose 'door' or 'stairs'.")
        castle_path()

def door_choice():
    print("\nThe door creaks open. You find a treasure chest!")
    print("You open it and find gold, jewels, and a magic sword.")
    print("Congratulations, you’ve found the treasure!")
    play_again()

def stairs_choice():
    print("\nYou climb the stairs and find a room full of traps!")
    print("Sadly, you trip on a hidden trap and fall into a pit.")
    print("Game Over!")
    play_again()

def forest_path():
    print("\nYou enter the forest. It's quiet and peaceful.")
    print("You spot a mysterious figure ahead. It's a wise old man!")
    choice = input("Do you approach him or walk away? (approach/walk): ").lower()

    if choice == "approach":
        wise_man_choice()
    elif choice == "walk":
        print("\nYou decide to walk away, but you get lost and never find your way out.")
        print("Game Over!")
        play_again()
    elif choice == "quit":
        print("Thanks for playing!")
    else:
        print("Invalid choice. Please choose 'approach' or 'walk'.")
        forest_path()

def wise_man_choice():
    print("\nThe wise man offers you a magical map that leads to the hidden treasure!")
    print("You follow the map and find a chest filled with gold and jewels.")
    print("Congratulations, you’ve found the treasure!")
    play_again()

def play_again():
    choice = input("\nDo you want to play again? (yes/no): ").lower()
    if choice == "yes":
        start_game()
    elif choice == "no":
        print("Thanks for playing!")
    else:
        print("Invalid choice. Please choose 'yes' or 'no'.")
        play_again()

if __name__ == "__main__":
    intro()
