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
    cities.append(expr)
    target = target.strip() # tu też i wtedy z instrukcji np. 'AlphaCentauri to Tambi = 18' zostaje ci {('AlphaCentauri','Tambi') : 18}
    travel.update({tuple(expr):int(target)})

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

for x in travel: # dla każdego elementu w dictionary travel (czyli: {('AlphaCentauri','Tambi') : 18})
    travel_path = [] # zaczynamy sprawdzanie od zainicjowania ścieżki podróży
    distance_travelled = 0 # dystans od którego rozpoczynamy jest 0
    cities_visited = tuple()
    for a,b in travel: # i jednocześnie dla każdego elementu w dictionary travel:
        travel.get((a,b)) # zwróć parę miast, w formie pojedynczych zmiennych
        if a in cities_visited: # jeśli a znajduje się w liście miast odwiedzonych 
            continue # skip
        else:
            distance_travelled += travel.get(x) # dodaj do dystansu dystans dla tej pary miast
            travel_path.append((a,b)) # dodaj parę miast do listy travel_path
            cities_visited.add(b) # dodaj to miasto które odwiedziłeś do listy
            
    
    print(a)
    print(b)
    print([x])
    print(travel.get(x))

for a,b in travel:
    travel.get((a,b))
    print(a)
    print(b)
# print(cities)
# print(travel)

        #     try:  # spróbuj przeprowadzić operacje logiczne dla tej instrukcji
        #         if expr.isdigit(): # jeśli zmienna expr (czyli w przykladzie 123 -> x to będzie 123, basically lewa strona instrukcji to cyfra, to wtedy: )
        #             value = int(expr) # wartość tego sygnalu będzie rowna tej lewej stronie, tylko trzeba zamienić str na int '123' na 123
        #         elif "AND" in expr: # lub jeśli w zmiennej po lewej stronie jest wyrażenie "AND": 
        #             a, b = expr.split(" AND ") # podziel sobie zmienną po lewej stronie np. x AND y na dwie kolejne zmienne a,b
        #             a_val = int(a) if a.isdigit() else wires[a] # teraz oceniamy wartość wyrażenia, jeśli a będzie cyfrą, tak jak na przykład 123 -> x, to przypisz do tej wartości inta 123
        #             b_val = int(b) if b.isdigit() else wires[b] # w przeciwnym wypadku, czyli else, wyciągnij wartość tej zmiennej ze słownika wires
        #             value = (a_val & b_val) & 0xFFFF  # na koniec wartość tego sygnału będzie równa wyniku działania znaku & czyli AND w pythonie dla tych dwóch zmiennych
        #             # 0xFFFF to takie wyrażenie, które pilnuje, żeby ta wartość była 16-bit (między 0 a 65535), czyli na przykład jeśli wynikiem działania będzie 70000 to zwraca 65535
        #         elif "OR" in expr:
        #             a, b = expr.split(" OR ") # analogicznie jak w AND tylko zmieniasz w ostatnim value znaczek z & na |
        #             a_val = int(a) if a.isdigit() else wires[a]
        #             b_val = int(b) if b.isdigit() else wires[b]
        #             value = (a_val | b_val) & 0xFFFF
        #         elif "LSHIFT" in expr:
        #             a, n = expr.split(" LSHIFT ") # dalem n bo przy RSHIFT i LSHIFT jest zawsze cyferka po wyrażeniu
        #             a_val = wires[a] # jeśli jest już takie wyrażenie w slowniku wires, to wyciągnij jego wartość
        #             value = (a_val << int(n)) & 0xFFFF # zrób LSHIFT dla tej wartości przez n tylko trzeba ją zamienić na int
        #         elif "RSHIFT" in expr:
        #             a, n = expr.split(" RSHIFT ") # analogicznie
        #             a_val = int(a) if a.isdigit() else wires[a]
        #             value = (a_val >> int(n)) & 0xFFFF
        #         elif "NOT" in expr:
        #             a = expr.replace("NOT ", "") # w instrukcjach "NOT "(pamiętaj spacja) jest zawsze na początku, więc zamień NOT na puste miejsce i zostaje ci zawsze np z NOT ax -> ay, ax -> ay
        #             a_val = wires[a] 
        #             value = (~a_val) & 0xFFFF
        #         else:
        #             if expr in wires:
        #                 value = wires[expr] # jeśli po lewej stronie nie ma żadnego z powyższych działań to wyciągnij wartość dla tego wire ze słownika wires
        #             else:
        #                 raise KeyError(expr) # jeśli nie ma tego wyrażenia w słowniku to sie wykrzacz
        #         wires[target] = value # i po tych wszystkich działaniach przypisz wartość (value) do konkretnego (target) wire w słowniku wires
        #     except KeyError: # odnosimy się do tego keyerrora, który był w else
        #         next_pending.append(instruction) # dodaj tą instrukcję do listy oczekujących
        # if len(next_pending) == len(pending): # jeśli ilość instrukcji oczekujących jest taka sama jak lista oczekujących (np. w obu nic nie ma, bo nic się nie udało dodać)
        #     break # to wtedy przerwij pętle while pending:
        # pending = next_pending # i zacznij iterować następną oczekującą instrukcję, bo zappendowałeś 3 linijki wcześniej kolejną instrukcję       
