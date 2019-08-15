vovels = ['a', 'e', 'i', 'o', 'u']
word = input("Gimme some string: ")
found = {}

for letter in word:
    if letter in vovels:
        found.setdefault(letter, 0)
        found[letter] += 1

for k, v in sorted(found.items()):
    print(k, 'was found', v, 'time(s).')
