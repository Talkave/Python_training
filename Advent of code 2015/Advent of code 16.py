# --- Day 16: Aunt Sue ---
# Your Aunt Sue has given you a wonderful gift, and you'd like to send her a thank you card. 
# However, there's a small problem: she signed it "From, Aunt Sue".

# You have 500 Aunts named "Sue".

# So, to avoid sending the card to the wrong person, you need to figure out which Aunt Sue (which you conveniently number 1 to 500, for sanity) gave you the gift. 
# You open the present and, as luck would have it, good ol' Aunt Sue got you a My First Crime Scene Analysis Machine! 
# Just what you wanted. Or needed, as the case may be.

# The My First Crime Scene Analysis Machine (MFCSAM for short) can detect a few specific compounds in a given sample, 
# as well as how many distinct kinds of those compounds there are. According to the instructions, these are what the MFCSAM can detect:

# children, by human DNA age analysis.
# cats. It doesn't differentiate individual breeds.
# Several seemingly random breeds of dog: samoyeds, pomeranians, akitas, and vizslas.
# goldfish. No other kinds of fish.
# trees, all in one group.
# cars, presumably by exhaust or gasoline or something.
# perfumes, which is handy, since many of your Aunts Sue wear a few kinds.
# In fact, many of your Aunts Sue have many of these. 
# You put the wrapping from the gift into the MFCSAM. 
# It beeps inquisitively at you a few times and then prints out a message on ticker tape:

# children: 3
# cats: 7
# samoyeds: 2
# pomeranians: 3
# akitas: 0
# vizslas: 0
# goldfish: 5
# trees: 3
# cars: 2
# perfumes: 1
# You make a list of the things you can remember about each Aunt Sue. 
# Things missing from your list aren't zero - you simply don't remember the value.

# What is the number of the Sue that got you the gift?

test_data = {
'children:':3,
'cats:':7,
'samoyeds:':2,
'pomeranians:': 3,
'akitas:': 0,
'vizslas:': 0,
'goldfish:': 5,
'trees:': 3,
'cars:': 2,
'perfumes:': 1
}

mode = "input"
#mode = "test_input"

if mode == "input":
    input_path = "./Advent of code/input_day16.txt"
    file = open(input_path)
    data = file.read()
    print("MODE = INPUT")
elif mode == "test_input":
    data = test_data
    print("MODE = TEST")

data_types=['children:','cats:','samoyeds:','pomeranians:','akitas:','vizslas:','goldfish:','trees:','cars:','perfumes:']
sue_dict = {} # {"Sue 1":{'children':children,'cats':cats,'samoyeds':samoyeds,'pomeranians': pomeranians,'akitas': akitas,... etc}}

for line in data.strip().splitlines():
    line = line.strip().replace(',','')
    segment = line.split()
    # print(segment) # 8 segmentów
    name = int(segment[1].strip(':'))
    # print(name)
    sue_dict[name]= {}
    i = 0
    while i < 8:
        if segment[i] in data_types:
            sue_dict[name][segment[i]] = int(segment[i+1])
        i+=1
# print(sue_dict)
# print(test_data['children:'])
for sue_id, attrs in sue_dict.items():
    is_match = True
    for prop, val in attrs.items():
        if prop in test_data:
            if prop in ('cats:','trees:'):
                if not (val > test_data[prop]):
                    is_match = False
                    break
            elif prop in ('pomeranians:', 'goldfish:'):
                if not (val < test_data[prop]):
                    is_match = False
                    break
            else:
                if test_data[prop] != val:   
                    is_match = False
                    break
    if is_match:
        print("Candidate:", sue_id)

# print(data)
# print(test_data['children']) # 3

# --- Part Two ---
# As you're about to send the thank you note, something in the MFCSAM's instructions catches your eye. 
# Apparently, it has an outdated retroencabulator, and so the output from the machine isn't exact values - some of them indicate ranges.

# In particular, the cats and trees readings indicates that there are greater than that many (due to the unpredictable nuclear decay of cat dander and tree pollen), 
# while the pomeranians and goldfish readings indicate that there are fewer than that many (due to the modial interaction of magnetoreluctance).

# What is the number of the real Aunt Sue?