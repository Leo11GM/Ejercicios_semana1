POS_X = 0
POS_Y = 1
MAP_WIDTH = 20
MAP_HEIGHT = 15

my_position = [3, 1]

print("+" + "-" * MAP_WIDTH * 3 + "+")

for coordinate_y in range(MAP_HEIGHT):
    print("|", end="")
    for coordinate_X in range(MAP_WIDTH):
        #Make an @ appear representing a player at the point indicated by the my_position variable.
        if my_position[POS_X] == coordinate_X and my_position[POS_Y] == coordinate_y:
            print(" @ ", end="")
        else:
            print("   ", end="")
    print("|")


print("+" + "-" * MAP_WIDTH * 3 + "+")


