import os
import random
import readchar

POS_X = 0
POS_Y = 1
MAP_WIDTH = 20
MAP_HEIGHT = 15

my_position = [3, 1]
tail_length = 0
tail = []


# Function to generate new random points for map_objects
def generate_map_objects():
    return [[random.randint(0, MAP_WIDTH - 1), random.randint(0, MAP_HEIGHT - 1)] for _ in range(10)]


# Generate ten points in the map with random positions using the random module
map_objects = generate_map_objects()


def restart_game():
    global my_position, tail_length, tail, map_objects
    my_position = [3, 1]
    tail_length = 0
    tail = []
    map_objects = generate_map_objects()


while True:
    # Draw the map
    print("+" + "-" * MAP_WIDTH * 3 + "+")

    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")
        for coordinate_X in range(MAP_WIDTH):

            char_to_draw = " "

            # Check if the current position has a map object
            for map_object in map_objects:
                if map_object[POS_X] == coordinate_X and map_object[POS_Y] == coordinate_y:
                    char_to_draw = "*"

            # Draw the tail
            for tail_piece in tail:
                if tail_piece[POS_X] == coordinate_X and tail_piece[POS_Y] == coordinate_y:
                    char_to_draw = "@"
            # Make an @ appear representing a player at the point indicated by the my_position variable.
            if my_position[POS_X] == coordinate_X and my_position[POS_Y] == coordinate_y:
                char_to_draw = "@"

                # Check if "@" is over a "*"; if so, remove the "*" from the map_objects list
                for map_object in map_objects:
                    if map_object[POS_X] == coordinate_X and map_object[POS_Y] == coordinate_y:
                        map_objects.remove(map_object)
                        tail_length += 1

                        # Generate a new random position for a new "*"
                        new_map_object = [random.randint(0, MAP_WIDTH - 1), random.randint(0, MAP_HEIGHT - 1)]
                        map_objects.append(new_map_object)

            print(" {} ".format(char_to_draw), end="")
        print("|")

    print("+" + "-" * MAP_WIDTH * 3 + "+")
    # Ask the player where they want to move
    direction = readchar.readchar()
    print(direction)

    # Check if the new head position collides with the tail
    new_head_position = my_position.copy()
    if direction == "w":
        new_head_position[POS_Y] -= 1
        if new_head_position[POS_Y] < 0:
            new_head_position[POS_Y] = MAP_HEIGHT - 1
    elif direction == "a":
        new_head_position[POS_X] -= 1
        if new_head_position[POS_X] < 0:
            new_head_position[POS_X] = MAP_WIDTH - 1
    elif direction == "s":
        new_head_position[POS_Y] += 1
        if new_head_position[POS_Y] >= MAP_HEIGHT:
            new_head_position[POS_Y] = 0
    elif direction == "d":
        new_head_position[POS_X] += 1
        if new_head_position[POS_X] >= MAP_WIDTH:
            new_head_position[POS_X] = 0
    elif direction == "q":
        exit()

    if new_head_position in tail:
        print("Game Over! You collided with yourself.")
        input("Press Enter to continue...")
        restart_game()

    else:
        tail.insert(0, my_position.copy())
        tail = tail[:tail_length]
        my_position = new_head_position
    # Clean the screen with os module
    os.system("cls")