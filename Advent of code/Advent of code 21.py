# --- Day 21: RPG Simulator 20XX ---
# Little Henry Case got a new video game for Christmas. 
# It's an RPG, and he's stuck on a boss. He needs to know what equipment to buy at the shop. He hands you the controller.

# In this game, the player (you) and the enemy (the boss) take turns attacking. 
# The player always goes first. Each attack reduces the opponent's hit points by at least 1. 
# The first character at or below 0 hit points loses.

# Damage dealt by an attacker each turn is equal to the attacker's damage score minus the defender's armor score. 
# An attacker always does at least 1 damage. So, if the attacker has a damage score of 8, and the defender has an armor score of 3, the defender loses 5 hit points.
#  If the defender had an armor score of 300, the defender would still lose 1 hit point.

# Your damage score and armor score both start at zero. They can be increased by buying items in exchange for gold. 
# You start with no items and have as much gold as you need. Your total damage or armor is equal to the sum of those stats from all of your items. 
# You have 100 hit points.

# Here is what the item shop is selling:

# Weapons:    Cost  Damage  Armor
# Dagger        8     4       0
# Shortsword   10     5       0
# Warhammer    25     6       0
# Longsword    40     7       0
# Greataxe     74     8       0

# Armor:      Cost  Damage  Armor
# Leather      13     0       1
# Chainmail    31     0       2
# Splintmail   53     0       3
# Bandedmail   75     0       4
# Platemail   102     0       5

# Rings:      Cost  Damage  Armor
# Damage +1    25     1       0
# Damage +2    50     2       0
# Damage +3   100     3       0
# Defense +1   20     0       1
# Defense +2   40     0       2
# Defense +3   80     0       3
# You must buy exactly one weapon; no dual-wielding. 
# Armor is optional, but you can't use more than one. You can buy 0-2 rings (at most one for each hand). 
# You must use any items you buy. The shop only has one of each item, so you can't buy, for example, two rings of Damage +3.

# For example, suppose you have 8 hit points, 5 damage, and 5 armor, and that the boss has 12 hit points, 7 damage, and 2 armor:

# The player deals 5-2 = 3 damage; the boss goes down to 9 hit points.
# The boss deals 7-5 = 2 damage; the player goes down to 6 hit points.
# The player deals 5-2 = 3 damage; the boss goes down to 6 hit points.
# The boss deals 7-5 = 2 damage; the player goes down to 4 hit points.
# The player deals 5-2 = 3 damage; the boss goes down to 3 hit points.
# The boss deals 7-5 = 2 damage; the player goes down to 2 hit points.
# The player deals 5-2 = 3 damage; the boss goes down to 0 hit points.
# In this scenario, the player wins! (Barely.)

# You have 100 hit points. The boss's actual stats are in your puzzle input. What is the least amount of gold you can spend and still win the fight?

test_data = 10

mode = "input"
# mode = "test_input"

if mode == "input":
    input_path = "./Advent of code/input_day21.txt"
    file = open(input_path)
    data = file.read().splitlines()
    print("MODE = INPUT")
elif mode == "test_input":
    data = test_data
    print("MODE = TEST")
equipment = []
player_starting_data = {'Hit Points': 100, 'Damage': 0, 'Armor': 0}
boss_data = {'Hit Points': 109, 'Damage': 8, 'Armor': 2}
# print(data)
parsed_data = []
for line in data:
    parsed_line = line.split()
    parsed_data.append(parsed_line)
for line in parsed_data:
    if line == []:
        parsed_data.pop(parsed_data.index(line))
for line in parsed_data:
    if 'Weapons:' in line:
        parsed_data.pop(parsed_data.index(line))
for line in parsed_data:
    if 'Armor:' in line:
        parsed_data.pop(parsed_data.index(line))
for line in parsed_data:
    if 'Rings:' in line:
        parsed_data.pop(parsed_data.index(line))
# self explanatory = czyscimy data 
i = 10
while i < len(parsed_data):
    parsed_data[i][0] = parsed_data[i][0] + parsed_data[i][1]
    parsed_data[i].pop(1)
    i += 1
# w ringach zrobilo sie osobno Defense, +1, czyscimy to jako Defense+1 etc.
for name, cost, dmg, arm in parsed_data:
    equipment.append({
        'name' : name,
        'cost' : int(cost),
        'dmg' : int(dmg),
        'arm' : int(arm),
    })
#robimy dict z przypisanymi wartosciami
weapons = equipment[0:5]
armor = [{'name' : "None",'cost' : 0,'dmg' : 0,'arm' : 0,}] + equipment[5:10]
rings = equipment[10:]
#osobny dict dla kazdej kategorii
# print(weapons)
# print(armor)
# print(rings)
def combat(player_data, boss_data):
    player_hp = player_data['Hit Points']
    boss_hp = boss_data['Hit Points']
    player_dmg = max(1, player_data['Damage'] - boss_data['Armor'])
    boss_dmg = max(1, boss_data['Damage'] - player_data['Armor'])
    # znajdz wieksza wartosc max(), miedzy wartoscia 1 a drugim argumentem - minimalny dmg jaki mozna zadac jest 1
    turns_to_kill_boss = (boss_hp + player_dmg - 1) // player_dmg
    # robimy sobie floor division (zaokraglanie w dol) hp bossa przez dmg gracza zaokraglajac w gore np turns... = (12 + 5) // 5 = 17 // 5 = 3turns
    # ale jesli odejmiemy 1 to koncowy wynik zwiekszy sie o 1: turns = (12 + 5 - 1) // 5 = 16 // 5 = 3
    # while boss_hp > 0:
    #     boss_hp -= player_dmg
    #     turns_to_kill_boss += 1
    turns_to_kill_player = (player_hp + boss_dmg - 1) // boss_dmg
    # while player_hp > 0:
    #     player_hp -= boss_dmg
    #     turns_to_kill_player += 1
    if turns_to_kill_boss <= turns_to_kill_player:
        result = 'Win'
    else:
        result = 'Loss'
    return result

print(combat(player_starting_data,boss_data))