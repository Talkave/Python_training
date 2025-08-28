#--- Day 17: No Such Thing as Too Much ---
# The elves bought too much eggnog again - 150 liters this time. 
# To fit it all into your refrigerator, you'll need to move it into smaller containers. 
# You take an inventory of the capacities of the available containers.

# For example, suppose you have containers of size 20, 15, 10, 5, and 5 liters. If you need to store 25 liters, there are four ways to do it:

# 15 and 10
# 20 and 5 (the first 5)
# 20 and 5 (the second 5)
# 15, 5, and 5
# Filling all containers entirely, how many different combinations of containers can exactly fit all 150 liters of eggnog?

test_data = [1,2,3,4,111,22,33,44,55,66,7,8,9,10]

mode = "input"
#mode = "test_input"

if mode == "input":
    input_path = "./Advent of code/input_day17.txt"
    file = open(input_path)
    data = file.read().splitlines()
    print("MODE = INPUT")
elif mode == "test_input":
    data = test_data
    print("MODE = TEST")

data2 = []
for x in data:
    data2.append(int(x))
# print(sum(data2)) # 522
volume = 150
combinations = []

def search_combinations(start,subset,current_sum):
    if current_sum == volume:
        combinations.append(list(subset))
        return
    if current_sum > volume:
        return
    for i in range(start, len(data2)):
        subset.append(data2[i])
        search_combinations(i+1, subset,current_sum + data2[i])
        subset.pop()

search_combinations(0,[],0)
# print(len(combinations))

# --- Part Two ---
# While playing with all the containers in the kitchen, another load of eggnog arrives! 
# The shipping and receiving department is requesting as many containers as you can spare.

# Find the minimum number of containers that can exactly fit all 150 liters of eggnog. 
# How many different ways can you fill that number of containers and still hold exactly 150 litres?

# In the example above, the minimum number of containers was two. 
# There were three ways to use that many containers, and so the answer there would be 3.

# print(combinations)
min_length = min(len(combo) for combo in combinations)
count_min = sum(1 for combo in combinations if len(combo) == min_length)
print(count_min)