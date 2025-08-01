"""--- Day 7: Some Assembly Required ---
This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates! 

Unfortunately, little Bobby is a little under the recommended age range, and he needs help assembling the circuit.

Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535). 

A signal is provided to each wire by a gate, another wire, or some specific value. 

Each wire can only get a signal from one source, but can provide its signal to multiple destinations. A gate provides no signal until all of its inputs have a signal.

The included instructions booklet describes how to connect the parts together: 

x AND y -> z means to connect wires x and y to an AND gate, and then connect its output to wire z.

For example:

123 -> x means that the signal 123 is provided to wire x.
x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.
Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). 
If, for some reason, you'd like to emulate the circuit instead, almost all programming languages (for example, C, JavaScript, or Python) provide operators for these gates.

For example, here is a simple circuit:

123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
After it is run, these are the signals on the wires:

d: 72
e: 507
f: 492
g: 114
h: 65412
i: 65079
x: 123
y: 456
In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?"""

test_input = "123 -> x\n456 -> y\nx AND y -> d\nx OR y -> e\nx LSHIFT 2 -> f\ny RSHIFT 2 -> g\nNOT x -> h\nNOT y -> i"
mode = "input"
#mode = "test_input"

if mode == "input":
    input_path = "./Advent of code/input_day7.txt"
    file = open(input_path)
    input = file.read()
    print("MODE = INPUT")
elif mode == "test_input":
    input = test_input
    print("MODE = TEST")

# bitwise gates in python:
# >> RSHIFT
# << LSHIFT
# ~ NOT
# | OR
# & AND
# ^ XOR

def provide(instructions, wires): # funkcja dla ktorej podajemy instrukcje które dodamy do dictionary o nazwie wires, który będzie stworzony z instrukcji, dla każdego wire będzie przypisana wartość np. a:46
    pending = instructions[:] # stwórz kopię listy instructions żebyśmy mogli sobie działać na tej liście bez zmian w instrukcjach
    while pending: # zawsze true
        next_pending = []
        for instruction in pending: # dla każdego elementu w pending:
            expr, target = instruction.split('->') # podziel instrukcje na expr i target w miejscu gdzie jest ->
            expr = expr.strip() # wywal spacje
            target = target.strip() # tu też i wtedy z instrukcji np. 123 -> x zostaje ci (123,x)
            try:  # spróbuj przeprowadzić operacje logiczne dla tej instrukcji
                if expr.isdigit(): # jeśli zmienna expr (czyli w przykladzie 123 -> x to będzie 123, basically lewa strona instrukcji to cyfra, to wtedy: )
                    value = int(expr) # wartość tego sygnalu będzie rowna tej lewej stronie, tylko trzeba zamienić str na int '123' na 123
                elif "AND" in expr: # lub jeśli w zmiennej po lewej stronie jest wyrażenie "AND": 
                    a, b = expr.split(" AND ") # podziel sobie zmienną po lewej stronie np. x AND y na dwie kolejne zmienne a,b
                    a_val = int(a) if a.isdigit() else wires[a] # teraz oceniamy wartość wyrażenia, jeśli a będzie cyfrą, tak jak na przykład 123 -> x, to przypisz do tej wartości inta 123
                    b_val = int(b) if b.isdigit() else wires[b] # w przeciwnym wypadku, czyli else, wyciągnij wartość tej zmiennej ze słownika wires
                    value = (a_val & b_val) & 0xFFFF  # na koniec wartość tego sygnału będzie równa wyniku działania znaku & czyli AND w pythonie dla tych dwóch zmiennych
                    # 0xFFFF to takie wyrażenie, które pilnuje, żeby ta wartość była 16-bit (między 0 a 65535), czyli na przykład jeśli wynikiem działania będzie 70000 to zwraca 65535
                elif "OR" in expr:
                    a, b = expr.split(" OR ") # analogicznie jak w AND tylko zmieniasz w ostatnim value znaczek z & na |
                    a_val = int(a) if a.isdigit() else wires[a]
                    b_val = int(b) if b.isdigit() else wires[b]
                    value = (a_val | b_val) & 0xFFFF
                elif "LSHIFT" in expr:
                    a, n = expr.split(" LSHIFT ") # dalem n bo przy RSHIFT i LSHIFT jest zawsze cyferka po wyrażeniu
                    a_val = wires[a] # jeśli jest już takie wyrażenie w slowniku wires, to wyciągnij jego wartość
                    value = (a_val << int(n)) & 0xFFFF # zrób LSHIFT dla tej wartości przez n tylko trzeba ją zamienić na int
                elif "RSHIFT" in expr:
                    a, n = expr.split(" RSHIFT ") # analogicznie
                    a_val = int(a) if a.isdigit() else wires[a]
                    value = (a_val >> int(n)) & 0xFFFF
                elif "NOT" in expr:
                    a = expr.replace("NOT ", "") # w instrukcjach "NOT "(pamiętaj spacja) jest zawsze na początku, więc zamień NOT na puste miejsce i zostaje ci zawsze np z NOT ax -> ay, ax -> ay
                    a_val = wires[a] 
                    value = (~a_val) & 0xFFFF
                else:
                    if expr in wires:
                        value = wires[expr] # jeśli po lewej stronie nie ma żadnego z powyższych działań to wyciągnij wartość dla tego wire ze słownika wires
                    else:
                        raise KeyError(expr) # jeśli nie ma tego wyrażenia w słowniku to sie wykrzacz
                wires[target] = value # i po tych wszystkich działaniach przypisz wartość (value) do konkretnego (target) wire w słowniku wires
            except KeyError: # odnosimy się do tego keyerrora, który był w else
                next_pending.append(instruction) # dodaj tą instrukcję do listy oczekujących
        if len(next_pending) == len(pending): # jeśli ilość instrukcji oczekujących jest taka sama jak lista oczekujących (np. w obu nic nie ma, bo nic się nie udało dodać)
            break # to wtedy przerwij pętle while pending:
        pending = next_pending # i zacznij iterować następną oczekującą instrukcję, bo zappendowałeś 3 linijki wcześniej kolejną instrukcję       
# Przykład:
# wires = {}
# provide("123 -> x", wires)
# print(wires) pokaże {'x': 123}
instructions = input.splitlines()
wires = {}
provide(instructions, wires)
# print(wires) # do testów
print(wires["a"])

"""--- --- Part Two ---
Now, take the signal you got on wire a, 
override wire b to that signal, 
and reset the other wires (including wire a). 
What new signal is ultimately provided to wire a?"""

a_value = wires["a"] # przypisz sobie wartość którą dostałeś z part 1
instructions2 = instructions[:] # robimy sobie kopie instrukcji
for line in instructions2: # ale:
    if line.strip().endswith(" -> b"): 
        instructions2.remove(line) # wywalamy sygnał przypisywany do b
instructions2.append(f"{a_value} -> b") # i dodajemy sobie nową instrukcję 
wires = {} # resetujemy wires
provide(instructions2, wires) # i przeprowadzamy logikę na nowych instrukcjach

print(wires["a"]) # voila