import os
import random
import readchar

POS_X = 0
POS_Y = 1
MAP_WIDTH = 20
MAP_HEIGHT = 15

my_position = [3, 1]

# Generate ten points in the map with random positions using the random module
map_objects = [[random.randint(0, MAP_WIDTH - 1), random.randint(0, MAP_HEIGHT - 1)] for _ in range(10)]

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

            # Make an @ appear representing a player at the point indicated by the my_position variable.
            if my_position[POS_X] == coordinate_X and my_position[POS_Y] == coordinate_y:
                char_to_draw = "@"

                # Check if "@" is over a "*"; if so, remove the "*" from the map_objects list
                for map_object in map_objects:
                    if map_object[POS_X] == coordinate_X and map_object[POS_Y] == coordinate_y:
                        map_objects.remove(map_object)

            print(" {} ".format(char_to_draw), end="")
        print("|")

    print("+" + "-" * MAP_WIDTH * 3 + "+")

    # Ask the player where they want to move
    direction = readchar.readchar()
    print(direction)

    if direction == "w":
        my_position[POS_Y] -= 1
    elif direction == "a":
        my_position[POS_X] -= 1
    elif direction == "s":
        my_position[POS_Y] += 1
    elif direction == "d":
        my_position[POS_X] += 1
    elif direction == "q":
        break

    # Check if the movement is possible
    if my_position[POS_X] < 0:
        my_position[POS_X] = 0
    elif my_position[POS_X] >= MAP_WIDTH:
        my_position[POS_X] = MAP_WIDTH - 1

    if my_position[POS_Y] < 0:
        my_position[POS_Y] = 0
    elif my_position[POS_Y] >= MAP_HEIGHT:
        my_position[POS_Y] = MAP_HEIGHT - 1

    # Clean the screen with os module
    os.system("cls")






