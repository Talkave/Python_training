test_input = "2x3x4\n1x1x10"
mode = "input"
#mode = "test_input"

if mode == "input":
    input_path = "./Advent of code/input_day2.txt"
    file = open(input_path)
    input = file.read()
elif mode == "test_input":
    input = test_input

def create_dimension_list(input):
    dimension_list = input.split("\n")
    dimensions = []
    for element in dimension_list:
        dimensions.append(element.split("x"))
    #print(dimensions)
    return dimensions

def surface_area_calc(dimensions): #
    side1 = (int(dimensions[0])*int(dimensions[1]))
    side2 = (int(dimensions[0])*int(dimensions[2]))
    side3 = (int(dimensions[1])*int(dimensions[2]))
    total_sides=sorted([side1,side2,side3])
    total_area= total_sides[0]*3 + total_sides[1]*2 + total_sides[2]*2
    return total_area

def surface_area_circ(dimensions): #
    length1 = int(dimensions[0])
    length2 = int(dimensions[1])
    length3 = int(dimensions[2])
    volume = length1*length2*length3
    total_sides=sorted([length1,length2,length3])
    total_area= total_sides[0]*2 + total_sides[1]*2 + volume
    return total_area

dimension_list = create_dimension_list(input)
sum = 0
for element in dimension_list:
    sum = sum + surface_area_circ(element)
print(sum)
