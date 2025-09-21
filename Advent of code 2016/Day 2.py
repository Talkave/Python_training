# --- Day 2: Bathroom Security ---
# You arrive at Easter Bunny Headquarters under cover of darkness. 
# However, you left in such a rush that you forgot to use the bathroom! 
# Fancy office buildings like this one usually have keypad locks on their bathrooms, so you search the front desk for the code.

# "In order to improve security," the document you find says, "bathroom codes will no longer be written down. 
# Instead, please memorize and follow the procedure below to access the bathrooms."

# The document goes on to explain that each button to be pressed can be found by starting on the previous button and moving to adjacent buttons on the keypad: 
# U moves up, D moves down, L moves left, and R moves right. 
# Each line of instructions corresponds to one button, starting at the previous button (or, for the first line, the "5" button); 
# press whatever button you're on at the end of each line. If a move doesn't lead to a button, ignore it.

# You can't hold it much longer, so you decide to figure out the code as you walk to the bathroom. You picture a keypad like this:

# 1 2 3
# 4 5 6
# 7 8 9
# Suppose your instructions are:

# ULL
# RRDDD
# LURDL
# UUUUD
# You start at "5" and move up (to "2"), left (to "1"), and left (you can't, and stay on "1"), so the first button is 1.
# Starting from the previous button ("1"), you move right twice (to "3") 
# and then down three times (stopping at "9" after two moves and ignoring the third), ending up with 9.
# Continuing from "9", you move left, up, right, down, and left, ending with 8.
# Finally, you move up four times (stopping at "2"), then down once, ending with 5.
# So, in this example, the bathroom code is 1985.

# Your puzzle input is the instructions from the document you found at the front desk. What is the bathroom code?

test_data = []

mode = "input"
#mode = "test_input"

if mode == "input":
    input_path = "./Advent of code 2016/data_day2.txt"
    file = open(input_path)
    data = file.read().split('\n')
    print("MODE = INPUT")
elif mode == "test_input":
    data = test_data
    print("MODE = TEST")
parsed_data = []
for x in data:
    parsed_data.append(x)
# print(parsed_data)
position = 5
def code_generator(position, data):
    for z in data:
        if z == 'D' and (position not in [7,8,9]):
            position += 3
        elif z == 'L' and (position not in [1,4,7]):
            position -= 1
        elif z == 'R' and (position not in [3,6,9]):
            position += 1 
        elif z == 'U' and (position not in [1,2,3]):
            position -= 3
        else:
            continue
    return position
keycode = []
for line in parsed_data:
    position = code_generator(position,line)
    keycode.append(position)
print(keycode)

# --- Part Two ---
# You finally arrive at the bathroom (it's a several minute walk from the lobby so visitors can behold the many fancy conference rooms and water coolers on this floor)
# and go to punch in the code. Much to your bladder's dismay, the keypad is not at all like you imagined it. 
# Instead, you are confronted with the result of hundreds of man-hours of bathroom-keypad-design meetings:

#     1
#   2 3 4
# 5 6 7 8 9
#   A B C
#     D
# You still start at "5" and stop when you're at an edge, but given the same instructions as above, the outcome is very different:

# You start at "5" and don't move at all (up and left are both edges), ending at 5.
# Continuing from "5", you move right twice and down three times (through "6", "7", "B", "D", "D"), ending at D.
# Then, from "D", you move five more times (through "D", "B", "C", "C", "B"), ending at B.
# Finally, after five more moves, you end at 3.
# So, given the actual keypad layout, the code would be 5DB3.

# Using the same instructions in your puzzle input, what is the correct bathroom code?

keypad = [
    [None, None ,'1',None,None],
    [None   ,'2','3','4',None],
        ['5','6','7','8','9'],
    [None   ,'A','B','C',None],
    [None,None  ,'D',None,None]
] # (row,col) index
row, col = 2, 0
keycode2 = []
for line in parsed_data:
    for symbol in line:
        new_row, new_col = row,col
        if symbol == 'D':
            new_row += 1
        elif symbol == 'U':
            new_row -= 1
        elif symbol == 'L':
            new_col -= 1
        elif symbol == 'R':
            new_col += 1
        if (0 <= new_row < len(keypad)
            and 0 <= new_col < len(keypad[0])
            and keypad[new_row][new_col] is not None):
            row,col = new_row,new_col
    keycode2.append(keypad[row][col])
print(keycode2)
