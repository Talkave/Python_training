# --- Day 18: Like a GIF For Your Yard ---
# After the million lights incident, the fire code has gotten stricter: now, at most ten thousand lights are allowed. 
# You arrange them in a 100x100 grid.

# Never one to let you down, Santa again mails you instructions on the ideal lighting configuration. 
# With so few lights, he says, you'll have to resort to animation.

# Start by setting your lights to the included initial configuration (your puzzle input). 
# A # means "on", and a . means "off".

# Then, animate your grid in steps, where each step decides the next configuration based on the current one. 
# Each light's next state (either on or off) depends on its current state and the current states of the eight lights adjacent to it (including diagonals). 
# Lights on the edge of the grid might have fewer than eight neighbors; the missing ones always count as "off".

# For example, in a simplified 6x6 grid, the light marked A has the neighbors numbered 1 through 8, and the light marked B, 
# which is on an edge, only has the neighbors marked 1 through 5:

# 1B5...
# 234...
# ......
# ..123.
# ..8A4.
# ..765.
# The state a light should have next is based on its current state (on or off) plus the number of neighbors that are on:

# A light which is on stays on when 2 or 3 neighbors are on, and turns off otherwise.
# A light which is off turns on if exactly 3 neighbors are on, and stays off otherwise.
# All of the lights update simultaneously; they all consider the same current state before moving to the next.

# Here's a few steps from an example configuration of another 6x6 grid:

# Initial state:
# .#.#.#
# ...##.
# #....#
# ..#...
# #.#..#
# ####..

# After 1 step:
# ..##..
# ..##.#
# ...##.
# ......
# #.....
# #.##..

# After 2 steps:
# ..###.
# ......
# ..###.
# ......
# .#....
# .#....

# After 3 steps:
# ...#..
# ......
# ...#..
# ..##..
# ......
# ......

# After 4 steps:
# ......
# ......
# ..##..
# ..##..
# ......
# ......
# After 4 steps, this example has four lights on.

# In your grid of 100x100 lights, given your initial configuration, how many lights are on after 100 steps?

test_data = [
'.#.#.#',
'...##.',
'#....#',
'..#...',
'#.#..#',
'####..',
]

mode = "input"
#mode = "test_input"

if mode == "input":
    input_path = "./Advent of code/input_day18.txt"
    file = open(input_path)
    data = file.read().splitlines()
    print("MODE = INPUT")
elif mode == "test_input":
    data = test_data
    print("MODE = TEST")
parsed_data = []
for row in data:
    new_data = [1 if column == '#' else 0 for column in row]
    parsed_data.append(new_data)
# print(parsed_data)
# print(parsed_data[0])
def count_neighbors(grid, row, column):
    total = 0
    for row_check in (-1,0,1): # left right
        for column_check in (-1,0,1): # up down
            if row_check == 0 and column_check == 0: # skip ten cell ktory sprawdzasz
                continue
            r_iter,c_iter = row + row_check, column + column_check
            if 0 <= r_iter < len(grid) and 0 <= c_iter < len(grid[0]): # czy jesteś w gridzie?
                total += grid[r_iter][c_iter] # zsumuj wszystkie iteracje gridu, czyli [-1][-1],[-1][0][-1][1],etc. z pominieciem [0][0]
    return total
def light_switcher(grid, steps):
    for _ in range(steps):
        new_grid = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))] # do kazdej iteracji stworz grid w ktorym wszystie swiatelka sa na 0 i w tym gridzie bedziesz przelaczal na 1 albo zostawial 0
        for row in range(len(grid)): # operujemy na argumencie wprowadzonym
            for column in range(len(grid[0])): # kazdy element listy w zakresie grid[0] (czyli lista zawierająca dany wiersz) bedzie odpowiadal kolumnie
                cell = grid[row][column] # ta celka po ktorej sie poruszamy i wobec ktorej sprawdzamy neighbors
                neighbors = count_neighbors(grid, row, column)
                # A light which is on stays on when 2 or 3 neighbors are on, and turns off otherwise.
                # A light which is off turns on if exactly 3 neighbors are on, and stays off otherwise.
                if cell == 1 and (neighbors == 3 or neighbors == 2): # sprawdzamy warunki
                    new_grid[row][column] = 1
                elif cell == 0 and neighbors == 3:
                    new_grid[row][column] = 1
                else: # w sumie niepotrzebne po dłuższej deliberacji, bo updajtuje grid pełen 0
                    new_grid[row][column] = 0
        new_grid[0][0] = 1
        new_grid[-1][0] = 1
        new_grid[0][-1] = 1
        new_grid[-1][-1] = 1 # part 2
        grid = new_grid # po sprawdzeniu wszystkich cell dla gridu nadpisz grid tym nowym gridem (w ktorym wlaczales swiatla po kolei)
    return grid
lights_switched = light_switcher(parsed_data, 100)
# 768 part 1
# 781 part 2
total_value = 0
for row in lights_switched:
    total_value += sum(row)
print(total_value)