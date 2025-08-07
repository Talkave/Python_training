# --- Day 11: Corporate Policy ---
# Santa's previous password expired, and he needs help choosing a new one.

# To help him remember his new password after the old one expires, Santa has devised a method of coming up with a password based on the previous one. 
# Corporate policy dictates that passwords must be exactly eight lowercase letters (for security reasons), 
# so he finds his new password by incrementing his old password string repeatedly until it is valid.

# Incrementing is just like counting with numbers: xx, xy, xz, ya, yb, and so on. 
# Increase the rightmost letter one step; if it was z, it wraps around to a, and repeat with the next letter to the left until one doesn't wrap around.

# Unfortunately for Santa, a new Security-Elf recently started, and he has imposed some additional password requirements:

# Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
# Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters and are therefore confusing.
# Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.
# For example:

# hijklmmn meets the first requirement (because it contains the straight hij) but fails the second requirement requirement (because it contains i and l).
# abbceffg meets the third requirement (because it repeats bb and ff) but fails the first requirement.
# abbcegjk fails the third requirement, because it only has one double letter (bb).
# The next password after abcdefgh is abcdffaa.
# The next password after ghijklmn is ghjaabcc, because you eventually skip all the passwords that start with ghi..., since i is not allowed.
# Given Santa's current password (your puzzle input), what should his next password be?

# Your puzzle input is hxbxwxba.

test_input = "abcdefgh" 
mode = "input"
#mode = "test_input"

if mode == "input":
    input_path = "./Advent of code/input_day11.txt"
    file = open(input_path)
    input = str(file.read())
    print("MODE = INPUT")
elif mode == "test_input":
    input = test_input
    print("MODE = TEST")

# print(ord('i')) # 105
# print(ord('o')) # 111
# print(ord('l')) # 108
# ord('a') = 97 # podobne zadanie do dzień 5.
# ord('z') = 122 # wartości ascii alfabetu do iterowania 
# chr(122) = 'z' # odwrotne działanie
def if_banned(s):
    # warunek 1: sprawdzamy pary
    i = 0
    pairs = 0
    while i < len(s) - 1: 
        if s[i] == s[i+1]:
            pairs += 1
            i += 2    
        else:
            i += 1
    if pairs < 2 :
        return True
    # warunek 2: sprawdzamy czy jest i o l

    if any(char in ['i','o','l'] for char in s):
        return True
    # warunek 3: sprawdzamy czy jest straight 'abc' 'bcd' itd.
    for j in range(len(s) - 2): 
        if ord(s[j+2]) - ord(s[j+1]) == 1  and ord(s[j+1]) - ord(s[j]) == 1:
            return False
    return True

def pass_generator(password):
    password = list(password) # zamień na listę bo w stringach nie da się zamieniać znaków
    while True:
        i = len(password) - 1 # inicjujemy iterator od końca słowa
        while i >= 0:
            new_ord = ord(password[i]) + 1 # dodajemy do ord + 1 żeby przeskakiwać po alfabecie
            if new_ord > 122: # jeśli przeskoczyłeś 'z':
                password[i] = 'a' # w tym miejscu wstaw 'a', można było dać chr(97) ale na chuj jak to samo daje 'a'
                i -= 1 # idziemy w lewo po słowie
            else:
                password[i] = chr(new_ord) # w przeciwnym wypadku w tym miejscu wstaw nowy ord z linijki 73, czyli z 'a' zrob 'b' , z 'b' 'c' itd. aż do z
                break # wyjdź z pętli bo zamieniłeś iterowany znak na nowy
        new_password = ''.join(password) # zlep z powrotem listę w jednego stringa
        if not if_banned(new_password): # jeśli nie jest zbanowane nowe haslo to je zwróć
            return new_password
        
        password = list(new_password) # do kolejnej iteracji 

print(pass_generator("hxbxxyzz"))