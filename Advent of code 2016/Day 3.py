# --- Day 3: Squares With Three Sides ---
# Now that you can think clearly, you move deeper into the labyrinth of hallways and office furniture that makes up this part of Easter Bunny HQ. 
# This must be a graphic design department; the walls are covered in specifications for triangles.

# Or are they?

# The design document gives the side lengths of each triangle it describes, but... 5 10 25? 
# Some of these aren't triangles. You can't help but mark the impossible ones.

# In a valid triangle, the sum of any two sides must be larger than the remaining side. 
# For example, the "triangle" given above is impossible, because 5 + 10 is not larger than 25.

# In your puzzle input, how many of the listed triangles are possible?

test_data = []

mode = "input"
#mode = "test_input"

if mode == "input":
    input_path = "./Advent of code 2016/data_day3.txt"
    file = open(input_path)
    data = file.read().split('\n')
    print("MODE = INPUT")
elif mode == "test_input":
    data = test_data
    print("MODE = TEST")

# print(data)

parsed_data = []
for line in data:
    newline = list(map(int,line.strip().split()))
    parsed_data.append(newline)
valid_triangles = []
for line in parsed_data:
    if (
    (line[0] + line[1]) > line[2] and
    (line[1] + line[2]) > line[0] and
    (line[0] + line[2]) > line[1]):
        valid_triangles.append(line)
    else:
        continue

print(len(valid_triangles))

# --- Part Two ---
# Now that you've helpfully marked up their design documents, it occurs to you that triangles are specified in groups of three vertically. 
# Each set of three numbers in a column specifies a triangle. Rows are unrelated.

# For example, given the following specification, numbers with the same hundreds digit would be part of the same triangle:

# 101 301 501
# 102 302 502
# 103 303 503
# 201 401 601
# 202 402 602
# 203 403 603
# In your puzzle input, and instead reading by columns, how many of the listed triangles are possible?
if mode == "input":
    input_path = "./Advent of code 2016/data_day3.txt"
    file = open(input_path)
    data2 = file.read().split()
# print(data2)
i = 0
parsed_data2=[]
while i <= len(data2):
    try:
        new_line = [int(data2[i]),int(data2[i+3]),int(data2[i+6])]
        parsed_data2.append(new_line)
    except IndexError:
        break
    i+=1
    if i % 3 == 0 :
        i += 6
print(len(parsed_data2))
valid_triangles2=[]
for line in parsed_data2:
    if (
    (line[0] + line[1]) > line[2] and
    (line[1] + line[2]) > line[0] and
    (line[0] + line[2]) > line[1]):
        valid_triangles2.append(line)
    else:
        continue
print(len(valid_triangles2))