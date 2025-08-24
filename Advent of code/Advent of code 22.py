# --- Day 22: Wizard Simulator 20XX ---
# Little Henry Case decides that defeating bosses with swords and stuff is boring. Now he's playing the game with a wizard. 
# Of course, he gets stuck on another boss and needs your help again.

# In this version, combat still proceeds with the player and the boss taking alternating turns. 
# The player still goes first. Now, however, you don't get any equipment; instead, you must choose one of your spells to cast. 
# The first character at or below 0 hit points loses.

# Since you're a wizard, you don't get to wear armor, and you can't attack normally. 
# However, since you do magic damage, your opponent's armor is ignored, and so the boss effectively has zero armor as well. 
# As before, if armor (from a spell, in this case) would reduce damage below 1, it becomes 1 instead - that is, the boss' attacks always deal at least 1 damage.

# On each of your turns, you must select one of your spells to cast. 
# If you cannot afford to cast any spell, you lose. Spells cost mana; you start with 500 mana, but have no maximum limit. 
# You must have enough mana to cast a spell, and its cost is immediately deducted when you cast it. 
# Your spells are Magic Missile, Drain, Shield, Poison, and Recharge.

# Magic Missile costs 53 mana. It instantly does 4 damage.
# Drain costs 73 mana. It instantly does 2 damage and heals you for 2 hit points.
# Shield costs 113 mana. It starts an effect that lasts for 6 turns. 
# While it is active, your armor is increased by 7.
# Poison costs 173 mana. It starts an effect that lasts for 6 turns. 
# At the start of each turn while it is active, it deals the boss 3 damage.
# Recharge costs 229 mana. It starts an effect that lasts for 5 turns. 
# At the start of each turn while it is active, it gives you 101 new mana.
# Effects all work the same way. Effects apply at the start of both the player's turns and the boss' turns. 
# Effects are created with a timer (the number of turns they last); at the start of each turn, after they apply any effect they have, their timer is decreased by one. 
# If this decreases the timer to zero, the effect ends. You cannot cast a spell that would start an effect which is already active. 
# However, effects can be started on the same turn they end.

# For example, suppose the player has 10 hit points and 250 mana, and that the boss has 13 hit points and 8 damage:

# -- Player turn --
# - Player has 10 hit points, 0 armor, 250 mana
# - Boss has 13 hit points
# Player casts Poison.

# -- Boss turn --
# - Player has 10 hit points, 0 armor, 77 mana
# - Boss has 13 hit points
# Poison deals 3 damage; its timer is now 5.
# Boss attacks for 8 damage.

# -- Player turn --
# - Player has 2 hit points, 0 armor, 77 mana
# - Boss has 10 hit points
# Poison deals 3 damage; its timer is now 4.
# Player casts Magic Missile, dealing 4 damage.

# -- Boss turn --
# - Player has 2 hit points, 0 armor, 24 mana
# - Boss has 3 hit points
# Poison deals 3 damage. This kills the boss, and the player wins.
# Now, suppose the same initial conditions, except that the boss has 14 hit points instead:

# -- Player turn --
# - Player has 10 hit points, 0 armor, 250 mana
# - Boss has 14 hit points
# Player casts Recharge.

# -- Boss turn --
# - Player has 10 hit points, 0 armor, 21 mana
# - Boss has 14 hit points
# Recharge provides 101 mana; its timer is now 4.
# Boss attacks for 8 damage!

# -- Player turn --
# - Player has 2 hit points, 0 armor, 122 mana
# - Boss has 14 hit points
# Recharge provides 101 mana; its timer is now 3.
# Player casts Shield, increasing armor by 7.

# -- Boss turn --
# - Player has 2 hit points, 7 armor, 110 mana
# - Boss has 14 hit points
# Shield's timer is now 5.
# Recharge provides 101 mana; its timer is now 2.
# Boss attacks for 8 - 7 = 1 damage!

# -- Player turn --
# - Player has 1 hit point, 7 armor, 211 mana
# - Boss has 14 hit points
# Shield's timer is now 4.
# Recharge provides 101 mana; its timer is now 1.
# Player casts Drain, dealing 2 damage, and healing 2 hit points.

# -- Boss turn --
# - Player has 3 hit points, 7 armor, 239 mana
# - Boss has 12 hit points
# Shield's timer is now 3.
# Recharge provides 101 mana; its timer is now 0.
# Recharge wears off.
# Boss attacks for 8 - 7 = 1 damage!

# -- Player turn --
# - Player has 2 hit points, 7 armor, 340 mana
# - Boss has 12 hit points
# Shield's timer is now 2.
# Player casts Poison.

# -- Boss turn --
# - Player has 2 hit points, 7 armor, 167 mana
# - Boss has 12 hit points
# Shield's timer is now 1.
# Poison deals 3 damage; its timer is now 5.
# Boss attacks for 8 - 7 = 1 damage!

