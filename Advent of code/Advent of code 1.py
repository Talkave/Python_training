import sys
input_path = "./Advent of code/input_day1.txt"
file = open(input_path)
input = file.read()
yolo = list(input)
floor = 0
symbol_id = 0
for i in yolo:
    symbol_id = symbol_id + 1
    if i == '(':
        floor += 1
    else:
        floor -= 1
    if floor < 0:
        print(symbol_id)
        break