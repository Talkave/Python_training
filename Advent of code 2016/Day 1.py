# --- Day 1: No Time for a Taxicab ---
# Santa's sleigh uses a very high-precision clock to guide its movements, and the clock's oscillator is regulated by stars. 
# Unfortunately, the stars have been stolen... by the Easter Bunny. To save Christmas, Santa needs you to retrieve all fifty stars by December 25th.

# Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. 
# Each puzzle grants one star. Good luck!

# You're airdropped near Easter Bunny Headquarters in a city somewhere. "Near", 
# unfortunately, is as close as you can get - the instructions on the Easter Bunny Recruiting Document the Elves intercepted start here, 
# and nobody had time to work them out further.

# The Document indicates that you should start at the given coordinates (where you just landed) and face North. 
# Then, follow the provided sequence: either turn left (L) or right (R) 90 degrees, then walk forward the given number of blocks, ending at a new intersection.

# There's no time to follow such ridiculous instructions on foot, though, so you take a moment and work out the destination. 
# Given that you can only walk on the street grid of the city, how far is the shortest path to the destination?

# For example:

# Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5 blocks away.
# R2, R2, R2 leaves you 2 blocks due South of your starting position, which is 2 blocks away.
# R5, L5, R5, R3 leaves you 12 blocks away.
# How many blocks away is Easter Bunny HQ?

test_data = []

mode = "input"
#mode = "test_input"

if mode == "input":
    input_path = "./Advent of code 2016/data_day1.txt"
    file = open(input_path)
    data = file.read().split(', ')
    print("MODE = INPUT")
elif mode == "test_input":
    data = test_data
    print("MODE = TEST")
# print(data)
parsed_data = []
i = 0 
while i < len(data):
    new_line = [data[i][0],int(data[i][1:])]
    parsed_data.append(new_line)
    i += 1
# print(parsed_data[0])
starting_degree = 0
starting_position = [0, 0] 
def movement(degree,position):
    for instr, move in parsed_data:
        if instr == 'R':
            degree += 90
        elif instr == 'L':
            degree -= 90
        degree %= 360 # jesli jest 360, to zmien na 0, jesli jest 450, to zmien na 90 itd itp.
        if degree == 0: # north (y+)
            position[1] += move
        elif degree == 90: #east (x+)
            position[0] += move
        elif degree == 180: #south (y-)
            position[1] -= move
        elif degree == 270: #west (x-)
            position[0] -= move
    return position

final_position = movement(starting_degree,starting_position)
print(final_position)
from math import sqrt
final_position_length = int(sqrt(final_position[0]**2) + sqrt(final_position[1]**2))
print(final_position_length)


# Then, you notice the instructions continue on the back of the Recruiting Document. 
# Easter Bunny HQ is actually at the first location you visit twice.

# For example, if your instructions are R8, R4, R4, R8, the first location you visit twice is 4 blocks away, due East.

# How many blocks away is the first location you visit twice?

starting_degree = 0
starting_position = [0, 0] 
def movement_check(degree,position):
    position_list = [(0,0)]    
    for instr, move in parsed_data:
        if instr == 'R':
            degree += 90
        elif instr == 'L':
            degree -= 90
        degree %= 360 # jesli jest 360, to zmien na 0, jesli jest 450, to zmien na 90 itd itp.
        k = 0
        if degree == 0: # north (y+)
            while k < move:
                new_position = (position[0], position[1] + 1)
                position = new_position
                k+=1
                if new_position in position_list:
                    position_list.append(new_position)
                    return new_position
                else:
                    position_list.append(new_position)
        elif degree == 90: #east (x+)
            while k < move:
                new_position = (position[0]+1, position[1])
                position = new_position
                k+=1
                if new_position in position_list:
                    position_list.append(new_position)
                    return new_position
                else:
                    position_list.append(new_position)
        elif degree == 180: #south (y-)
            while k < move:
                new_position = (position[0], position[1] - 1)
                position = new_position
                k+=1
                if new_position in position_list:
                    position_list.append(new_position)
                    return new_position
                else:
                    position_list.append(new_position)
        elif degree == 270: #west (x-)
            while k < move:
                new_position = (position[0]-1, position[1])
                position = new_position
                k+=1
                if new_position in position_list:
                    position_list.append(new_position)
                    return new_position
                else:
                    position_list.append(new_position)
    new_position = position
    return position_list
final_position = movement_check(starting_degree,starting_position)

print(final_position)

from math import sqrt
final_twice_position_length = int(sqrt(final_position[0]**2) + sqrt(final_position[1]**2))
print(final_twice_position_length)