# -- Player turn --
# - Player has 1 hit point, 7 armor, 167 mana
# - Boss has 9 hit points
# Shield's timer is now 0.
# Shield wears off, decreasing armor by 7.
# Poison deals 3 damage; its timer is now 4.
# Player casts Magic Missile, dealing 4 damage.

# -- Boss turn --
# - Player has 1 hit point, 0 armor, 114 mana
# - Boss has 2 hit points
# Poison deals 3 damage. This kills the boss, and the player wins.
# You start with 50 hit points and 500 mana points. 
# The boss's actual stats are in your puzzle input.
# What is the least amount of mana you can spend and still win the fight? (Do not include mana recharge effects as "spending" negative mana.)

# test_data = 10

# mode = "input"
# mode = "test_input"
# if mode == "input":
#     input_path = "./Advent of code/input_day21.txt"
#     file = open(input_path)
#     data = file.read().splitlines()
#     print("MODE = INPUT")
# elif mode == "test_input":
#     data = test_data
#     print("MODE = TEST")

# Magic Missile costs 53 mana. It instantly does 4 damage.
# Drain costs 73 mana. It instantly does 2 damage and heals you for 2 hit points.
# Shield costs 113 mana. It starts an effect that lasts for 6 turns. 
# While it is active, your armor is increased by 7.
# Poison costs 173 mana. It starts an effect that lasts for 6 turns. 
# At the start of each turn while it is active, it deals the boss 3 damage.
# Recharge costs 229 mana. It starts an effect that lasts for 5 turns. 
# At the start of each turn while it is active, it gives you 101 new mana.

spells = {
    'Shield':       {'timer': 6, 'effect' : 7 , 'cost': 113},
    'Poison' :      {'timer': 6, 'effect' : 3 , 'cost': 173},
    'Recharge':     {'timer': 5, 'effect' :101, 'cost': 229},
    'Magic missile':{'timer': 0, 'effect' : 4 , 'cost': 53},
    'Drain':        {'timer': 0, 'effect' : 2 , 'cost': 73},
    }

spell_cost_list = [x['cost'] for x in spells.values()]
spell_name_list = [x for x in spells]
# print(spell_name_list)
player_starting_data = {'Hit Points': 50, 'Damage': 0, 'Mana': 500, 'Armor': 0}
boss_data = {'Hit Points': 71, 'Damage': 10}

def cast(spell_name):
    timer = spells[spell_name].get('timer')
    cost = spells[spell_name].get('cost')
    effect = spells[spell_name].get('effect')
    return spell_name, timer, effect, cost

