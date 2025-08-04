# --- Day 9: All in a Single Night ---
# Every year, Santa manages to deliver all of his presents in a single night.

# This year, however, he has some new locations to visit; 
# his elves have provided him the distances between every pair of locations. 
# He can start and end at any two (different) locations he wants, but he must visit each location exactly once. 
# What is the shortest distance he can travel to achieve this?

# For example, given the following distances:

# London to Dublin = 464
# London to Belfast = 518
# Dublin to Belfast = 141
# The possible routes are therefore:

# Dublin -> London -> Belfast = 982
# London -> Dublin -> Belfast = 605
# London -> Belfast -> Dublin = 659
# Dublin -> Belfast -> London = 659
# Belfast -> Dublin -> London = 605
# Belfast -> London -> Dublin = 982
# The shortest of these is London -> Dublin -> Belfast = 605, and so the answer is 605 in this example.

# What is the distance of the shortest route?

test_input = [] 
mode = "input"
# mode = "test_input"

if mode == "input":
    input_path = "./Advent of code/input_day9.txt"
    file = open(input_path)
    input = file.read().splitlines()
    print("MODE = INPUT")
elif mode == "test_input":
    input = test_input
    print("MODE = TEST")

travel={}
cities=list()

for element in input: # dla każdego elementu w input:
    expr, target = element.split(' = ') # podziel instrukcje na expr i target w miejscu gdzie jest =
    expr = expr.split(" to ")
    target = int(target.strip()) # tu z instrukcji np. 'AlphaCentauri to Tambi = 18' zostaje ci {('AlphaCentauri','Tambi') : 18} i przy okazji ta wartość 18 od razu jest intem
    # cities.append(expr)
    a,b = expr # podziel pary miast na pojedyncze miasta do permutacji
    travel[(a,b)] = target 
    travel[(b,a)] = target
    cities.extend([a,b])
    # travel.update({tuple(expr):int(target)}) # tu tworzymy słownik z inputu

    # {
# ('Faerun', 'Norrath'): 129, 
# ('Faerun', 'Tristram'): 58, 
# ('Faerun', 'AlphaCentauri'): 13, 
# ('Faerun', 'Arbre'): 24, 
# ('Faerun', 'Snowdin'): 60, 
# ('Faerun', 'Tambi'): 71, 
# ('Faerun', 'Straylight'): 67, 
# ('Norrath', 'Tristram'): 142, 
# ('Norrath', 'AlphaCentauri'): 15, 
# ('Norrath', 'Arbre'): 135, 
# ('Norrath', 'Snowdin'): 75, 
# ('Norrath', 'Tambi'): 82, 
# ('Norrath', 'Straylight'): 54, 
# ('Tristram', 'AlphaCentauri'): 118, 
# ('Tristram', 'Arbre'): 122, 
# ('Tristram', 'Snowdin'): 103, 
# ('Tristram', 'Tambi'): 49, 
# ('Tristram', 'Straylight'): 97, 
# ('AlphaCentauri', 'Arbre'): 116, 
# ('AlphaCentauri', 'Snowdin'): 12, 
# ('AlphaCentauri', 'Tambi'): 18, 
# ('AlphaCentauri', 'Straylight'): 91, 
# ('Arbre', 'Snowdin'): 129, 
# ('Arbre', 'Tambi'): 53, 
# ('Arbre', 'Straylight'): 40, 
# ('Snowdin', 'Tambi'): 15, 
# ('Snowdin', 'Straylight'): 99, 
# ('Tambi', 'Straylight'): 70
# }

def permutacje(city_list): # robimy każdą możliwą ścieżkę w ogóle
    if len(city_list) == 0:
        return [[]] # zaczynamy od inputu pustego
    result = []
    for element in range(len(city_list)): # tworzymy permutacje dla każdego elementu listy
        first = city_list[element] # element listy na którym iterujemy
        rest = city_list[:element] + city_list[element+1:] # pozostałe elementy listy z lewej i prawej strony
        for perm in permutacje(rest): # przeprowadź zdefiniowaną powyżej funkcję dla pozostałych elementów listy
            result.append([first] + perm) # stwórz końcowy rezultat zrobiony z elementu listy z ktorego iterowałeś i pozostałych permutacji 
    return result

# for para in cities:
#     for element in para:
#         city_list.add(element) # te 3 linijki robią to samo co linijka poniżej
# city_set = {element for para in cities for element in para}
city_list=list(set(cities)) # szybka metoda na zrobienie zestawu unikatowych miast
city_perm = permutacje(city_list)

# print(city_perm)
# print(city_list)
shortest_distance = float('inf') # zamiast magic numberu można dać nieskończoność w ten sposób
shortest_path = []
longest_distance = 0
longest_path = []

for permutacja in city_perm: # dla każdego elementu w dictionary travel (czyli: {('AlphaCentauri','Tambi') : 18})
    distance_travelled = 0 # dystans od którego rozpoczynamy jest 0
    valid_path = True
    for index in range(len(permutacja) - 1): # i jednocześnie dla każdego indeksu w liście permutacji:
        travel_try = (permutacja[index], permutacja[index+1]) # bierzemy z permutacji pierwszą parę miast
        if travel_try in travel: # jeśli próba przejścia znajduje się w słowniku travel to:
            distance_travelled += travel[travel_try] # do dystansu, który przeszliśmy dodaj wartość przypisaną do tego indeksu w słowniku
        else: # jeśli nie ma takiej pary:
            valid_path = False
            break # nie ma drogi między tymi miastami i przerwij pętle   
    if valid_path and distance_travelled < shortest_distance: # jeśli jest taka ścieżka i dystans który przeszliśmy jest mniejszy niż przy innych które sprawdzaliśmy, to przypisz jego wartość do najkrótszego dystansu
        shortest_distance = distance_travelled
        shortest_path = permutacja # i zwróć permutacje dla tego dystansu, bo to będzie najkrótsza droga
    if valid_path and distance_travelled > longest_distance: # jeśli jest taka ścieżka i dystans który przeszliśmy jest większy niż przy innych które sprawdzaliśmy, to przypisz jego wartość do najdłuższego dystansu
        longest_distance = distance_travelled
        longest_path = permutacja # i zwróć permutacje dla tego dystansu, bo to będzie najdłuższa droga

print(shortest_distance)
print(shortest_path) 

# --- Part Two ---
# The next year, just to show off, Santa decides to take the route with the longest distance instead.

# He can still start and end at any two (different) locations he wants, and he still must visit each location exactly once.

# For example, given the distances above, the longest route would be 982 via (for example) Dublin -> London -> Belfast.

# What is the distance of the longest route?

print(longest_distance)
print(longest_path)


# ---- TESTY ----
#     print(a)
#     print(b)
#     print([x])
#     print(travel.get(x))

# for a,b in travel:
#     travel.get((a,b))
#     print(a)
#     print(b)
# print(cities)
# print(travel)       