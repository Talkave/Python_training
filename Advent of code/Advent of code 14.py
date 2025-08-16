# --- Day 14: Reindeer Olympics ---
# This year is the Reindeer Olympics! Reindeer can fly at high speeds, but must rest occasionally to recover their energy. Santa would like to know which of his reindeer is fastest, and so he has them race.

# Reindeer can only either be flying (always at their top speed) or resting (not moving at all), and always spend whole seconds in either state.

# For example, suppose you have the following Reindeer:

# Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
# Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
# After one second, Comet has gone 14 km, while Dancer has gone 16 km. After ten seconds, Comet has gone 140 km, while Dancer has gone 160 km. 
# On the eleventh second, Comet begins resting (staying at 140 km), and Dancer continues on for a total distance of 176 km. 
# On the 12th second, both reindeer are resting. They continue to rest until the 138th second, when Comet flies for another ten seconds. 
# On the 174th second, Dancer flies for another 11 seconds.

# In this example, after the 1000th second, both reindeer are resting, and Comet is in the lead at 1120 km (poor Dancer has only gotten 1056 km by that point). 
# So, in this situation, Comet would win (if the race ended at 1000 seconds).

# Given the descriptions of each reindeer (in your puzzle input), after exactly 2503 seconds, what distance has the winning reindeer traveled?

test_data = 2503
mode = "input"
#mode = "test_input"

if mode == "input":
    input_path = "./Advent of code/input_day14.txt"
    file = open(input_path)
    data = file.read()
    print("MODE = INPUT")
elif mode == "test_input":
    data = test_data
    print("MODE = TEST")


reindeer_dict = {} # {"Name":name,"Velocity":v,"Travel time":t,"Rest_Time":seconds}
for line in data.strip().splitlines():
    line = line.strip().replace('.','')
    segment = line.split()
    # print(segment)
    name = segment[0]
    velocity = int(segment[3])
    travel_time = int(segment[6])
    rest_time = int(segment[-2])
    reindeer_dict[name] = {
        "Velocity" : velocity, 
        "Travel time": travel_time, 
        "Rest time": rest_time
    } 

def reindeer(Name): #comet:
    seconds = 0
    distance = 0
    score = 0
    i = 1
    while seconds < test_data: # śledzimy sekundy
        for x, obj in reindeer_dict.items():
                t = obj.get("Travel time") # tyle może lecieć
                v = obj.get("Velocity") # z taką prędkością
                r = obj.get("Rest time")
                if x == Name:
                    if i % t == 0:
                        s = v*t # V = S/T => S = V*T
                        seconds += r # czekaj 127 seconds po każdym 10 seconds
                        distance += s
                    seconds += 1
        i += 1
    return distance
final_list = []
for x in reindeer_dict.keys():
    final_list.append(reindeer(x))
final_list.sort(reverse=True)
print(final_list)
# print(final_list[0])

# --- Part Two ---
# Seeing how reindeer move in bursts, Santa decides he's not pleased with the old scoring system.

# Instead, at the end of each second, he awards one point to the reindeer currently in the lead. 
# (If there are multiple reindeer tied for the lead, they each get one point.) 
# He keeps the traditional 2503 second time limit, of course, as doing otherwise would be entirely ridiculous.

# Given the example reindeer from above, after the first second, Dancer is in the lead and gets one point. 
# He stays in the lead until several seconds into Comet's second burst: after the 140th second, Comet pulls into the lead and gets his first point. 
# Of course, since Dancer had been in the lead for the 139 seconds before that, he has accumulated 139 points by the 140th second.

# After the 1000th second, Dancer has accumulated 689 points, while poor Comet, our old champion, only has 312. 
# So, with the new scoring system, Dancer would win (if the race ended at 1000 seconds).

# Again given the descriptions of each reindeer (in your puzzle input), after exactly 2503 seconds, how many points does the winning reindeer have?

total_time = test_data  # e.g. 2503

distances = {name: 0 for name in reindeer_dict}
scores = {name: 0 for name in reindeer_dict}

for second in range(1, total_time+1):
    for name, info in reindeer_dict.items():
        t = info["Travel time"]
        v = info["Velocity"]
        r = info["Rest time"]
        cycle = t + r
        which_in_cycle = (second-1) % cycle
        if which_in_cycle < t:
            distances[name] += v
    max_distance = max(distances.values())
    for name, dist in distances.items():
        if dist == max_distance:
            scores[name] += 1
            
print(scores)

