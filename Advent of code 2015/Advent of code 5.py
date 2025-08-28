"""--- Day 5: Doesn't He Have Intern-Elves For This? ---
Santa needs help figuring out which strings in his text file are naughty or nice.

A nice string is one with all of the following properties:

It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
For example:

ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
jchzalrnumimnmhp is naughty because it has no double letter.
haegwjzuvuyypxyu is naughty because it contains the string xy.
dvszwmarrgswjxmb is naughty because it contains only one vowel.
How many strings are nice?
--- Part Two ---
Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.

Now, a nice string is one with all of the following properties:

It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
For example:

qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.
How many strings are nice under these new rules?
"""
#test_input = "ugknbfddgicrmopn" # nice
test_input = "qjhvhtzxzqqjkmpb\nxxyxx\nuurcxstgmygtbstg\nieodomkazucvgmuy" # 2
mode = "input"
#mode = "test_input"


if mode == "input":
    input_path = "./Advent of code/input_day5.txt"
    file = open(input_path)
    input = file.read()
elif mode == "test_input":
    input = test_input

banned = ["ab", "cd", "pq", "xy"]
allowed = ["aa","bb","cc","dd","ee","ff","gg","hh","ii","jj","kk","ll","mm","nn","oo","pp","qq","rr","ss","tt","uu","ww","vv","xx","yy","zz"]
vowel_list = ['a','e','i','o','u']
def create_word_list(input):
    word_list = input.split("\n")
    return word_list

word_list = create_word_list(input)

"""for word in word_list:
    if any(bad in word for bad in banned):
        #print(word)
        word_list.remove(word)
        #print(word_list)
    else:
        continue
for word in word_list:
    if any(good in word for good in allowed):
        continue
    else:
        #print(word)
        word_list.remove(word)
        #print(word_list) # to nie działa, lepiej dodawać do listy niż usuwać w trakcie iterowania"""

listy_samoglosek = ['a','e','i','o','u']
final_list1 = []
for word in word_list:  
    iterator = 0 
    for litera in word:
        if litera in listy_samoglosek:
            iterator+=1
    if iterator >= 3 :
        if not any(bad in word for bad in banned):
            if any(good in word for good in allowed):
                final_list1.append(word)
                
final_list2=[]
for word in word_list:
    for i in range(len(word)-1):
        pair = word[i]+word[i+1]
        new_word = word[i+2:]
        if pair in new_word:
            for i in range(len(word)-2):
                if word[i] == word[i+2]:
                    final_list2.append(word)   
                    break
            break
word_set=set(final_list2)
print("task 1: " + str(len(final_list1)))
print("task 2: " + str(len(final_list2)))
print("task 2: " + str(len(word_set)))