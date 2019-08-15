phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

for i in range(3, 6, 2):
    plist[i] = plist[i + 2]
plist = plist[1:-5]

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
