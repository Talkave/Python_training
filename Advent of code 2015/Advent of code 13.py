# --- Day 13: Knights of the Dinner Table ---
# In years past, the holiday feast with your family hasn't gone so well. 
# Not everyone gets along! This year, you resolve, will be different. 
# You're going to find the optimal seating arrangement and avoid all those awkward conversations.

# You start by writing up a list of everyone invited and the amount their happiness would increase or decrease if they were to find themselves sitting next to each other person. 
# You have a circular table that will be just big enough to fit everyone comfortably, and so each person will have exactly two neighbors.

# For example, suppose you have only four attendees planned, and you calculate their potential happiness as follows:

# Alice would gain 54 happiness units by sitting next to Bob.
# Alice would lose 79 happiness units by sitting next to Carol.
# Alice would lose 2 happiness units by sitting next to David.
# Bob would gain 83 happiness units by sitting next to Alice.
# Bob would lose 7 happiness units by sitting next to Carol.
# Bob would lose 63 happiness units by sitting next to David.
# Carol would lose 62 happiness units by sitting next to Alice.
# Carol would gain 60 happiness units by sitting next to Bob.
# Carol would gain 55 happiness units by sitting next to David.
# David would gain 46 happiness units by sitting next to Alice.
# David would lose 7 happiness units by sitting next to Bob.
# David would gain 41 happiness units by sitting next to Carol.
# Then, if you seat Alice next to David, Alice would lose 2 happiness units (because David talks so much), but David would gain 46 happiness units (because Alice is such a good listener), for a total change of 44.

# If you continue around the table, you could then seat Bob next to Alice (Bob gains 83, Alice gains 54). Finally, seat Carol, who sits next to Bob (Carol gains 60, Bob loses 7) and David (Carol gains 55, David gains 41). The arrangement looks like this:

#      +41 +46
# +55   David    -2
# Carol       Alice
# +60    Bob    +54
#      -7  +83
# After trying every other seating arrangement in this hypothetical scenario, you find that this one is the most optimal, with a total change in happiness of 330.

# What is the total change in happiness for the optimal seating arrangement of the actual guest list?

test_data = "Alice would lose 2 happiness units by sitting next to Bob.\nAlice would lose 62 happiness units by sitting next to Carol.\nAlice would gain 65 happiness units by sitting next to David."
mode = "input"
#mode = "test_input"

if mode == "input":
    input_path = "./Advent of code/input_day13.txt"
    file = open(input_path)
    data = file.read()
    print("MODE = INPUT")
elif mode == "test_input":
    data = test_data
    print("MODE = TEST")

happiness_dict = {}
unique_names = set()
for line in data.splitlines():
    line = line.strip().rstrip(".")
    parts = line.split()
    name1 = parts[0]
    gain_lose = parts[2]
    value = int(parts[3])
    if gain_lose == "lose":
        value = -value
    name2 = parts[-1]
    happiness_dict[(name1, name2)] = value
    unique_names.add(name1)
    unique_names.add(name2)

def happiness_calc(name1, name2):
    return happiness_dict.get((name1, name2), 0)

unique_name_list = list(unique_names)
def permutacje(unique_name_list): # robimy każdą możliwą ścieżkę w ogóle
    if len(unique_name_list) == 0:
        return [[]] # zaczynamy od inputu pustego
    result = []
    for element in range(len(unique_name_list)): # tworzymy permutacje dla każdego elementu listy
        first = unique_name_list[element] # element listy na którym iterujemy
        rest = unique_name_list[:element] + unique_name_list[element+1:] # pozostałe elementy listy z lewej i prawej strony
        for perm in permutacje(rest): # przeprowadź zdefiniowaną powyżej funkcję dla pozostałych elementów listy
            result.append([first] + perm) # stwórz końcowy rezultat zrobiony z elementu listy z ktorego iterowałeś i pozostałych permutacji 
    return result

def total_arrangement_score(arrangement, happiness_calc):
    n = len(arrangement)
    total = 0
    for i in range(n):
        left_person = arrangement[i]
        right_person = arrangement[(i+1) % n]  # jeśli reszta z dzielenia i + 1 np. 13 / długość słowa np 12 jest mniejsza od zera (bo jest -1 w tym przypadku) 
        total += happiness_calc(left_person, right_person)
        total += happiness_calc(right_person, left_person)
    return total

max_score = float('-inf')
best_arrangement = None
for perm in permutacje(unique_name_list):
    score = total_arrangement_score(perm, happiness_calc)
    if score > max_score:
        best_arrangement = perm
        max_score = score

print('Best arrangement:', best_arrangement, 'with score', max_score)

# --- Part Two ---
# In all the commotion, you realize that you forgot to seat yourself. At this point, you're pretty apathetic toward the whole thing, and your happiness wouldn't really go up or down regardless of who you sit next to. You assume everyone else would be just as ambivalent about sitting next to you, too.

# So, add yourself to the list, and give all happiness relationships that involve you a score of 0.

# What is the total change in happiness for the optimal seating arrangement that actually includes yourself?