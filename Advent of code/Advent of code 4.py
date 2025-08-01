"""--- Day 4: The Ideal Stocking Stuffer ---
Santa needs help mining some AdventCoins (very similar to bitcoins) to use as gifts for all the economically forward-thinking little girls and boys.

To do this, he needs to find MD5 hashes which, in hexadecimal, start with at least five zeroes. The input to the MD5 hash is some secret key (your puzzle input, given below) followed by a number in decimal. To mine AdventCoins, you must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...) that produces such a hash.

For example:

If your secret key is abcdef, the answer is 609043, because the MD5 hash of abcdef609043 starts with five zeroes (000001dbbfa...), and it is the lowest such number to do so.
If your secret key is pqrstuv, the lowest number it combines with to make an MD5 hash starting with five zeroes is 1048970; that is, the MD5 hash of pqrstuv1048970 looks like 000006136ef....
Your puzzle input is ckczppom.

--- Part Two ---
Now find one that starts with six zeroes.
"""
#test_input = "abcdef" # 609043
test_input = "pqrstuv" # 1048970
mode = "input"
#mode = "test_input"

import hashlib

if mode == "input":
    input_path = "./Advent of code/input_day4.txt"
    file = open(input_path)
    input = file.read()
elif mode == "test_input":
    input = test_input

test_number = 0
test_hash = input + str(test_number)
md5_hash = hashlib.md5(test_hash.encode()).hexdigest()
while md5_hash[:6] != "000000":
    test_hash = input + str(test_number)
    md5_hash = hashlib.md5(test_hash.encode()).hexdigest()
    test_number += 1
print(test_hash)
print(md5_hash)


"""for test_number in range(0,100000000000000):
    test_hash = input + str(test_number)
    md5_hash = hashlib.md5(test_hash.encode()).hexdigest()
    if md5_hash[:5] == "00000":
        print(md5_hash)
        break
    test_number += 1
print(test_hash)
for test_number in range(0, test_number):
    test_hash = input + str(test_number)
    md5_hash = hashlib.md5(test_hash.encode()).hexdigest()
    if md5_hash[:5] == "00000":
        print(md5_hash)
        break
    test_number += 1"""