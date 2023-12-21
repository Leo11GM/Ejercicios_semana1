from random import randint
import os

def clear_screen():
    # Clear screen command based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')

def perform_attack(attacker, defender, attack_name, damage):
    print(f"{attacker} uses {attack_name} and deals {damage} damage.")
    defender -= damage
    defender = max(0, defender)  # Ensure that HP doesn't go below 0
    print(f"{attacker} has {defender} HP left: {'=' * (defender // 5)}")
    return defender

def get_user_input(prompt, valid_inputs):
    while True:
        try:
            user_input = input(prompt)
            if user_input.lower() == "exit":
                exit()
            user_input = int(user_input)
            if user_input in valid_inputs:
                return user_input
            else:
                print("Invalid input. Please enter a valid option.")

        except ValueError:
            print("Invalid input. Please enter a number.")

def display_life_bars(pikachu_hp, charmander_hp):
    print("\nComparison of Life Bars:")
    print(f"Pikachu: {'=' * (pikachu_hp // 5)}")
    print(f"Charmander: {'=' * (charmander_hp // 5)}")

pikachu_hp = 100
charmander_hp = 100

print("Welcome to the Pokemon Battle!")
print("Pikachu vs. Charmander")

while pikachu_hp > 0 and charmander_hp > 0:
    # Pikachu's turn
    print("\nPikachu's turn:")
    pikachu_attack = randint(1, 2)
    if pikachu_attack == 1:
        charmander_hp = perform_attack("Pikachu", charmander_hp, "Thunderbolt", 10)
    else:
        charmander_hp = perform_attack("Pikachu", charmander_hp, "Quick Attack", 5)

    # Display comparison of life bars
    display_life_bars(pikachu_hp, charmander_hp)

    # Prompt user to continue
    input("Press Enter to continue...")
    clear_screen()

    # Charmander's turn
    print("\nCharmander's turn:")
    print("Choose your move:")
    print("1. Ember")
    print("2. Scratch")
    print("3. Skip Turn")

    charmander_attack = get_user_input("Enter 1, 2, or 3 (type 'exit' to end the game): ", [1, 2, 3])

    if charmander_attack == 1:
        pikachu_hp = perform_attack("Charmander", pikachu_hp, "Ember", 10)
    elif charmander_attack == 2:
        pikachu_hp = perform_attack("Charmander", pikachu_hp, "Scratch", 5)

    # Display comparison of life bars
    display_life_bars(pikachu_hp, charmander_hp)

    # Prompt user to continue
    if charmander_attack != 3:
        input("Press Enter to continue...")
        clear_screen()

# Check for the winner
if pikachu_hp <= 0:
    print("\nCharmander wins!")
elif charmander_hp <= 0:
    print("\nPikachu wins!")