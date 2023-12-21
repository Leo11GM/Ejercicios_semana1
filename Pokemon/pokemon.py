from random import randint


def perform_attack(attacker, defender, attack_name, damage):
    """
    Performs an attack on a defender by an attacker.

    Args:
        attacker (str): The name of the attacker.
        defender (int): The current HP of the defender.
        attack_name (str): The name of the attack.
        damage (int): The amount of damage the attack deals.

    Returns:
        int: The updated HP of the defender after the attack.
    """
    print(f"{attacker} uses {attack_name} and deals {damage} damage.")
    defender -= damage
    defender = max(0, defender)  # Ensure that HP doesn't go below 0
    print(f"{attacker} has {defender} HP left: {'=' * (defender // 5)}")
    return defender

def get_user_input(prompt, valid_inputs):
    """
    Prompt the user for input and validate it against a list of valid inputs.

    Args:
        prompt (str): The prompt to display to the user.
        valid_inputs (list): A list of valid inputs.

    Returns:
        int: The user's input as an integer.

    Raises:
        ValueError: If the user enters a non-numeric input.

    Example:
        >>> get_user_input("Enter a number: ", [1, 2, 3])
        Enter a number: 5
        Invalid input. Please enter a valid option.
        Enter a number: 2
        2
    """
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

    # Prompt user to continue
    input("Press Enter to continue...")

    # Charmander's turn
    print("\nCharmander's turn:")
    print("Choose your move:")
    print("1. Ember")
    print("2. Scratch")

    charmander_attack = get_user_input("Enter 1 or 2 (type 'exit' to end the game): ", [1, 2])

    if charmander_attack == 1:
        pikachu_hp = perform_attack("Charmander", pikachu_hp, "Ember", 10)
    else:
        pikachu_hp = perform_attack("Charmander", pikachu_hp, "Scratch", 5)

    # Prompt user to continue
    input("Press Enter to continue...")

# Check for the winner
if pikachu_hp <= 0:
    print("\nCharmander wins!")
elif charmander_hp <= 0:
    print("\nPikachu wins!")