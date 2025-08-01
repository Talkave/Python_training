#List comprehension: newlist = [expression for item in oldlist if condition == True]

#--- Day 3: Perfectly Spherical Houses in a Vacuum ---
# Santa is delivering presents to an infinite two-dimensional grid of houses.
#
# He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. 
# Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.
#[x x]
#[x x]
#However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?
"""
--- Part Two ---
The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.

Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

This year, how many houses receive at least one present?

For example:

^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.
"""
#test_input = "^>v<" # 4
#test_input = "^v^v^v^v^v" # 2
#test_input = ">" # 2
test_input = ">>>>>>>>^^^^^^^^"
mode = "input"
#mode = "test_input"

if mode == "input":
    input_path = "./Advent of code/input_day3.txt"
    file = open(input_path)
    input = file.read()
elif mode == "test_input":
    input = test_input

movement=list(input)

new_movement = enumerate(movement)

santa_x, santa_y = 0, 0
robo_x, robo_y = 0, 0

visited = set()
visited.add((0,0))

for index, element in new_movement:
    if index %2 == 0:
        if element == "^":
            santa_y+=1
        elif element == "<":
            santa_x-=1
        elif element == "v":
            santa_y-=1
        elif element == ">":
            santa_x+=1
        visited.add((santa_x,santa_y))
    else:
        if element == "^":
            robo_y+=1
        elif element == "<":
            robo_x-=1
        elif element == "v":
            robo_y-=1
        elif element == ">":
            robo_x+=1
        visited.add((robo_x,robo_y))

print(len(visited))
