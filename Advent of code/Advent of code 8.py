# """--- Day 8: Matchsticks ---
# Space on the sleigh is limited this year, and so Santa will be bringing his list as a digital copy. 
# He needs to know how much space it will take up when stored.

# It is common in many programming languages to provide a way to escape special characters in strings. 
# For example, C, JavaScript, Perl, Python, and even PHP handle special characters in very similar ways.

# However, it is important to realize the difference between the number of characters in the code representation of the string literal 

# and the number of characters in the in-memory string itself.

# For example:

# "" is 2 characters of code (the two double quotes), but the string contains zero characters.
# "abc" is 5 characters of code, but 3 characters in the string data.
# "aaa\"aaa" is 10 characters of code, but the string itself contains six "a" characters and a single, escaped quote character, for a total of 7 characters in the string data.
# "\x27" is 6 characters of code, but the string itself contains just one - an apostrophe ('), escaped using hexadecimal notation.
# Santa's list is a file that contains many double-quoted string literals, one on each line. 
# The only escape sequences used are \\ (which represents a single backslash), \" (which represents a lone double-quote character), and \x plus two hexadecimal characters (which represents a single character with that ASCII code).

# Disregarding the whitespace in the file, 
# what is the number of characters of code for string literals minus the number of characters in memory for the values of the strings in total for the entire file?

# For example, given the four strings above, the total number of characters of string code (2 + 5 + 10 + 6 = 23) minus the total number of characters in memory for string values (0 + 3 + 7 + 1 = 11) is 23 - 11 = 12."""

test_input = ["","abc","aaa\"aaa","\x27"] # 12
mode = "input"
# mode = "test_input"

if mode == "input":
    input_path = "./Advent of code/input_day8.txt"
    file = open(input_path)
    input = file.read().splitlines()
    print("MODE = INPUT")
elif mode == "test_input":
    input = test_input
    print("MODE = TEST")

def decoded_length(s): # chcemy obliczyć ile znaków zajmuje w pamięci dane słowo
   # chcemy stworzyć logikę dla znaków specjalnych w pythonie (escape sequences), czyli takich, które są ignorowane/interpretowane przez program automatycznie, i.e. \\, \",\x** gdzie gwiazdki to dowolne 2 symbole
    s = s[1:-1] # obcinamy cudzysłowia na końcach
    i = 0 # inicjujemy iterator
    length = 0 # inicjujemy długość słowa
    while i < len(s): # jedziemy od początku słowa, jeżeli i jest mniejsze od długości s (czyli słowo z obciętymi cudzysłowiami)
        if s[i] == '\\': #jeżeli jakikolwiek indeksy słowa są równe \, czyli początek escape sequence to, musimy pisać dwa \, bo python intepretuje to jako jeden \:
            if i + 1 < len(s): # jeżeli jest jeszcze kolejny znak po tym to:
                if s[i+1] in ('\\', '"'): # jeżeli w kolejnym indeksie znajduje się \ albo " 
                    length += 1 # to długość słowa zwiększ o 1
                    i += 2 # i przeskocz o 2 indeksy do przodu na słowie, 
                    # np. w sytuacji abc\\abc\"abc\xd2abc doszliśmy do indeksu 3, czyli \ i sprawdziliśmy czy kolejny znak jest \ albo ", 
                    # i skoro tak jest to dodaliśmy 1 do długości słowa i przeskoczyliśmy na indeks 5 czyli kolejne a
                elif s[i+1] == 'x' and i + 3 < len(s): # lub jeśli indeks który znajduje się po \ jest równy x oraz są jeszcze po nim 2 inne symbole(nie jest to koniec słowa):
                    length += 1 # zwiększ długość słowa o 1
                    i += 4 # przeskocz o 4 indeksy do przodu na słowie np. w słowie abc\\abc\"abc\xd2abc doszliśmy do indeksu 13, w którym jest \ a po nim bezpośrednio jest x,
                            # to dodajemy 1 do długości słowa i przeskakujemy o 4 indeksy, do indeksu 17, czyli a 
                else:
                    length += 1 # w każdym przeciwnym wypadku (czyli jeśli nie jest to początek escape sequence), dodaj 1 do długości słowa i leć na kolejny znak
                    i += 1
            else:
                length += 1
                i += 1
        else:
            length += 1
            i += 1
    return length #zwróć całą długość słowa (które jest w pamięci)

total_code = 0 # inicjacja zmiennych przed pętlą
total_memory = 0

for line in input: # dla każdej linijki w inpucie
    code_len = len(line) # to co jest w kodzie
    mem_len = decoded_length(line) # to co jest w pamięci
    total_code += code_len
    total_memory += mem_len

print(total_code - total_memory)

"""--- Part Two ---
Now, let's go the other way. 
In addition to finding the number of characters of code, 

you should now encode each code representation as a new string and find the number of characters of the new encoded representation, 
including the surrounding double quotes.

For example:

"" encodes to "\"\"", an increase from 2 characters to 6.
"abc" encodes to "\"abc\"", an increase from 5 characters to 9.
"aaa\"aaa" encodes to "\"aaa\\\"aaa\"", an increase from 10 characters to 16.
"\x27" encodes to "\"\\x27\"", an increase from 6 characters to 11.
Your task is to find the total number of characters to represent the newly encoded strings minus the number of characters of code in each original string literal. 
For example, for the strings above, the total encoded length (6 + 9 + 16 + 11 = 42) minus the characters in the original code representation (23, just like in the first part of this puzzle) is 42 - 23 = 19."""

def encoded_length(s): 
    chars = ['"']  # do każdego słowa na początku mamy dodać " bo python odczytuje stringi bez ""
    for c in s: # więc dla każdego znaku w słowie:
        if c == '"': # jeśli znak jest równy \"
            chars.append('\\"') # dodaj do listy znaków \\"
        elif c == '\\': # jeśli znak jest równy \ 
            chars.append('\\\\') # to dodaj do znaku \\ 
# tak jak na przykład w "aaa\"aaa", to python odczytuje to jako aaa"aaa, czyli na początku słowa dodajemy ", idziemy po a a a dochodzimy do " i dodajemy \"
# idziemy dalej po słowie a a a i doszliśmy do końca
        else: # jeśli słowo nie zawiera żadnej escape sequence
            chars.append(c) # dodaj całe słowo do chars
    chars.append('"')  # i na koniec słowa dodajemy drugi cudzysłów
    return len(''.join(chars)) # i teraz sklej całą powstałą w ten sposób listę chars bez żadnych przerw w jeden string i zwróć jego długość

total_code = 0
total_encoded = 0

for line in input: # robimy analogicznie jak 1 część tylko odwrotnie bo total_code będzie mniejszy niż total_encoded
    code_len = len(line) # to co w kodzie
    enc_len = encoded_length(line) # to co w pamięci
    total_code += code_len
    total_encoded += enc_len

print(total_encoded - total_code) # 2046
