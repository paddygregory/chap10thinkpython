hello = dict([('one', 1), ('two', 2), ('three', 3 )])

for letters in hello:
    print(letters)

for letters in hello.values():
    print(letters)

for letters in hello:
    value = hello[letters]
    print(letters, value)

