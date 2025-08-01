"""--- Day 6: Probably a Fire Hazard ---
Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided to deploy one million lights in a 1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the ideal lighting configuration.

Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.

For example:

turn on 0,0 through 999,999 would turn on (or leave on) every light.
toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.
After following the instructions, how many lights are lit?

--- Part Two ---
You just finish implementing your winning light pattern when you realize you mistranslated Santa's message from Ancient Nordic Elvish.

The light grid you bought actually has individual brightness controls; each light can have a brightness of zero or more. The lights all start at zero.

The phrase turn on actually means that you should increase the brightness of those lights by 1.

The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.

The phrase toggle actually means that you should increase the brightness of those lights by 2.

What is the total brightness of all lights combined after following Santa's instructions?

For example:

turn on 0,0 through 0,0 would increase the total brightness by 1.
toggle 0,0 through 999,999 would increase the total brightness by 2000000."""

test_input = "turn on 0,0 through 2,2\nturn off 500,500 through 999,999\ntoggle 300,300 through 500,500" # 40410 lights
#mode = "input"
mode = "test_input"

if mode == "input":
    input_path = "Python-training/Python-training/Advent of code/input_day6.txt"
    file = open(input_path)
    input = file.read()
    print("MODE = INPUT")
elif mode == "test_input":
    input = test_input
    print("MODE = TEST")

coordinates = [(x,y) for x in range(1000) for y in range(1000)]
light_states = {coord: 0 for coord in coordinates}
def turn_on(coord):
    
    light_states[coord] = 1

def turn_off(coord):
    if coord != -1:
        light_states[coord] = 0

def toggle(coord):
    light_states[coord] = 1 - light_states[coord]

def instruction_processor(input):
    for line in input.splitlines(): # potnij input (instrukcje) na line, czyli pojedyncze linijki
        if line.startswith("turn on"): # jeśli instrukcja zaczyna się od turn on to zrób to:
            action = turn_on
            coord = line[len("turn on "):] # obetnij line, czyli rozpatrywaną linijkę od momentu kiedy skończy się wyrażenie turn on aż do końca
        elif line.startswith("turn off"): # analogicznie do poprzedniego
            action = turn_off
            coord = line[len("turn off "):] # analogicznie do poprzedniego
        elif line.startswith("toggle"): # analogicznie do poprzedniego
            action = toggle
            coord = line[len("toggle "):] # analogicznie do poprzedniego
        else:
            continue
        start, end = coord.split(" through ") # teraz w inpucie mamy np. (500,500 through 900,900), wytnij through i będą startowe lampki start = "500,500" do końcowych lampek end = "900,900"
        x_start, y_start = map(int, start.split(",")) # teraz mamy coś takiego dla zmiennej start "500,500" i ta funkcja map(int, start.split(",")) ciacha ten string przez "," i od razu przypisuje (mapuje) pierwsze 500 do x_start i drugie 500 do y_start
        x_end,y_end = map(int, end.split(",")) # analogiczne jw.
        for x in range(x_start,x_end+1): # no i teraz zawiązujemy wszystko co chcieliśmy zrobić dla obu współrzędnych - wykonaj dla każdego x w zakresie od start do końca +1 (bo indeksy)
            for y in range(y_start,y_end+1): # potem to samo też dla y, bo musi być jedno z drugim razem zrobione
                action((x,y)) # action zdefiniowane funkcjami zdefiniowanymi na początku programu     

instruction_processor(input)
print(sum(light_states.values())) # wyprintuj sumę wszystkich 1 (czyli podświetlonych lampek)