def combat(player_data, boss_data):
    player_armor = player_data['Armor']
    player_hp = player_data['Hit Points']
    boss_hp = boss_data['Hit Points']
    player_mana = player_data['Mana']
    boss_dmg = max(1, boss_data['Damage'] - player_armor)
    player_dmg = 0
    # znajdz wieksza wartosc max(), miedzy wartoscia 1 a drugim argumentem - minimalny dmg jaki mozna zadac jest 1
    active_spell_effects = {'Debuff' : {'timer': float('inf'), 'effect' : 1}}
    # print(f"Available spells: ")
    # for x in spells:
        # print(x)
    turn_count = 1
    total_mana_cost = 0
    # print(f"---------------------- Turn {turn_count}. Your turn ------------------------\nYour current HP: {player_hp}\nYour current MP: {player_mana}\nArmor: {player_armor}\n\nCurrent boss hp: {boss_hp}\n")
    while True:
        while True:
            player_hp -= 1
            # print(f"The debuff ticks! HP: {player_hp}\n")
                # HARDMODE
            if player_hp <= 0:
                # print("You lose... Try again?")
                result = 'Loss'
                break
            # spell = input("Choose a spell to cast - just type the spell's name: \n").strip().casefold().capitalize()
            import random
            spell = random.choice(spell_name_list)
            if (spell in spells.keys()) and (player_mana >= spells[spell].get('cost') and (spell not in active_spell_effects)):
                spell_cast, timer, effect, cost = cast(spell)
                player_mana -= cost
                total_mana_cost += cost
                if spell_cast == 'Magic missile':
                    player_dmg = effect
                if spell_cast == 'Drain':
                    player_dmg = effect
                    player_hp += effect
                if timer > 0:
                    active_spell_effects.update({spell_cast : {'timer': timer, 'effect' : effect}})
                    player_dmg = 0 
                # print(f"----------------------------------------------------------------------\n                   *******You cast {spell}!*******          \n----------------------------------------------------------------------\n")
                break
            if player_mana < min(spell_cost_list):
                # print("\n************************* You are out of mana... ****************************\n---------------------- Basic attack! ----------------------------------\n")
                player_dmg = 1
                break
            if spell == 'None':
                # print(f"\n---------------------- Basic attack! ----------------------------------\n")
                player_dmg = 1
                break
            if spell not in spells:
                # print("\nSpell not recognized, are you sure you typed in the correct name? \n Try again. If you want to use your basic attack, type in \"none\".\n")
                continue
            if player_mana < spells[spell].get('cost'):
                # print("\n************************ Not enough mana! *************************\n\n--------------------------- Try a different spell: ---------------------------\n")  
                continue
            if spell in active_spell_effects:
                # print("\n************************ Spell already active. *************************\n\n--------------------------- Try a different spell: ---------------------------\n")  
                continue
            break

        if 'Shield' in active_spell_effects:
            player_armor = active_spell_effects['Shield']['effect']
        if 'Shield' not in active_spell_effects:
            player_armor = 0
        if 'Recharge' in active_spell_effects:
            player_mana += active_spell_effects['Recharge']['effect']
            # print(f'************* Recharge refills {spells['Recharge'].get('effect')} of your mana! *****************\n')
        # if spell == 'Drain':
        #     print(f'Drain heals you for {spells['Drain'].get('effect')} hp.\n')
        boss_hp -= player_dmg
        # if player_dmg > 0:
        #     print(f"You deal: {player_dmg} damage!\n")
        # print(f"Boss: {boss_hp} hp \nActive spells: {list(active_spell_effects.keys())}\n")
        turn_count += 1
        # print(f"---------------------- Turn {turn_count}. Boss's turn. ----------------------\n")
        player_hp -= 1
        # print(f"The debuff ticks! HP: {player_hp}\n")
            # HARDMODE
        if player_hp <= 0:
            # print("You lose... Try again?")
            result = 'Loss'
            break
        for spell, data in list(active_spell_effects.items()):
            data['timer'] -= 1
            if data['timer'] <= 0:
                active_spell_effects.pop(spell)
                # print(f'{spell} wears off.\n')
        if 'Poison' in active_spell_effects:
            for spell, data in list(active_spell_effects.items()):
                if data['timer'] != spells['Poison'].get('timer'):
                    boss_hp -= spells['Poison'].get('effect')
                    # print(f'************* Poison deals {spells['Poison'].get('effect')} damage!*************\nCurrent boss hp: {boss_hp}\n')
                    break  
                else:
                    continue
        if boss_hp <= 0:
            # print("You win!")
            result = 'Win'
            break
        if 'Shield' in active_spell_effects:
            player_armor = active_spell_effects['Shield']['effect']
        if 'Shield' not in active_spell_effects:
            player_armor = 0
        if 'Recharge' in active_spell_effects:
            player_mana += active_spell_effects['Recharge']['effect']
            # print(f'************* Recharge refills {spells['Recharge'].get('effect')} of your mana! *****************\n')
        player_hp -= boss_dmg - player_armor
        # print(f"Boss deals:  {boss_dmg - player_armor} damage!\nActive spells: {list(active_spell_effects.keys())}\n")
        turn_count += 1
        # print(f"---------------------- Turn {turn_count}. Your turn. ------------------------\n\nHP: {player_hp}\nMP: {player_mana}\nArmor: {player_armor}\nActive spells: {list(active_spell_effects.keys())}\n")
        if 'Poison' in active_spell_effects:
            for spell, data in list(active_spell_effects.items()):
                if data['timer'] != spells['Poison'].get('timer'):
                    boss_hp -= spells['Poison'].get('effect')
                    # print(f'************* Poison deals {spells['Poison'].get('effect')} damage!*************\nCurrent boss hp: {boss_hp}\n')
                    break
                else:
                    continue
        if boss_hp <= 0:
            # print("You win!")
            result = 'Win'
            break
        for spell, data in list(active_spell_effects.items()):
            data['timer'] -= 1
            if data['timer'] <= 0:
                active_spell_effects.pop(spell)
                # print(f'{spell} wears off.\n')
        if player_hp <= 0:
            # print("You lose... Try again?")
            result = 'Loss'
            break
    return result, total_mana_cost

# combat_result = combat(player_starting_data, boss_data)
# if combat_result == 'Loss':
#     decision = input('Y/N? ').capitalize()
#     if decision == 'Y':
#         combat(player_starting_data,boss_data)
#     else:
#         print('Loser')
mana_costs = []
def autobattler():
    player_data = player_starting_data.copy()
    boss_auto_data = boss_data.copy()
    result, total_mana_cost = combat(player_data, boss_auto_data)
    if result == 'Win':
        mana_costs.append(total_mana_cost)
    else:
        return mana_costs
while len(mana_costs) < 5:
    autobattler()
print(min(mana_costs))
# minimum cost dla mojego data 1791 ale zla odp, 1824 correct

# --- Part Two ---
# On the next run through the game, you increase the difficulty to hard.

# At the start of each player turn (before any other effects apply), you lose 1 hit point. If this brings you to or below 0 hit points, you lose.

# With the same starting stats for you and the boss, what is the least amount of mana you can spend and still win the fight?
