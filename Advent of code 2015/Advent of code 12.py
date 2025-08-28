# --- Day 12: JSAbacusFramework.io ---
# Santa's Accounting-Elves need help balancing the books after a recent order. Unfortunately, their accounting software uses a peculiar storage format. 
# That's where you come in.

# They have a JSON document which contains a variety of things: arrays ([1,2,3]), objects ({"a":1, "b":2}), numbers, and strings. 
# Your first job is to simply find all of the numbers throughout the document and add them together.

# For example:

# [1,2,3] and {"a":2,"b":4} both have a sum of 6.
# [[[3]]] and {"a":{"b":4},"c":-1} both have a sum of 3.
# {"a":[-1,1]} and [-1,{"a":1}] both have a sum of 0.
# [] and {} both have a sum of 0.
# You will not encounter any strings containing numbers.

# What is the sum of all numbers in the document?

test_input = "abcdefgh" 
mode = "input"
#mode = "test_input"

if mode == "input":
    input_path = "./Advent of code/input_day12.txt"
    file = open(input_path)
    input = str(file.read())
    print("MODE = INPUT")
elif mode == "test_input":
    input = test_input
    print("MODE = TEST")

def is_it_a_number(c):
    numbers = []
    i = 0
    while i < len(c):
        num = '' # sprawdzamy number
        neg = False # zakładamy że jest dodatni
        while i < len(c) and (c[i] == '-' or c[i].isdigit()): # zrób tą logikę tylko w przypadku jeśli to co iterujesz to znak `-` albo liczba:
            if c[i] == '-': # jeśli przed numberem jest `-`, to znaczy że jest ujemny
                neg = True
                i += 1 # i przejdz na kolejny symbol
            else: # jeśli przed symbolem nie ma `-` (czyli jest liczba) to zrób to:
                while i < len(c) and c[i].isdigit(): # przejedź kolejną pętlą od tego miejsca bo trzeba sprawdzić czy kolejny znak to też liczba
                    num += c[i] # dodaj to co już znalazleś w poprzednim while do number
                    i += 1 # przejedź na kolejny znak
                if num: # jeśli num jest niepuste to:
                    n = int(num) # zmienna jest cyfrą
                    if neg: # plus jeśli jest ujemna to:
                        n = -n # jest ujemna
                    numbers.append(n) # do listy cyfr dodaj tą zmienną
                    num = '' # i zresetuj sobie number, bo jedziesz dalej zewnętrzny while
                    neg = False # i reset tego czy jest ujemna
                continue
        i += 1
    return numbers

print(sum(is_it_a_number(input)))

# --- Part Two ---
# Uh oh - the Accounting-Elves have realized that they double-counted everything red.

# Ignore any object (and all of its children) which has any property with the value "red". Do this only for objects ({...}), not arrays ([...]).

# [1,2,3] still has a sum of 6.
# [1,{"c":"red","b":2},3] now has a sum of 4, because the middle object is ignored.
# {"d":"red","e":[1,2,3,4],"f":5} now has a sum of 0, because the entire structure is ignored.
# [1,"red",5] has a sum of 6, because "red" in an array has no effect.

# o ja jebie kurwa
 
import json

def sum_no_red(obj):
    if isinstance(obj, dict): # sprawdz czy w jsonie są słowniki {} (objects)
        if "red" in obj.values(): # jeśli w wartościach obiektu znajduje się "red", zwróć go jako 0
            return 0
        return sum(sum_no_red(v) for v in obj.values()) # zwróć sumę v (values) dla v w values obiektu, w tym przypadku słownik (obj.values())
    elif isinstance(obj, list): # lub jeśli w jsonie są listy [] (arrays)
        return sum(sum_no_red(item) for item in obj) # zwróć sumę dla pozycji (item) w tym obiekcie, w tym przypadku array
    elif isinstance(obj, int): # lub jeśli w jsonie są luźne cyfry
        return obj # to je zwróć
    else:
        return 0 # w każdym innym wypadku zwróć 0 (stringi itp itd.)


input_path2 = "./Advent of code/input_day12.json"
file2 = open(input_path)
data = json.load(file2)

print(sum_no_red(data))