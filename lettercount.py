from sys import argv
# import string

char_counts = {}
alphabet = "abcdefghijklmnopqrstuvwxyz"
for letter in alphabet:
    char_counts[letter] = 0

script, filename = argv

with open(filename) as f:
    filetext = f.read()
    for char in filetext:
        if char.isalpha():
            char = char.lower()
            char_counts[char] = char_counts.get(char) + 1

for char in sorted(char_counts):
    print char_counts[char]

# ascii_list = []

# for x in range(123):
#     ascii_list.append(0)

# if char.isalpha():
#     char = char.lower()
#     ascii_value = ord(char)
#     ascii_list[ascii_value] += 1

# for x in range(97,123):
#     print char(x), ascii_list[x]