# --- Day 15: Science for Hungry People ---
# Today, you set out on the task of perfecting your milk-dunking cookie recipe. All you have to do is find the right balance of ingredients.

# Your recipe leaves room for exactly 100 teaspoons of ingredients. 
# You make a list of the remaining ingredients you could use to finish the recipe (your puzzle input) and their properties per teaspoon:

# capacity (how well it helps the cookie absorb milk)
# durability (how well it keeps the cookie intact when full of milk)
# flavor (how tasty it makes the cookie)
# texture (how it improves the feel of the cookie)
# calories (how many calories it adds to the cookie)
# You can only measure ingredients in whole-teaspoon amounts accurately, and you have to be accurate so you can reproduce your results in the future. 
# The total score of a cookie can be found by adding up each of the properties (negative totals become 0) and then multiplying together everything except calories.

# For instance, suppose you have these two ingredients:

# Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
# Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
# Then, choosing to use 44 teaspoons of butterscotch and 56 teaspoons of cinnamon (because the amounts of each ingredient must add up to 100) 
# would result in a cookie with the following properties:

# A capacity of 44*-1 + 56*2 = 68
# A durability of 44*-2 + 56*3 = 80
# A flavor of 44*6 + 56*-2 = 152
# A texture of 44*3 + 56*-1 = 76
# Multiplying these together (68 * 80 * 152 * 76, ignoring calories for now) results in a total score of 62842880, 
# which happens to be the best score possible given these ingredients. 
# If any properties had produced a negative total, it would have instead become zero, causing the whole score to multiply to zero.

# Given the ingredients in your kitchen and their properties, what is the total score of the highest-scoring cookie you can make?

test_data = {"Frosting": 
             {"capacity" :4, "durability" :-2, "flavor" :0, "texture" :0, },#"calories" :5},
             "Candy":
             {"capacity" :0, "durability" :5, "flavor" :-1, "texture" :0, },#"calories" :8},
             "Butterscotch":
             {"capacity" :-1, "durability" :0, "flavor" :5, "texture" :0, },#"calories" :6},
             "Sugar":
             {"capacity" :0, "durability" :0, "flavor" :-2, "texture" :2, },#"calories" :1},
}
#mode = "input"
mode = "test_input"

if mode == "input":
    input_path = "./Advent of code/input_day15.txt"
    file = open(input_path)
    data = file.read()
    print("MODE = INPUT")
elif mode == "test_input":
    data = test_data
    print("MODE = TEST")

# kombinacje a, b, c, d e.g. 0,0,0,100 : 100*0*100*0*100*(-2), czyli 0 * 100*2 = 0
# 1,0,0,99 (1*4+99*0)*(1*-2+99*0)*(1*0+99*-2)*(1*0+99*2)= 0
# czyli jeśli którykolwiek nawias będzie = 0 to można pominąć tą kombinację

max_score = 0
ingredients = {
'Frosting' : [4,-2,0,0,5],
'Candy' : [0,5,-1,0,8],
'Butterscotch' : [-1,0,5,0,6],
'Sugar' : [0,0,-2,2,1]
} # latwiej mi na tym operować
for weight_F in range(101):
    for weight_C in range(101-weight_F):
        for weight_B in range(101 - weight_F - weight_C):
            weight_S = 100 - weight_F - weight_C - weight_B
            total = [0,0,0,0]
            total_calories = 0
            for i in range(4):
                total[i] = (weight_F*ingredients["Frosting"][i] + weight_C*ingredients["Candy"][i] + weight_B * ingredients["Butterscotch"][i] + weight_S * ingredients["Sugar"][i])
                total_calories = weight_F*ingredients["Frosting"][4] + weight_C*ingredients["Candy"][4] + weight_B * ingredients["Butterscotch"][4] + weight_S * ingredients["Sugar"][4]
            if any(t <= 0 for t in total):
                score = 0
            else:
                score = total[0] * total[1] * total[2] * total[3]
            if score > max_score and total_calories == 500: # calorie counter
                max_score = score

print(max_score)

# --- Part Two ---
# Your cookie recipe becomes wildly popular! 
# Someone asks if you can make another recipe that has exactly 500 calories per cookie (so they can use it as a meal replacement). 
# Keep the rest of your award-winning process the same (100 teaspoons, same ingredients, same scoring system).

# For example, given the ingredients above, if you had instead selected 40 teaspoons of butterscotch and 60 teaspoons of cinnamon (which still adds to 100), 
# the total calorie count would be 40*8 + 60*3 = 500. 
# The total score would go down, though: only 57600000, the best you can do in such trying circumstances.

# Given the ingredients in your kitchen and their properties, what is the total score of the highest-scoring cookie you can make with a calorie total of 500?